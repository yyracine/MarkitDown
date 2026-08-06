================================================================================
  MarkItDown GUI - Installation & Usage Guide
================================================================================

WELCOME!
--------
Thank you for installing MarkItDown GUI - A powerful tool to convert 20+ file
formats to Markdown using Microsoft's MarkItDown library.

QUICK START
-----------
1. Double-click "MarkItDown.bat" to launch the application
2. Click "Browse" to select a file to convert
3. View the Markdown preview in real-time
4. Save to file or copy to clipboard

SUPPORTED FORMATS (20+)
-----------------------
Documents:    PDF, DOCX, XLSX, PPTX, EPub, Jupyter Notebooks, Outlook Messages
Web Content:  HTML, CSS, RSS Feeds, Wikipedia, YouTube (with transcription)
Media:        JPG, PNG, GIF, WEBP, BMP, TIFF (with EXIF), MP3, WAV
Data:         CSV, JSON, XML, ZIP
Other:        Plain Text, Markdown, Binary Detection

INSTALLATION REQUIREMENTS
--------------------------
- Windows 7, 8, 10, or 11 (64-bit)
- 512 MB RAM minimum (2+ GB recommended)
- 200 MB free disk space
- No administrator required

FEATURES
--------
✓ Async conversion (non-blocking interface)
✓ Real-time Markdown preview
✓ Progress bar for long conversions
✓ Copy to clipboard or save to file
✓ Support for 20+ file formats
✓ Error handling and validation
✓ UTF-8 character support

TROUBLESHOOTING
---------------

Q: Application won't start
A: Make sure Python 3.10+ is installed. Try running from PowerShell:
   .\.venv\Scripts\python markitdown_gui.py

Q: Conversion is slow
A: First conversion takes 3-10 seconds. Subsequent conversions are faster (2-8s).

Q: File format not supported
A: Check the supported formats above. Some formats need optional packages.

Q: Python error or missing module
A: Reinstall dependencies:
   .\.venv\Scripts\pip install PyQt6
   .\.venv\Scripts\pip install -e 'markitdown[all]'

ADVANCED USAGE
--------------
To run from PowerShell:
  .\.venv\Scripts\Activate.ps1
  python markitdown_gui.py

To check installed packages:
  .\.venv\Scripts\pip list

PORTABLE INSTALLATION
---------------------
This installation is fully portable:
- No system registry changes
- Can be moved to USB drive
- Can be copied to any location
- Works from any folder

Simply move this entire folder to your desired location and double-click
MarkItDown.bat

CREATING A DESKTOP SHORTCUT (Windows)
--------------------------------------
1. Right-click MarkItDown.bat
2. Create shortcut
3. Move shortcut to Desktop
4. Right-click shortcut → Properties → Advanced → "Run as administrator" (optional)

LICENSE
-------
This project uses MIT License - feel free to use and modify

GITHUB REPOSITORY
-----------------
https://github.com/yyracine/MarkitDown

SUPPORT
-------
For issues or questions, visit the GitHub repository

================================================================================
Version: 1.0
Last Updated: 2026-08-06
================================================================================
