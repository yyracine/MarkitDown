@echo off
REM MarkItDown GUI Launcher
REM This script launches the MarkItDown GUI application

cd /d "%~dp0"

REM Activate virtual environment and run the GUI
call .venv\Scripts\activate.bat
python markitdown_gui.py
