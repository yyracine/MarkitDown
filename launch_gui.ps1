# Script de lancement de MarkItDown GUI pour PowerShell
# Usage: .\launch_gui.ps1

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

Write-Host "[*] Lancement de MarkItDown GUI..." -ForegroundColor Green

# Chercher Python
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonPath) {
    Write-Host "[OK] Python trouvé: $($pythonPath.Source)" -ForegroundColor Green
    & python markitdown_gui.py
    exit 0
}

# Chercher dans venv
if (Test-Path ".venv\Scripts\python.exe") {
    Write-Host "[OK] Environnement virtuel trouve" -ForegroundColor Green
    & .\.venv\Scripts\python markitdown_gui.py
    exit 0
}

Write-Host "[ERROR] Erreur: Python n'a pas pu etre trouve!" -ForegroundColor Red
Write-Host "Veuillez s'il vous plaît:" -ForegroundColor Yellow
Write-Host "1. Installer Python (python.org)" -ForegroundColor Yellow
Write-Host "2. Ou créer un environnement virtuel: python -m venv .venv" -ForegroundColor Yellow
Write-Host "3. Ou installer PyQt6: pip install PyQt6" -ForegroundColor Yellow

Read-Host "Appuyez sur Entrée pour quitter"
exit 1
