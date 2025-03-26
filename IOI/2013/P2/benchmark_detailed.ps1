<#
.SYNOPSIS
    Detailed performance benchmarking for the art classification algorithms.
.DESCRIPTION
    This script performs multiple runs of both classifiers on sample images
    and provides detailed timing statistics to compare their performance.
.EXAMPLE
    .\benchmark_detailed.ps1
.PARAMETER Iterations
    Number of times to repeat each test for more accurate timing (default: 3)
.PARAMETER SamplesLimit
    Maximum number of sample files to test (default: 5)
#>

param(
    [Parameter(Mandatory=$false)]
    [int]$Iterations = 3,
    
    [Parameter(Mandatory=$false)]
    [int]$SamplesLimit = 5
)

# Check if samples directory exists
$SamplesDir = "./samples"
if (-not (Test-Path $SamplesDir)) {
    Write-Error "Samples directory not found. Please run download_samples.py first."
    exit 1
}

# Get sample files and limit the number if requested
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

# Limit number of samples if needed
if ($SamplesLimit -gt 0 -and $testFiles.Count -gt $SamplesLimit) {
    # Try to pick samples from different styles
    $selectedFiles = @()
    for ($style = 1; $style -le 4; $style++) {
        $styleFiles = $testFiles | Where-Object { $_.Name -match "style-$style-" }
        if ($styleFiles.Count -gt 0) {
            $selectedFiles += $styleFiles[0]
            if ($selectedFiles.Count -ge $SamplesLimit) {
                break
            }
        }
    }
    
    # If we still need more samples, add whatever is available
    while ($selectedFiles.Count -lt $SamplesLimit -and $selectedFiles.Count -lt $testFiles.Count) {
        $nextFile = $testFiles | Where-Object { $selectedFiles -notcontains $_ } | Select-Object -First 1
        if ($nextFile) {
            $selectedFiles += $nextFile
        } else {
            break
        }
    }
    
    $testFiles = $selectedFiles
}

Write-Host "Starting performance benchmark with $($testFiles.Count) samples, $Iterations iterations each" -ForegroundColor Green

# Track detailed timing results
$results = @()

foreach ($file in $testFiles) {
    $testName = $file.Name
    Write-Host "`nBenchmarking $testName..." -ForegroundColor Cyan
    
    $numpyTimes = @()
    $noNumpyTimes = @()
    $numpyResults = @()
    $noNumpyResults = @()
    
    # Run multiple iterations for more accurate timing
    for ($i = 0; $i -lt $Iterations; $i++) {
        Write-Host "  Iteration $($i+1)/$Iterations... " -NoNewline
        
        # Test NumPy implementation
        $numpyStart = Get-Date
        $numpyResult = (Get-Content $file.FullName | python .\classify.py).Trim()
        $numpyEnd = Get-Date
        $numpyTime = ($numpyEnd - $numpyStart).TotalSeconds
        $numpyTimes += $numpyTime
        $numpyResults += $numpyResult
        
        # Test non-NumPy implementation
        $noNumpyStart = Get-Date
        $noNumpyResult = (Get-Content $file.FullName | python .\classify_no_numpy.py).Trim()
        $noNumpyEnd = Get-Date
        $noNumpyTime = ($noNumpyEnd - $noNumpyStart).TotalSeconds
        $noNumpyTimes += $noNumpyTime
        $noNumpyResults += $noNumpyResult
        
        Write-Host "NumPy: ${numpyTime:F3}s, No-NumPy: ${noNumpyTime:F3}s" -ForegroundColor Yellow
    }
    
    # Calculate statistics
    $avgNumpyTime = ($numpyTimes | Measure-Object -Average).Average
    $avgNoNumpyTime = ($noNumpyTimes | Measure-Object -Average).Average
    $minNumpyTime = ($numpyTimes | Measure-Object -Minimum).Minimum
    $minNoNumpyTime = ($noNumpyTimes | Measure-Object -Minimum).Minimum
    $maxNumpyTime = ($numpyTimes | Measure-Object -Maximum).Maximum
    $maxNoNumpyTime = ($noNumpyTimes | Measure-Object -Maximum).Maximum
    
    # Output results for this file
    $speedup = $avgNoNumpyTime / $avgNumpyTime
    $speedupDesc = if ($speedup > 1) {
        "NumPy ${speedup:F2}x faster"
    } else {
        "No-NumPy $((1/$speedup):F2)x faster"
    }
    
    Write-Host "  Results:" -ForegroundColor Cyan
    Write-Host "    NumPy:    Min=${minNumpyTime:F3}s, Avg=${avgNumpyTime:F3}s, Max=${maxNumpyTime:F3}s" -ForegroundColor Yellow
    Write-Host "    No-NumPy: Min=${minNoNumpyTime:F3}s, Avg=${avgNoNumpyTime:F3}s, Max=${maxNoNumpyTime:F3}s" -ForegroundColor Yellow
    Write-Host "    Comparison: $speedupDesc" -ForegroundColor Magenta
    
    # Check for result consistency
    $numpyConsistent = ($numpyResults | Select-Object -Unique).Count -eq 1
    $noNumpyConsistent = ($noNumpyResults | Select-Object -Unique).Count -eq 1
    $consistencyMsg = if ($numpyConsistent -and $noNumpyConsistent) {
        "Both implementations produced consistent results"
    } elseif (-not $numpyConsistent -and -not $noNumpyConsistent) {
        "Both implementations produced inconsistent results!"
    } elseif (-not $numpyConsistent) {
        "NumPy implementation produced inconsistent results!"
    } else {
        "No-NumPy implementation produced inconsistent results!"
    }
    
    $consistencyColor = if ($numpyConsistent -and $noNumpyConsistent) { "Green" } else { "Red" }
    Write-Host "    Consistency: $consistencyMsg" -ForegroundColor $consistencyColor
    
    # Add to results collection
    $resultObj = [PSCustomObject]@{
        TestFile = $testName
        NumPy_AvgTime = $avgNumpyTime
        NumPy_MinTime = $minNumpyTime
        NumPy_MaxTime = $maxNumpyTime
        NumPy_Result = ($numpyResults | Select-Object -First 1)
        NumPy_Consistent = $numpyConsistent
        NoNumPy_AvgTime = $avgNoNumpyTime
        NoNumPy_MinTime = $minNoNumpyTime
        NoNumPy_MaxTime = $maxNoNumpyTime
        NoNumPy_Result = ($noNumpyResults | Select-Object -First 1)
        NoNumPy_Consistent = $noNumpyConsistent
        Speedup = $speedup
        SpeedupDesc = $speedupDesc
    }
    $results += $resultObj
}

# Calculate overall averages
$overallNumpyAvg = ($results | Measure-Object -Property NumPy_AvgTime -Average).Average
$overallNoNumpyAvg = ($results | Measure-Object -Property NoNumPy_AvgTime -Average).Average
$overallSpeedup = $overallNoNumpyAvg / $overallNumpyAvg

# Output summary
Write-Host "`n======================" -ForegroundColor Magenta
Write-Host "Benchmark Summary" -ForegroundColor Magenta
Write-Host "======================" -ForegroundColor Magenta
Write-Host "Files tested: $($results.Count)"
Write-Host "Iterations per file: $Iterations"
Write-Host "Overall NumPy average time: ${overallNumpyAvg:F3}s"
Write-Host "Overall No-NumPy average time: ${overallNoNumpyAvg:F3}s"

if ($overallSpeedup > 1) {
    Write-Host "NumPy is ${overallSpeedup:F2}x faster than No-NumPy implementation" -ForegroundColor Green
} else {
    Write-Host "No-NumPy is $((1/$overallSpeedup):F2)x faster than NumPy implementation" -ForegroundColor Green
}

# Export detailed results to CSV
$csvPath = "benchmark_results.csv"
$results | Export-Csv -Path $csvPath -NoTypeInformation
Write-Host "`nDetailed benchmark results saved to $csvPath" -ForegroundColor Green
