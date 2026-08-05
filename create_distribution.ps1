# Create distribution ZIP archive

Write-Host "Creating distribution archive..." -ForegroundColor Cyan

# Paths
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $scriptPath

# Clean and create distribution folder
$distFolder = Join-Path $scriptPath "distribution"
if (Test-Path $distFolder) {
    Remove-Item -Recurse -Force -Path $distFolder -ErrorAction SilentlyContinue
}
New-Item -ItemType Directory -Path $distFolder -Force | Out-Null

# Copy files
Write-Host "Copying files..." -ForegroundColor Yellow
Copy-Item -Recurse "dist\MarkItDown" "$distFolder\"
Copy-Item "dist\MarkItDown.bat" "$distFolder\"
Copy-Item "EXECUTABLE_README.md" "$distFolder\README.md"

Write-Host "[OK] Distribution folder created" -ForegroundColor Green

# Create ZIP
Write-Host "Creating ZIP archive..." -ForegroundColor Yellow
$zipPath = Join-Path $scriptPath "MarkItDown-GUI-Executable.zip"

if (Test-Path $zipPath) {
    Remove-Item $zipPath
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory(
    $distFolder,
    $zipPath,
    [System.IO.Compression.CompressionLevel]::Optimal,
    $false
)

Write-Host "[OK] Archive created!" -ForegroundColor Green

# Display statistics
$zipSize = (Get-Item $zipPath).Length / 1MB
Write-Host ""
Write-Host "=== Distribution Archive ===" -ForegroundColor Cyan
Write-Host "Name: MarkItDown-GUI-Executable.zip"
Write-Host "Size: $([math]::Round($zipSize, 2)) MB"
Write-Host "Path: $zipPath"
Write-Host ""
Write-Host "Archive contains:" -ForegroundColor Green
Write-Host "  [+] MarkItDown/          (Application directory)"
Write-Host "      - MarkItDown.exe    (6.7 MB executable)"
Write-Host "      - _internal/        (All dependencies)"
Write-Host "  [+] MarkItDown.bat       (Quick launcher)"
Write-Host "  [+] README.md            (Instructions)"
Write-Host ""
Write-Host "Distribution ready for download!" -ForegroundColor Cyan

Pop-Location
