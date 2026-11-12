"""Lab 7 - Hypothesis fuzz tests for thermostat_control.py.

Contract for the hardened module: invalid input returns None (never raises);
valid input returns the correct value.
"""
import math

from hypothesis import given, settings, strategies as st

from thermostat_control import parse_setpoint, average_temperature, schedule_slot

FUZZ = settings(max_examples=500, deadline=None)

# Valid-input generators
finite_temps = st.floats(min_value=-50, max_value=150, allow_nan=False, allow_infinity=False)
valid_times = st.tuples(st.integers(0, 23), st.integers(0, 59))


# ---------------- 1. No-crash fuzzing (random / malformed input) ----------------
@FUZZ
@given(st.text() | st.none())
def test_parse_setpoint_no_crash(s):
    try:
        parse_setpoint(s)
    except Exception as e:
        assert False, f"parse_setpoint crashed on {s!r}: {e!r}"


@FUZZ
@given(st.text() | st.none())
def test_average_temperature_no_crash(s):
    try:
        average_temperature(s)
    except Exception as e:
        assert False, f"average_temperature crashed on {s!r}: {e!r}"


@FUZZ
@given(st.text() | st.none())
def test_schedule_slot_no_crash(s):
    try:
        schedule_slot(s)
    except Exception as e:
        assert False, f"schedule_slot crashed on {s!r}: {e!r}"


# ---------------- 2. Property tests (correctness on valid input) ----------------
@FUZZ
@given(finite_temps)
def test_parse_setpoint_celsius_roundtrip(t):
    assert parse_setpoint(f"{t}C") == round(t, 1)


@FUZZ
@given(finite_temps)
def test_parse_setpoint_fahrenheit_converts(t):
    assert parse_setpoint(f"{t}F") == round((t - 32) * 5 / 9, 1)


@FUZZ
@given(finite_temps)
def test_parse_setpoint_requires_unit(t):
    # "21" has no unit: it must be rejected, not misread as "2" with unit "1"
    assert parse_setpoint(str(t)) is None


@FUZZ
@given(st.lists(finite_temps, min_size=1, max_size=20))
def test_average_within_min_and_max(values):
    avg = average_temperature(",".join(str(v) for v in values))
    assert avg is not None and math.isfinite(avg)
    assert min(values) - 1e-9 <= avg <= max(values) + 1e-9


@FUZZ
@given(st.sampled_from(["nan", "inf", "-inf", "1e400"]))
def test_average_rejects_non_finite(bad):
    assert average_temperature(f"20,{bad},22") is None


@FUZZ
@given(valid_times)
def test_schedule_slot_valid_times(hm):
    h, m = hm
    expected = ("night " if h < 6 else "day ") + str(m)
    assert schedule_slot(f"{h:02d}:{m:02d}") == expected


@FUZZ
@given(st.integers(24, 99) | st.integers(-99, -1), st.integers(0, 59))
def test_schedule_slot_rejects_out_of_range_hour(h, m):
    assert schedule_slot(f"{h}:{m:02d}") is None


@FUZZ
@given(st.integers(0, 23), st.integers(60, 99))
def test_schedule_slot_rejects_out_of_range_minute(h, m):
    assert schedule_slot(f"{h:02d}:{m}") is None
