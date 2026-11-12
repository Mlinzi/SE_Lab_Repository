"""Smart Thermostat Controller - hardened after Hypothesis fuzz testing (Lab 7).

Every function validates its input and returns None for anything invalid
instead of raising, so bad user or sensor input can't crash the controller.
"""
import math
import re

# number followed by a mandatory C/F unit, e.g. "21.5C", "-3f", " 70 F "
_SETPOINT_RE = re.compile(r"^\s*([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*([CcFf])\s*$")
_TIME_RE = re.compile(r"^\s*(\d{1,2}):(\d{2})\s*$")


def parse_setpoint(text):
    """'21.5C' -> 21.5, '70F' -> 21.1 (Celsius). Invalid -> None."""
    if not isinstance(text, str):
        return None                                  # bug: None/non-str crashed (TypeError)
    match = _SETPOINT_RE.match(text)
    if not match:
        return None                                  # bug: '', '21' (no unit), 'abcC' crashed or misparsed
    value = float(match.group(1))
    if not math.isfinite(value):
        return None                                  # bug: '1e400C' gave inf
    if match.group(2).upper() == 'F':
        value = (value - 32) * 5 / 9
    return round(value, 1)


def average_temperature(readings_csv):
    """'20.5,21,22.5' -> 21.33... Invalid or empty -> None."""
    if not isinstance(readings_csv, str):
        return None                                  # bug: None crashed (AttributeError)
    values = []
    for part in readings_csv.split(','):
        try:
            value = float(part)
        except ValueError:
            return None                              # bug: '', '1,,3', 'abc' crashed (ValueError)
        if not math.isfinite(value):
            return None                              # bug: 'nan'/'inf' produced nan/inf averages
        values.append(value)
    return sum(values) / len(values)                 # split() always yields >= 1 part: no ZeroDivision


def schedule_slot(time_text):
    """'07:30' -> 'day 30', '05:05' -> 'night 5'. Invalid -> None."""
    if not isinstance(time_text, str):
        return None                                  # bug: None crashed (AttributeError)
    match = _TIME_RE.match(time_text)
    if not match:
        return None                                  # bug: '', ':', '1:2:3', 'ab:cd' crashed
    hour, minute = int(match.group(1)), int(match.group(2))
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        return None                                  # bug: '24:00', '07:75' were accepted
    if hour < 6:
        return 'night ' + str(minute)                # bug: night kept raw text ('night 05' vs 'day 5')
    return 'day ' + str(minute)


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result if result is not None else "Invalid setpoint")

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    result = average_temperature(user_input)
    print("Average Temperature:", result if result is not None else "Invalid readings")

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result if result is not None else "Invalid time")


if __name__ == "__main__":
    main()
