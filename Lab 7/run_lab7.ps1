# Lab 7 screenshots. Run from this folder:
#   powershell -ExecutionPolicy Bypass -File .\run_lab7.ps1 <step>
#   step2 = original program     step4 = fuzz tests vs original (FAIL)
#   step5 = fixed program        step6 = fuzz tests vs fixed (PASS)
param([ValidateSet('step2','step4','step5','step6')][string]$step)
switch ($step) {
  'step2' { python original\thermostat_control.py }
  'step4' { Copy-Item test_thermostat_control.py original\ -Force
            Push-Location original; python -m pytest test_thermostat_control.py -p no:cacheprovider --tb=line; Pop-Location
            Remove-Item original\test_thermostat_control.py }
  'step5' { python thermostat_control.py }
  'step6' { python -m pytest test_thermostat_control.py -v -p no:cacheprovider }
}
