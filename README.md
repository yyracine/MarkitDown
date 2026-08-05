# MarkItDown GUI

> A beautiful, user-friendly graphical interface for [MarkItDown](https://github.com/microsoft/markitdown) — convert any file format to Markdown for LLMs and text analysis.

[![GitHub](https://img.shields.io/badge/GitHub-yyracine%2FMarkitDown-blue)](https://github.com/yyracine/MarkitDown)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Overview

**MarkItDown GUI** makes file conversion to Markdown effortless with an intuitive desktop application. No command-line knowledge required — just select a file, click convert, and save your Markdown.

Perfect for:
- 📄 Converting documents (PDF, Word, Excel, PowerPoint)
- 🖼️ Extracting text from images
- 🎬 Getting YouTube transcriptions
- 📰 Processing web content (HTML, RSS, Wikipedia)
- 🔄 Building document processing pipelines for LLMs

## ✨ Key Features

### 🎨 Intuitive Interface
- **File Selection** - Easy file picker with support for all formats
- **Real-time Preview** - See your Markdown as it converts
- **Visual Feedback** - Progress bar and status messages
- **One-Click Export** - Save to file or copy to clipboard

### 📦 Format Support
- **Documents**: PDF, Word (.docx), Excel (.xlsx, .xls), PowerPoint (.pptx), EPub
- **Web**: HTML, RSS, Wikipedia, YouTube, Bing Search
- **Media**: Images (JPG, PNG, GIF, WEBP), Audio (transcription)
- **Data**: CSV, JSON, XML, ZIP (iterate contents)
- **Other**: Jupyter Notebooks, Outlook Messages, Plain text

### ⚙️ Advanced Options
- **Plugins** - Enable third-party plugin support (markitdown-ocr, etc.)
- **Azure Document Intelligence** - High-quality OCR for scanned documents
- **Azure Content Understanding** - Structured field extraction with YAML frontmatter

### 🚀 Performance
- **Non-blocking UI** - Async conversion thread never freezes the interface
- **Fast Processing** - Typically 2-10 seconds per file
- **Efficient** - Markdown is token-efficient for LLM input

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yyracine/MarkitDown.git
cd MarkitDown
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install PyQt6
pip install -e 'markitdown/packages/markitdown[all]'
```

4. **Verify installation**
```bash
python check_requirements.py
```

### Launch the Application

**Windows (easiest):**
```bash
launch_gui.bat
```

**PowerShell:**
```powershell
.\.venv\Scripts\python .\markitdown_gui.py
```

**macOS/Linux:**
```bash
source .venv/bin/activate
python markitdown_gui.py
```

## 📖 Usage Guide

### Basic Workflow

1. **Select a File**
   - Click "📁 Select File"
   - Choose any supported format

2. **Configure (Optional)**
   - Go to "⚙️ Options" tab
   - Enable plugins or Azure services if needed

3. **Convert**
   - Click "🔄 Convert"
   - Wait for completion (usually 2-10 seconds)

4. **Save or Copy**
   - Click "💾 Save Markdown" to save as .md file
   - Or "📋 Copy Text" to copy to clipboard

### Examples

**Convert a PDF to Markdown:**
```
1. Select: report.pdf
2. Convert
3. Save: report.md
```

**Extract text from an image:**
```
1. Select: screenshot.jpg
2. Convert
3. Copy to clipboard
```

**Get YouTube transcription:**
```
1. Select: https://youtube.com/watch?v=...
2. Convert (wait ~10 seconds)
3. Save: transcription.md
```

**Process Excel data:**
```
1. Select: data.xlsx
2. Convert
3. Result: Markdown table with data
4. Save: data.md
```

## 📚 Documentation

Complete documentation is available:

| Document | Purpose | Read Time |
|----------|---------|-----------|
| [QUICKSTART.txt](QUICKSTART.txt) | Get started in 5 minutes | 5 min |
| [README_GUI.md](README_GUI.md) | Complete usage guide | 15 min |
| [GUIDE_GUI.md](GUIDE_GUI.md) | Advanced configuration | 20 min |
| [INDEX.md](INDEX.md) | Navigation and file structure | 10 min |
| [INSTALLATION_COMPLETE.md](INSTALLATION_COMPLETE.md) | Installation summary | 10 min |

**New to the project?** Start with [QUICKSTART.txt](QUICKSTART.txt)

## 🏗️ Project Structure

```
MarkitDown/
├── markitdown_gui.py                    # Main application (880 lines)
├── launch_gui.bat                       # Windows launcher
├── launch_gui.ps1                       # PowerShell launcher
├── check_requirements.py                # Dependency checker
│
├── 📚 Documentation
│   ├── README.md                        # This file
│   ├── QUICKSTART.txt                   # 5-minute guide
│   ├── README_GUI.md                    # Complete guide
│   ├── GUIDE_GUI.md                     # Advanced guide
│   ├── INDEX.md                         # Navigation
│   ├── INSTALLATION_COMPLETE.md         # Installation summary
│   └── RESUME_CREATION.txt              # Project summary
│
├── markitdown/                          # Original MarkItDown (Microsoft)
│   └── packages/markitdown/
│       ├── src/markitdown/              # Core library
│       └── tests/                       # Test suite
│
└── .venv/                               # Python virtual environment
```

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **GUI** | PyQt6 | Cross-platform interface |
| **Conversion** | MarkItDown | File format conversion |
| **Threading** | QThread | Async file processing |
| **Dependencies** | 25+ packages | Format-specific converters |

### Key Dependencies

- **beautifulsoup4** - HTML parsing
- **requests** - HTTP requests
- **pdfminer.six** - PDF extraction
- **python-pptx** - PowerPoint processing
- **pandas** - Excel handling
- **mammoth** - Word document processing
- And more for optimal format support

## ⚙️ Configuration

### Windows Batch
Simply double-click `launch_gui.bat` — it auto-detects Python.

### Environment Variables
```powershell
# Enable specific converters
QT_QPA_PLATFORM=offscreen  # Headless mode
PYTHONIOENCODING=utf-8     # UTF-8 output
```

### Advanced: Azure Integration

**Document Intelligence (OCR):**
1. Create Azure resource
2. Copy endpoint URL
3. Go to Options → "Azure Document Intelligence"
4. Paste endpoint → Convert

**Content Understanding (Structured extraction):**
1. Create Azure Content Understanding resource
2. Configure in Options
3. Set analyzer ID (optional)
4. Convert

## 🔒 Security Considerations

⚠️ **Important**: MarkItDown accesses files with your process's permissions.

### Best Practices
- ✅ Only convert files from trusted sources
- ✅ Validate file paths before conversion
- ✅ Be cautious with ZIP files (can contain code)
- ✅ Be cautious with Office files (can contain macros)

For more details, see [Microsoft's security guidelines](https://github.com/microsoft/markitdown#security-considerations).

## 🐛 Troubleshooting

### "Application won't start"
```bash
# Check dependencies
python check_requirements.py

# If missing dependencies:
pip install PyQt6
pip install -e 'markitdown/packages/markitdown[all]'
```

### "Format not supported"
Install optional dependencies:
```bash
pip install python-pptx pdfplumber mammoth pandas openpyxl xlrd
```

### "Conversion is slow"
- First file is slower (library loading) — subsequent files are faster
- Large files naturally take longer
- This is expected behavior

### "Can't use Azure services"
- You need an Azure subscription and configured resource
- Without Azure, use built-in converters (perfectly fine!)

**More help?** Check [README_GUI.md](README_GUI.md#troubleshooting) for detailed troubleshooting.

## 📊 Performance Benchmarks

Typical conversion times on modern hardware:

| File Type | Size | Time |
|-----------|------|------|
| Plain text | < 1 MB | < 1 sec |
| PDF (simple) | 5-10 pages | 2-5 sec |
| PDF (complex) | 50+ pages | 15-30 sec |
| Image | 5 MB | 2-5 sec |
| Excel | 1000 rows | 3-8 sec |
| PowerPoint | 20 slides | 3-8 sec |
| HTML | 100 KB | 1-2 sec |

*Times vary based on hardware and optional dependencies installed*

## 🚀 Advanced Usage

### Batch Processing
Currently manual, but planned for future release. For now:
1. Convert files one at a time
2. Or use MarkItDown CLI for batch operations

### Integration with Scripts
```python
from pathlib import Path
import sys

sys.path.insert(0, 'markitdown/packages/markitdown/src')
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert_local('document.pdf')
print(result.markdown)
```

### Using with LLMs
```python
import openai

# Convert document to Markdown
md = MarkItDown()
result = md.convert_local('document.pdf')

# Send to LLM
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": f"Summarize:\n{result.markdown}"}
    ]
)
```

## 🤝 Contributing

This project wraps the excellent [MarkItDown](https://github.com/microsoft/markitdown) library from Microsoft.

### Contributing Guidelines
- Report bugs via GitHub Issues
- Submit pull requests for improvements
- Add tests for new features
- Update documentation

### Contribution Areas
- [ ] Batch file conversion
- [ ] Dark theme support
- [ ] Drag & drop file upload
- [ ] Recent files history
- [ ] Custom export formats
- [ ] Plugin marketplace UI

## 📜 License

This project is licensed under the **MIT License** - same as MarkItDown.

See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **MarkItDown** - Original library by [Microsoft AutoGen Team](https://github.com/microsoft/markitdown)
- **PyQt6** - Cross-platform GUI framework
- **All Contributors** - Making file conversion effortless

## 📞 Support & Contact

### Questions?
- Read the documentation: [QUICKSTART.txt](QUICKSTART.txt)
- Check [FAQ section](README_GUI.md#faq) in README_GUI.md
- Review [Troubleshooting](README_GUI.md#troubleshooting)

### Found a bug?
1. Run `check_requirements.py` to verify setup
2. Try reproducing with a simple file
3. Open an issue with:
   - Steps to reproduce
   - File type used
   - Error message
   - Python/OS version

### Want to contribute?
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🗺️ Roadmap

### v1.1 (Next)
- [ ] Batch conversion interface
- [ ] Recent files menu
- [ ] Custom keyboard shortcuts
- [ ] Theme selection (light/dark)

### v1.2
- [ ] Search & replace in Markdown
- [ ] Export to HTML/PDF
- [ ] Plugin marketplace UI
- [ ] Configuration profiles

### v2.0 (Future)
- [ ] Multi-document workspace
- [ ] Real-time collaboration
- [ ] Cloud storage integration
- [ ] Mobile companion app

## 📈 Statistics

- **Code**: 880 lines (PyQt6 application)
- **Documentation**: 1400+ lines
- **Formats Supported**: 20+
- **Dependencies**: 25+ packages
- **Installation Size**: ~500 MB (with all converters)
- **Python**: 3.10+

## 🎓 Learning Resources

### Getting Started
- [Python GUI with PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [MarkItDown Documentation](https://github.com/microsoft/markitdown)
- [Qt Documentation](https://doc.qt.io/qt-6/)

### Advanced Topics
- Async threading in PyQt6
- Custom converters
- Azure integrations
- LLM integration patterns

## 💡 Tips & Tricks

### Tip 1: Keyboard Shortcuts
Standard shortcuts work:
- `Ctrl+C` - Copy selected text
- `Ctrl+A` - Select all in editor

### Tip 2: File Format Priority
MarkItDown automatically detects format. For ambiguous files, rename with correct extension.

### Tip 3: Large PDFs
For very large PDFs (100+ pages):
1. Consider splitting the file
2. Or use Azure Document Intelligence for better performance

### Tip 4: Regular Expressions
Markdown output can be cleaned with regex in text editor:
- Remove extra whitespace
- Normalize heading levels
- Fix formatting issues

## 📝 Changelog

### v1.0 (Initial Release)
- ✨ PyQt6-based GUI application
- 📦 Support for 20+ file formats
- ⚙️ Advanced options (plugins, Azure)
- 📚 Comprehensive documentation
- 🧪 Full testing and verification

See [COMMITS](../../commits/main) for full history.

---

<div align="center">

### ⭐ If you find this useful, please star the repository!

[GitHub Repository](https://github.com/yyracine/MarkitDown) • [MarkItDown Original](https://github.com/microsoft/markitdown) • [Report Issue](https://github.com/yyracine/MarkitDown/issues)

**Made with ❤️ for seamless file conversion**

</div>
