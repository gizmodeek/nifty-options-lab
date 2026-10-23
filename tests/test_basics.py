import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from strategies import Leg, strategy_payoff, iron_condor, summarise  # noqa: E402
from probability import prob_above, expected_move  # noqa: E402
from risk import max_lots_for_risk, stop_loss_hit, reward_to_risk  # noqa: E402


def test_long_call_payoff():
    legs = [Leg("CE", 100, 5, "buy")]
    assert strategy_payoff(legs, 90) == -5
    assert strategy_payoff(legs, 110) == 5


def test_iron_condor_max_profit_and_loss():
    legs = iron_condor(put_buy=90, put_sell=95, call_sell=105, call_buy=110,
                       put_buy_prem=1, put_sell_prem=3, call_sell_prem=3, call_buy_prem=1)
    s = summarise(legs, lower=80, upper=120, step=0.5)
    assert s["max_profit"] == 4        # net credit 4 when price stays between 95 and 105
    assert s["max_loss"] == -1         # spread width 5 minus credit 4
    assert len(s["breakevens"]) == 2


def test_probability_sanity():
    p = prob_above(spot=100, strike=100, iv=0.2, days=30)
    assert 0.45 < p < 0.55
    assert prob_above(100, 200, 0.2, 30) < 0.01


def test_expected_move():
    assert math.isclose(expected_move(100, 0.2, 365), 20)


def test_risk_sizing_and_stop():
    assert max_lots_for_risk(500000, 0.01, 40, 75) == 1
    assert stop_loss_hit(entry_value=100, current_value=50, stop_pct=0.5) is True
    assert stop_loss_hit(entry_value=100, current_value=60, stop_pct=0.5) is False
    assert reward_to_risk(4, 1) == 4
