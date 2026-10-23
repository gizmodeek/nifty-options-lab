"""Rough probability estimates from the Black-Scholes model (educational).

Important: these are model estimates, not forecasts. They assume a volatility
number you supply (implied volatility, IV) and a log-normal price distribution.
Real markets have fat tails and jumps, so treat results as a rough guide.
"""

import math


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def prob_above(spot: float, strike: float, iv: float, days: float, rate: float = 0.065) -> float:
    """Model probability that spot is above `strike` at expiry (risk-neutral, rough)."""
    t = days / 365.0
    d2 = (math.log(spot / strike) + (rate - 0.5 * iv * iv) * t) / (iv * math.sqrt(t))
    return norm_cdf(d2)


def prob_below(spot: float, strike: float, iv: float, days: float, rate: float = 0.065) -> float:
    return 1.0 - prob_above(spot, strike, iv, days, rate)


def prob_expires_between(spot: float, lower: float, upper: float, iv: float, days: float) -> float:
    """Model probability that expiry lands between two strikes (e.g. an iron condor's range)."""
    return prob_below(spot, upper, iv, days) - prob_below(spot, lower, iv, days)


def expected_move(spot: float, iv: float, days: float) -> float:
    """One-standard-deviation move implied by IV over the period, in points."""
    return spot * iv * math.sqrt(days / 365.0)
