<#
.SYNOPSIS
    Simpler script to run multiple test cases with a single classifier.
.DESCRIPTION
    This script allows quickly testing either classifier with multiple test cases
    without detailed comparisons.
.EXAMPLE
    .\run_batch_test.ps1 -Implementation "no_numpy"
.PARAMETER Implementation
    Which implementation to use: "numpy" (default) or "no_numpy"
.PARAMETER Pattern
    Optional file pattern to filter test files (default: all *.in files)
#>

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("numpy", "no_numpy")]
    [string]$Implementation = "numpy",
    
    [Parameter(Mandatory=$false)]
    [string]$Pattern = "*"
)

# Select the right script based on implementation
$script = if ($Implementation -eq "numpy") { ".\classify.py" } else { ".\classify_no_numpy.py" }

# Get test files matching the pattern
$testFiles = Get-ChildItem -Path ".\samples" -Filter "*.in" | Where-Object { $_.Name -like $Pattern }

if ($testFiles.Count -eq 0) {
    Write-Host "No test files found matching pattern '$Pattern'" -ForegroundColor Red
    exit
}

Write-Host "Running $Implementation implementation on $($testFiles.Count) test files:" -ForegroundColor Cyan

foreach ($file in $testFiles) {
    $testName = $file.Name
    # Extract expected style from filename if possible
    $expectedStyle = if ($testName -match 'style-(\d+)-') { [int]$Matches[1] } else { "unknown" }
    
    Write-Host -NoNewline "  $testName (expected: Style $expectedStyle): "
    $result = (Get-Content $file.FullName | python $script).Trim()
    
    # Determine color based on whether result matches expected style
    $color = if ($result -eq $expectedStyle) { "Green" } else { "Red" }
    Write-Host "Style $result" -ForegroundColor $color
}

Write-Host "`nAll tests completed!" -ForegroundColor Green
