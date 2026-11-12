"""Lab 6 - Branch coverage tests for thermostat_control.py.

Goal: every decision (if / for) evaluates both True and False, tested at its
boundary values. Each test name states the decision and the outcome taken.
"""
import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# ===== target_temperature =====
# D1: mode == "away"
def test_d1_away_true():
    assert target_temperature("away", False, 3) == 16


# D2: mode == "sleep"  /  D3: hour < 6 or hour >= 22
@pytest.mark.parametrize("hour, expected", [
    (0, 18),    # D3 true via hour < 6
    (5, 18),    # D3 true, boundary just below 6
    (6, 20),    # D3 false, boundary hour == 6
    (21, 20),   # D3 false, boundary just below 22
    (22, 18),   # D3 true via hour >= 22, boundary
])
def test_d2_sleep_true_d3_both_outcomes(hour, expected):
    assert target_temperature("sleep", True, hour) == expected


# D4: not occupied
def test_d4_unoccupied_true():
    assert target_temperature("home", False, 7) == 18


# D5: 6 <= hour < 9   /  D6: 17 <= hour < 22
@pytest.mark.parametrize("hour, expected", [
    (5, 20),    # D5 false (below 6), D6 false -> default
    (6, 22),    # D5 true, lower boundary
    (8, 22),    # D5 true, upper edge
    (9, 20),    # D5 false at 9, D6 false
    (16, 20),   # D6 false, just below 17
    (17, 21),   # D6 true, lower boundary
    (21, 21),   # D6 true, upper edge
    (22, 20),   # D6 false at 22 -> default
])
def test_d5_d6_occupied_time_windows(hour, expected):
    assert target_temperature("home", True, hour) == expected


# ===== hvac_action =====
# D7: abs(diff) < 1   /  D8: diff > 0   /  D9: outside < 5   /  D10: outside > 30
@pytest.mark.parametrize("current, target, outside, expected", [
    (22, 22, 20, "idle"),        # D7 true, diff 0
    (21.1, 22, 20, "idle"),      # D7 true, diff 0.9
    (22.9, 22, 20, "idle"),      # D7 true, diff -0.9
    (21, 22, 20, "heat"),        # D7 false at exactly +1, D8 true, D9 false
    (21, 22, 4, "heat_boost"),   # D9 true just below 5
    (21, 22, 5, "heat"),         # D9 false at boundary 5
    (23, 22, 20, "cool"),        # D7 false at exactly -1, D8 false, D10 false
    (23, 22, 30, "cool"),        # D10 false at boundary 30
    (23, 22, 31, "cool_boost"),  # D10 true just above 30
])
def test_hvac_all_decisions(current, target, outside, expected):
    assert hvac_action(current, target, outside) == expected


# ===== energy_alert =====
# L1: for-loop body runs zero / many times   D11: reading > limit
# D12: over == 0   D13: over * 2 > len(readings)
def test_l1_loop_zero_iterations():
    assert energy_alert([], 10) == "ok"


def test_d11_all_false_d12_true():
    assert energy_alert([1, 2, 10], 10) == "ok"      # reading == limit is NOT over


def test_d13_false_exactly_half_over():
    assert energy_alert([11, 12, 1, 2], 10) == "warning"  # 2*2 > 4 is False


def test_d13_true_majority_over():
    assert energy_alert([11, 12, 13, 2], 10) == "critical"


def test_d13_true_single_reading_over():
    assert energy_alert([50], 10) == "critical"
