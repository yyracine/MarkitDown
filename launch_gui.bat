@echo off
REM Script de lancement de MarkItDown GUI pour Windows
REM Lancer la GUI MarkItDown en restant dans le répertoire courant

cd /d "%~dp0"

REM Vérifier si Python est disponible
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Lancement de MarkItDown GUI...
    python markitdown_gui.py
    goto :end
)

REM Essayer avec l'environnement virtuel
if exist ".venv\Scripts\python.exe" (
    echo Lancement de MarkItDown GUI avec venv...
    .venv\Scripts\python markitdown_gui.py
    goto :end
)

echo Erreur: Python n'a pas pu être trouvé!
echo Veuillez installer Python ou activer l'environnement virtuel
pause
exit /b 1

:end
echo Application fermée
