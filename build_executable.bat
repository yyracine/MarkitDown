@echo off
REM Script de construction de l'executable MarkItDown GUI avec PyInstaller

echo.
echo ========================================
echo   Building MarkItDown GUI Executable
echo ========================================
echo.

REM Verify PyInstaller is installed
.\.venv\Scripts\python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] PyInstaller not installed
    echo Installing PyInstaller...
    .\.venv\Scripts\pip install pyinstaller -q
)

echo [1/4] Cleaning previous builds...
if exist build\ (
    rmdir /s /q build
    echo [OK] Cleaned build directory
)
if exist dist\ (
    rmdir /s /q dist
    echo [OK] Cleaned dist directory
)

echo.
echo [2/4] Building executable...
.\.venv\Scripts\pyinstaller -y build_exe.spec

echo.
echo [3/4] Verifying build...
if exist "dist\MarkItDown\MarkItDown.exe" (
    echo [OK] Executable created successfully
    echo [OK] Location: dist\MarkItDown\MarkItDown.exe
) else (
    echo [ERROR] Build failed - executable not found
    exit /b 1
)

echo.
echo [4/4] Creating launcher batch file...
(
    echo @echo off
    echo cd /d "%%~dp0"
    echo MarkItDown\MarkItDown.exe
) > "dist\MarkItDown.bat"
echo [OK] Launcher created: dist\MarkItDown.bat

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo.
echo Executable created at: dist\MarkItDown\MarkItDown.exe
echo Launcher created at: dist\MarkItDown.bat
echo.
echo To run the application:
echo   Option 1: Double-click dist\MarkItDown.bat
echo   Option 2: Run dist\MarkItDown\MarkItDown.exe
echo.
echo File size:
for /F "usebackq" %%A in (`dir /b dist\MarkItDown\MarkItDown.exe`) do (
    for /F "tokens=5" %%B in ('dir dist\MarkItDown\MarkItDown.exe') do (
        set size=%%B
    )
)
if defined size (
    echo Size: %size% bytes (approximately %size:~0,-6% MB)
)

echo.
echo ========================================
pause
