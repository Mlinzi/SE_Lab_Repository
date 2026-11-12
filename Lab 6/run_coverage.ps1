# Lab 6 - run from this folder:  powershell -ExecutionPolicy Bypass -File .\run_coverage.ps1 code|branch
param([ValidateSet('code','branch')][string]$kind = 'code')
if ($kind -eq 'code') {
    Write-Host "`n=== CODE (LINE) COVERAGE ===" -ForegroundColor Cyan
    python -m coverage run -m pytest -v CodeCoverageTest_thermostat_control.py
} else {
    Write-Host "`n=== BRANCH COVERAGE ===" -ForegroundColor Cyan
    python -m coverage run --branch -m pytest -v BranchCoverageTest_thermostat_control.py
}
python -m coverage report -m --include=thermostat_control.py
