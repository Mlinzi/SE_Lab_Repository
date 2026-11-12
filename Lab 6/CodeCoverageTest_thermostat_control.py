"""Lab 6 - Code (line) coverage tests for thermostat_control.py.

Goal: execute every line of the module at least once.
Each test drives execution to one specific return statement.
"""
from thermostat_control import target_temperature, hvac_action, energy_alert


# ---------- target_temperature ----------
def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_at_night():
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_mode_during_day():
    assert target_temperature("sleep", True, 12) == 20


def test_home_but_unoccupied():
    assert target_temperature("home", False, 12) == 18


def test_occupied_morning():
    assert target_temperature("home", True, 7) == 22


def test_occupied_evening():
    assert target_temperature("home", True, 18) == 21


def test_occupied_midday_default():
    assert target_temperature("home", True, 12) == 20


# ---------- hvac_action ----------
def test_idle_when_close_to_target():
    assert hvac_action(21.5, 22, 15) == "idle"


def test_heat_boost_when_freezing_outside():
    assert hvac_action(15, 22, 0) == "heat_boost"


def test_heat_when_mild_outside():
    assert hvac_action(18, 22, 15) == "heat"


def test_cool_boost_when_hot_outside():
    assert hvac_action(28, 22, 35) == "cool_boost"


def test_cool_when_warm_outside():
    assert hvac_action(26, 22, 25) == "cool"


# ---------- energy_alert ----------
def test_no_readings():
    assert energy_alert([], 10) == "ok"


def test_critical_when_most_readings_over_limit():
    assert energy_alert([12, 15, 9], 10) == "critical"


def test_warning_when_some_readings_over_limit():
    assert energy_alert([12, 5, 6, 7], 10) == "warning"
