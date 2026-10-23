"""Risk checks you should run before any trade (educational).

These functions only do arithmetic. They never place orders.
"""


def max_lots_for_risk(capital: float, risk_pct: float, max_loss_per_unit: float, lot_size: int) -> int:
    """How many lots keep the worst-case loss within `risk_pct` of capital.

    Example: capital 5,00,000, risk 1%, max loss 40 points per unit, lot 75 -> 1 lot
    (5000 risk budget / (40 * 75 = 3000 per lot) = 1.67, rounded down).
    """
    if capital <= 0 or not (0 < risk_pct <= 0.02) or max_loss_per_unit <= 0 or lot_size <= 0:
        raise ValueError("check inputs: risk_pct should be at most 2% for a beginner")
    budget = capital * risk_pct
    per_lot = max_loss_per_unit * lot_size
    return int(budget // per_lot)


def stop_loss_hit(entry_value: float, current_value: float, stop_pct: float) -> bool:
    """True if the position has lost `stop_pct` of its entry value (e.g. 0.5 = 50%)."""
    if entry_value <= 0:
        raise ValueError("entry_value must be positive")
    return current_value <= entry_value * (1.0 - stop_pct)


def reward_to_risk(max_profit: float, max_loss: float) -> float:
    if max_loss <= 0:
        raise ValueError("max_loss must be a positive number")
    return max_profit / max_loss
