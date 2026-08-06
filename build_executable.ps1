# PowerShell script to build MarkItDown GUI executable

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Building MarkItDown GUI Executable" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if PyInstaller is installed
$pyinstaller = & .\.venv\Scripts\python -m pip show pyinstaller 2>$null
if (-not $pyinstaller) {
    Write-Host "[WARNING] PyInstaller not found, installing..." -ForegroundColor Yellow
    & .\.venv\Scripts\pip install pyinstaller -q
}

# Step 1: Clean previous builds
Write-Host "[1/4] Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build" -ErrorAction SilentlyContinue
    Write-Host "[OK] Cleaned build directory" -ForegroundColor Green
}
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist" -ErrorAction SilentlyContinue
    Write-Host "[OK] Cleaned dist directory" -ForegroundColor Green
}

# Step 2: Build executable
Write-Host ""
Write-Host "[2/4] Building executable..." -ForegroundColor Yellow

& .\.venv\Scripts\pyinstaller build_exe.spec

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Build failed!" -ForegroundColor Red
    exit 1
}

# Step 3: Verify build
Write-Host ""
Write-Host "[3/4] Verifying build..." -ForegroundColor Yellow
if (Test-Path "dist\MarkItDown\MarkItDown.exe") {
    Write-Host "[OK] Executable created successfully" -ForegroundColor Green
    $size = (Get-Item "dist\MarkItDown\MarkItDown.exe").Length / 1MB
    Write-Host "[OK] Location: dist\MarkItDown\MarkItDown.exe ($([math]::Round($size, 2)) MB)" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Build failed - executable not found" -ForegroundColor Red
    exit 1
}

# Step 4: Create launcher
Write-Host ""
Write-Host "[4/4] Creating launcher batch file..." -ForegroundColor Yellow
@"
@echo off
cd /d "%~dp0"
MarkItDown\MarkItDown.exe
"@ | Out-File -Encoding ASCII "dist\MarkItDown.bat" -Force
Write-Host "[OK] Launcher created: dist\MarkItDown.bat" -ForegroundColor Green

# Summary
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Build Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Executable created at:" -ForegroundColor Green
Write-Host "  dist\MarkItDown\MarkItDown.exe"
Write-Host ""
Write-Host "Launcher created at:" -ForegroundColor Green
Write-Host "  dist\MarkItDown.bat"
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Cyan
Write-Host "  Option 1: Double-click dist\MarkItDown.bat"
Write-Host "  Option 2: Run dist\MarkItDown\MarkItDown.exe"
Write-Host ""

# Check total size
$totalSize = 0
Get-ChildItem -Path "dist\MarkItDown" -Recurse | ForEach-Object {
    $totalSize += $_.Length
}
$totalMB = [math]::Round($totalSize / 1MB, 2)
Write-Host "Total size: $totalMB MB" -ForegroundColor Cyan
Write-Host ""
