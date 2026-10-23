"""Payoff math for basic option strategies (educational, no broker connection).

All prices are per unit of the underlying. Multiply by lot size for rupee values.
Premiums are what you pay (positive, for buys) or receive (positive, for sells).
"""

from dataclasses import dataclass


@dataclass
class Leg:
    kind: str      # "CE" (call) or "PE" (put)
    strike: float
    premium: float # per unit, always positive
    side: str      # "buy" or "sell"


def leg_payoff(leg: Leg, spot_at_expiry: float) -> float:
    """Profit or loss of one leg at expiry, per unit."""
    if leg.kind == "CE":
        intrinsic = max(spot_at_expiry - leg.strike, 0.0)
    elif leg.kind == "PE":
        intrinsic = max(leg.strike - spot_at_expiry, 0.0)
    else:
        raise ValueError("kind must be CE or PE")

    if leg.side == "buy":
        return intrinsic - leg.premium
    if leg.side == "sell":
        return leg.premium - intrinsic
    raise ValueError("side must be buy or sell")


def strategy_payoff(legs: list[Leg], spot_at_expiry: float) -> float:
    return sum(leg_payoff(leg, spot_at_expiry) for leg in legs)


def iron_condor(put_buy: float, put_sell: float, call_sell: float, call_buy: float,
                put_buy_prem: float, put_sell_prem: float,
                call_sell_prem: float, call_buy_prem: float) -> list[Leg]:
    """Sell an OTM put and call, buy further-OTM protection on each side.

    Example layout (Nifty, illustrative numbers only):
        buy PE 22000 | sell PE 22300 | sell CE 23700 | buy CE 24000
    """
    return [
        Leg("PE", put_buy, put_buy_prem, "buy"),
        Leg("PE", put_sell, put_sell_prem, "sell"),
        Leg("CE", call_sell, call_sell_prem, "sell"),
        Leg("CE", call_buy, call_buy_prem, "buy"),
    ]


def summarise(legs: list[Leg], lower: float, upper: float, step: float = 10.0) -> dict:
    """Scan expiry prices from `lower` to `upper` and report max profit, max loss, breakevens."""
    prices = []
    x = lower
    while x <= upper + 1e-9:
        prices.append(x)
        x += step
    pnl = [(p, strategy_payoff(legs, p)) for p in prices]
    max_profit = max(v for _, v in pnl)
    max_loss = min(v for _, v in pnl)
    breakevens = []
    for (p1, v1), (p2, v2) in zip(pnl, pnl[1:]):
        if v1 == 0:
            breakevens.append(p1)
        elif v1 * v2 < 0:
            breakevens.append(round(p1 + (p2 - p1) * (-v1) / (v2 - v1), 2))
    return {"max_profit": round(max_profit, 2), "max_loss": round(max_loss, 2),
            "breakevens": breakevens}
