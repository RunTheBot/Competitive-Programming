<#
.SYNOPSIS
    Script to run tests on all samples and save results to a file.
.DESCRIPTION
    Tests both classify.py and classify_no_numpy.py on all sample files
    and saves the results to a text file for comparison.
.EXAMPLE
    .\run_all_samples.ps1
.PARAMETER Implementation
    Which implementation to test: "numpy", "no_numpy", or "both" (default)
#>

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet("numpy", "no_numpy", "both")]
    [string]$Implementation = "both"
)

# Check if samples directory exists
$SamplesDir = "./samples"
if (-not (Test-Path $SamplesDir)) {
    Write-Error "Samples directory not found. Please run download_samples.py first."
    exit 1
}

# Get all sample files and sort them
$testFiles = Get-ChildItem -Path $SamplesDir -Filter "*.in" | 
    Sort-Object { 
        if ($_.Name -match 'style-(\d+)-(\d+)') { 
            [int]$Matches[1] * 1000 + [int]$Matches[2]
        } else { 
            9999 
        }
    }

if ($testFiles.Count -eq 0) {
    Write-Error "No sample files found. Please run download_samples.py first."
    exit 1
}

Write-Host "Found $($testFiles.Count) sample files" -ForegroundColor Green

# Create output file
$outputFile = "sample_test_results.txt"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

"Art Classification Test Results - $timestamp" | Out-File -FilePath $outputFile
"======================================================" | Out-File -FilePath $outputFile -Append
"" | Out-File -FilePath $outputFile -Append

# Track results
$numpyCorrect = 0
$noNumpyCorrect = 0
$totalTests = $testFiles.Count

# Track timing
$numpyTimes = @()
$noNumpyTimes = @()

# Process each test file
foreach ($file in $testFiles) {
    $testName = $file.Name
    
    # Extract expected style from filename
    $expectedStyle = if ($testName -match 'style-(\d+)-') { [int]$Matches[1] } else { "unknown" }
    
    Write-Host "Testing $testName... " -ForegroundColor Cyan
    
    $resultLine = "$testName - Expected: Style $expectedStyle"
    
    # Test with NumPy implementation if requested
    if ($Implementation -eq "numpy" -or $Implementation -eq "both") {
        $numpyStart = Get-Date
        $numpyResult = (Get-Content $file.FullName | python .\classify.py).Trim()
        $numpyEnd = Get-Date
        $numpyTime = ($numpyEnd - $numpyStart).TotalSeconds
        $numpyTimes += $numpyTime
        
        if ($numpyResult -eq $expectedStyle) {
            Write-Host "  NumPy: ✓ Correct (Style $numpyResult) - ${numpyTime:F3}s" -ForegroundColor Green
            $numpyCorrect++
            $resultLine += ", NumPy: Style $numpyResult (${numpyTime:F3}s) ✓ CORRECT"
        } else {
            Write-Host "  NumPy: ✗ Incorrect (Expected $expectedStyle, got $numpyResult) - ${numpyTime:F3}s" -ForegroundColor Red
            $resultLine += ", NumPy: Style $numpyResult (${numpyTime:F3}s) ✗ INCORRECT"
        }
    }
    
    # Test with non-NumPy implementation if requested
    if ($Implementation -eq "no_numpy" -or $Implementation -eq "both") {
        $noNumpyStart = Get-Date
        $noNumpyResult = (Get-Content $file.FullName | python .\classify_no_numpy.py).Trim()
        $noNumpyEnd = Get-Date
        $noNumpyTime = ($noNumpyEnd - $noNumpyStart).TotalSeconds
        $noNumpyTimes += $noNumpyTime
        
        if ($noNumpyResult -eq $expectedStyle) {
            Write-Host "  No-NumPy: ✓ Correct (Style $noNumpyResult) - ${noNumpyTime:F3}s" -ForegroundColor Green
            $noNumpyCorrect++
            $resultLine += ", No-NumPy: Style $noNumpyResult (${noNumpyTime:F3}s) ✓ CORRECT"
        } else {
            Write-Host "  No-NumPy: ✗ Incorrect (Expected $expectedStyle, got $noNumpyResult) - ${noNumpyTime:F3}s" -ForegroundColor Red
            $resultLine += ", No-NumPy: Style $noNumpyResult (${noNumpyTime:F3}s) ✗ INCORRECT"
        }
    }
    
    $resultLine | Out-File -FilePath $outputFile -Append
}

# Calculate average execution times
$avgNumpyTime = if ($numpyTimes.Count -gt 0) { ($numpyTimes | Measure-Object -Average).Average } else { 0 }
$avgNoNumpyTime = if ($noNumpyTimes.Count -gt 0) { ($noNumpyTimes | Measure-Object -Average).Average } else { 0 }

# Calculate and add summary
"" | Out-File -FilePath $outputFile -Append
"Summary:" | Out-File -FilePath $outputFile -Append
"--------" | Out-File -FilePath $outputFile -Append
"Total tests: $totalTests" | Out-File -FilePath $outputFile -Append

if ($Implementation -eq "numpy" -or $Implementation -eq "both") {
    $numpyAccuracy = ($numpyCorrect / $totalTests) * 100
    "NumPy Correct classifications: $numpyCorrect ($($numpyAccuracy.ToString("F2"))%)" | Out-File -FilePath $outputFile -Append
    "NumPy Average execution time: $($avgNumpyTime.ToString("F3"))s" | Out-File -FilePath $outputFile -Append
}

if ($Implementation -eq "no_numpy" -or $Implementation -eq "both") {
    $noNumpyAccuracy = ($noNumpyCorrect / $totalTests) * 100
    "No-NumPy Correct classifications: $noNumpyCorrect ($($noNumpyAccuracy.ToString("F2"))%)" | Out-File -FilePath $outputFile -Append
    "No-NumPy Average execution time: $($avgNoNumpyTime.ToString("F3"))s" | Out-File -FilePath $outputFile -Append
}

# Display summary to console
Write-Host "`nTesting complete!" -ForegroundColor Cyan
Write-Host "Total tests: $totalTests" -ForegroundColor White

if ($Implementation -eq "numpy" -or $Implementation -eq "both") {
    $numpyAccuracy = ($numpyCorrect / $totalTests) * 100
    $colorNumpy = if ($numpyAccuracy -ge 90) { "Green" } elseif ($numpyAccuracy -ge 70) { "Yellow" } else { "Red" }
    Write-Host "NumPy correct: $numpyCorrect ($($numpyAccuracy.ToString("F2"))%)" -ForegroundColor $colorNumpy
    Write-Host "NumPy avg time: $($avgNumpyTime.ToString("F3"))s" -ForegroundColor Cyan
    
    # Calculate NumPy IOI score
    $numpyScore = if ($numpyAccuracy -lt 25) {
        0
    } elseif ($numpyAccuracy -lt 50) {
        [math]::Floor(10 * ($numpyAccuracy - 25) / 25)
    } elseif ($numpyAccuracy -lt 90) {
        10 + [math]::Floor(90 * ($numpyAccuracy - 50) / 40)
    } else {
        100
    }
    
    Write-Host "NumPy IOI score: $numpyScore / 100" -ForegroundColor $colorNumpy
}

if ($Implementation -eq "no_numpy" -or $Implementation -eq "both") {
    $noNumpyAccuracy = ($noNumpyCorrect / $totalTests) * 100
    $colorNoNumpy = if ($noNumpyAccuracy -ge 90) { "Green" } elseif ($noNumpyAccuracy -ge 70) { "Yellow" } else { "Red" }
    Write-Host "No-NumPy correct: $noNumpyCorrect ($($noNumpyAccuracy.ToString("F2"))%)" -ForegroundColor $colorNoNumpy
    Write-Host "No-NumPy avg time: $($avgNoNumpyTime.ToString("F3"))s" -ForegroundColor Cyan
    
    # Calculate No-NumPy IOI score
    $noNumpyScore = if ($noNumpyAccuracy -lt 25) {
        0
    } elseif ($noNumpyAccuracy -lt 50) {
        [math]::Floor(10 * ($noNumpyAccuracy - 25) / 25)
    } elseif ($noNumpyAccuracy -lt 90) {
        10 + [math]::Floor(90 * ($noNumpyAccuracy - 50) / 40)
    } else {
        100
    }
    
    Write-Host "No-NumPy IOI score: $noNumpyScore / 100" -ForegroundColor $colorNoNumpy
}

# Compare performance if both implementations were run
if ($Implementation -eq "both" -and $numpyTimes.Count -gt 0 -and $noNumpyTimes.Count -gt 0) {
    $speedup = $avgNoNumpyTime / $avgNumpyTime
    $performanceNote = if ($speedup > 1) {
        "NumPy is $($speedup.ToString("F2"))x faster than No-NumPy"
    } else {
        "No-NumPy is $((1/$speedup).ToString("F2"))x faster than NumPy"
    }
    
    Write-Host "`nPerformance comparison: $performanceNote" -ForegroundColor Magenta
    "Performance comparison: $performanceNote" | Out-File -FilePath $outputFile -Append
}

Write-Host "`nResults saved to $outputFile" -ForegroundColor Green
