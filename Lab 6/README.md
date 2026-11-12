# Lab 6 – Code and Branch Coverage Analysis

Assigned repo: `SETAPESU26/L6_L7_29_thermostat_control` (Smart Thermostat Controller). Module under test: `thermostat_control.py`.

| Run | Tests | Line coverage | Branch coverage |
|---|---:|---:|---:|
| Starter `test_thermostat_control.py` | 2 | 26% (9/35) | 19% combined |
| `CodeCoverageTest_thermostat_control.py` | 15 | **100%** (35/35) | 100% (28/28) |
| `BranchCoverageTest_thermostat_control.py` | 29 | **100%** | **100%** (28/28, 0 partial) |

**Code coverage tests** drive execution to each of the 15 `return` statements once.
**Branch coverage tests** go decision by decision (D1–D13 plus the loop), making each condition both True and False *at its boundary*: hours 5/6, 8/9, 16/17, 21/22; temperature difference of exactly ±1 vs ±0.9; outside temperature 4/5 and 30/31; reading equal to the limit; exactly half the readings over the limit.

**Observation:** in this module every `if` ends in a `return`, so reaching every line already forces every branch. That's why line coverage gave 100% branch coverage too. The branch suite is still stronger: the line suite would pass if `hour >= 22` were mistakenly written `hour > 22`, but the branch suite's boundary cases (hour 22) catch it.

## Commands
```
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_thermostat_control.py          # line coverage
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_thermostat_control.py  # branch coverage
coverage report -m
```
Or run `run_coverage.ps1 code` / `run_coverage.ps1 branch`.

## Screenshots
`screenshots/code_coverage.png`, `screenshots/branch_coverage.png`: terminal output after reaching the targets.
