# Lab 7 – Fuzzing for Input Validation Bugs

Assigned repo: `SETAPESU26/L6_L7_29_thermostat_control` (Smart Thermostat Controller), using Hypothesis property-based fuzzing.

| File | Content |
|---|---|
| `thermostat_control.py` | **Fixed** application (hardened: invalid input returns `None`, never raises) |
| `original/thermostat_control.py` | Original buggy version, kept for the before screenshots |
| `test_thermostat_control.py` | Completed Hypothesis tests: 3 no-crash fuzzers + 8 property tests, 500 examples each |
| `Lab7_Submission.pdf` | Screenshots for steps 2, 4, 5 and 6 |

## Results
| | Original | Fixed |
|---|---|---|
| Fuzz tests | **8 failed**, 3 passed | **11 passed** |

## Bugs found by Hypothesis (minimal failing inputs)
| Function | Input | Original behaviour | Fix |
|---|---|---|---|
| parse_setpoint | `None` | TypeError | type check → None |
| parse_setpoint | `''`, `'abcC'` | ValueError | regex: number + mandatory C/F unit |
| parse_setpoint | `'0.0'` (no unit) | silently returned 0.0 (read `'0.'` with unit `'0'`) | unit is required → None |
| parse_setpoint | `'1e400C'` | returned `inf` | reject non-finite |
| average_temperature | `None` | AttributeError | type check → None |
| average_temperature | `''`, `'1,,3'` | ValueError | per-value try/except → None |
| average_temperature | `'20,nan,22'` | returned `nan` | reject non-finite readings |
| schedule_slot | `None` | AttributeError | type check → None |
| schedule_slot | `''`, `':'` | ValueError | regex `H:MM` / `HH:MM` |
| schedule_slot | `'24:00'`, `'00:60'` | accepted as valid | range check 0–23 / 0–59 |
| schedule_slot | `'00:00'` | `'night 00'` but daytime gives `'day 0'` (inconsistent) | normalise minute with `int()` for both |

## Running
```
pip install hypothesis pytest
python thermostat_control.py
python -m pytest test_thermostat_control.py
```
`run_lab7.ps1 step2|step4|step5|step6` reproduces each screenshot step.
