<#
.SYNOPSIS
    Script to run the art classification program with test files.
.DESCRIPTION
    This script demonstrates different methods to pipe file contents to the Python program.
.EXAMPLE
    .\run_test.ps1 -file "samples\style-1-0.in"
#>
param(
    [Parameter(Mandatory=$true)]
    [string]$file
)

Write-Host "Running test with file: $file" -ForegroundColor Green

# Method 1: Get-Content and pipe
Write-Host "`nMethod 1: Using Get-Content and pipe" -ForegroundColor Yellow
Get-Content $file | python classify.py

# Method 2: Using the PowerShell redirection operator
Write-Host "`nMethod 2: Using redirection operator" -ForegroundColor Yellow
python classify.py < $file

# Method 3: Using the -c flag with python to read from stdin
Write-Host "`nMethod 3: Using python -c to read from stdin" -ForegroundColor Yellow
Get-Content $file | python -c "import sys; exec(open('classify.py').read())"

Write-Host "`nTest completed!" -ForegroundColor Green
