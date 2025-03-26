<#
.SYNOPSIS
    Script to run all test cases in the samples directory through the classifiers.
.DESCRIPTION
    This script loops through all .in files in the samples directory and passes them
    to both the NumPy and non-NumPy versions of the classifier, comparing results.
.EXAMPLE
    .\run_all_tests.ps1
.EXAMPLE
    .\run_all_tests.ps1 -Implementation "both" -Verbose
.PARAMETER Implementation
    Which implementation to test: "numpy", "no_numpy", or "both" (default)
.PARAMETER SamplesDir
    Directory containing the sample test files (default: "./samples")
#>

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("numpy", "no_numpy", "both")]
    [string]$Implementation = "both",
    
    [Parameter(Mandatory=$false)]
    [string]$SamplesDir = "./samples"
)

# Enable verbose output if requested
$VerbosePreference = $PSCmdlet.MyInvocation.BoundParameters["Verbose"] -eq $true ? "Continue" : "SilentlyContinue"

# Check if samples directory exists
if (-not (Test-Path $SamplesDir)) {
    Write-Error "Samples directory '$SamplesDir' not found. Please run download_samples.py first."
    exit 1
}

# Get all .in files in the samples directory
$testFiles = Get-ChildItem -Path $SamplesDir -Filter "*.in" | Sort-Object Name

if ($testFiles.Count -eq 0) {
    Write-Error "No test files found in '$SamplesDir'. Please run download_samples.py first."
    exit 1
}

Write-Host "Found $($testFiles.Count) test files in '$SamplesDir'" -ForegroundColor Green

# Create results table
$results = @()

# Create style counters 
$numpyStyleCounts = @{1=0; 2=0; 3=0; 4=0}
$noNumpyStyleCounts = @{1=0; 2=0; 3=0; 4=0}

# Initialize counters for matching results
$matchCount = 0
$mismatchCount = 0

# Process each test file
foreach ($file in $testFiles) {
    $testName = $file.Name
    Write-Host "`nProcessing test: $testName" -ForegroundColor Cyan
    
    # Extract expected style from filename
    $expectedStyle = if ($testName -match 'style-(\d+)-') { [int]$Matches[1] } else { "unknown" }
    
    $numpyResult = $null
    $noNumpyResult = $null
    
    # Test with NumPy implementation
    if ($Implementation -eq "numpy" -or $Implementation -eq "both") {
        Write-Verbose "Running NumPy implementation on $testName"
        $numpyStart = Get-Date
        $numpyResult = (Get-Content $file.FullName | python .\classify.py).Trim()
        $numpyEnd = Get-Date
        $numpyTime = ($numpyEnd - $numpyStart).TotalSeconds
        
        if ($numpyResult -match '^\d+$') {
            $numpyStyle = [int]$numpyResult
            $numpyStyleCounts[$numpyStyle]++
            Write-Host "  NumPy result: Style $numpyResult (${numpyTime:F3}s)" -ForegroundColor Yellow
        }
    }
    
    # Test with non-NumPy implementation
    if ($Implementation -eq "no_numpy" -or $Implementation -eq "both") {
        Write-Verbose "Running non-NumPy implementation on $testName"
        $noNumpyStart = Get-Date
        $noNumpyResult = (Get-Content $file.FullName | python .\classify_no_numpy.py).Trim()
        $noNumpyEnd = Get-Date
        $noNumpyTime = ($noNumpyEnd - $noNumpyStart).TotalSeconds
        
        if ($noNumpyResult -match '^\d+$') {
            $noNumpyStyle = [int]$noNumpyResult
            $noNumpyStyleCounts[$noNumpyStyle]++
            Write-Host "  Non-NumPy result: Style $noNumpyResult (${noNumpyTime:F3}s)" -ForegroundColor Blue
        }
    }
    
    # Check if results match when both implementations are run
    $match = "N/A"
    if ($Implementation -eq "both" -and $numpyResult -and $noNumpyResult) {
        $match = $numpyResult -eq $noNumpyResult ? "Yes" : "No"
        if ($match -eq "Yes") {
            $matchCount++
        } else {
            $mismatchCount++
        }
    }
    
    # Add to results table
    $result = [PSCustomObject]@{
        TestFile = $testName
        ExpectedStyle = $expectedStyle
        NumpyResult = $numpyResult
        NoNumpyResult = $noNumpyResult
        Match = $match
    }
    $results += $result
}

# Display summary
Write-Host "`n----------------------" -ForegroundColor Magenta
Write-Host "Classification Results" -ForegroundColor Magenta
Write-Host "----------------------" -ForegroundColor Magenta

if ($Implementation -eq "numpy" -or $Implementation -eq "both") {
    Write-Host "`nNumPy Implementation Style Counts:" -ForegroundColor Yellow
    foreach ($styleNum in (1..4)) {
        Write-Host "  Style $styleNum`: $($numpyStyleCounts[$styleNum]) images"
    }
}

if ($Implementation -eq "no_numpy" -or $Implementation -eq "both") {
    Write-Host "`nNon-NumPy Implementation Style Counts:" -ForegroundColor Blue
    foreach ($styleNum in (1..4)) {
        Write-Host "  Style $styleNum`: $($noNumpyStyleCounts[$styleNum]) images"
    }
}

if ($Implementation -eq "both") {
    Write-Host "`nImplementation Comparison:" -ForegroundColor Green
    Write-Host "  Matching results: $matchCount"
    Write-Host "  Mismatched results: $mismatchCount"
    
    if ($testFiles.Count -gt 0) {
        $matchPercentage = ($matchCount / $testFiles.Count) * 100
        Write-Host "  Agreement rate: ${matchPercentage:F1}%" -ForegroundColor $(if ($matchPercentage -ge 90) { "Green" } elseif ($matchPercentage -ge 70) { "Yellow" } else { "Red" })
    }
}

# Export detailed results to CSV
$csvPath = "classification_results.csv"
$results | Export-Csv -Path $csvPath -NoTypeInformation

Write-Host "`nDetailed results have been saved to: $csvPath" -ForegroundColor Green
Write-Host "Run 'Import-Csv $csvPath | Format-Table' to view detailed results in PowerShell"
Write-Host "Run 'Import-Csv $csvPath | Where-Object {`$_.Match -eq 'No'} | Format-Table' to see mismatches"
