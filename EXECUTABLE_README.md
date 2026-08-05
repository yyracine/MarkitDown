# MarkItDown GUI - Executable Distribution

> Standalone executable for MarkItDown GUI - No Python installation required!

## 📦 What's Included

This folder contains a complete, ready-to-run installation of MarkItDown GUI:

```
dist/
├── MarkItDown.bat              # Quick launcher (Windows)
└── MarkItDown/                 # Application directory
    ├── MarkItDown.exe          # Main executable (6.7 MB)
    ├── base_library.zip        # Python libraries
    ├── _internal/              # All dependencies
    │   ├── PyQt6/              # GUI framework
    │   ├── markitdown/         # Conversion library
    │   ├── PIL/                # Image processing
    │   └── ... (other deps)
    └── [other runtime files]
```

**Total Size:** 172.83 MB (includes all dependencies)

## 🚀 Quick Start

### Option 1: Double-Click Launcher (Easiest!)

```
dist\MarkItDown.bat
```

Simply double-click and the application opens!

### Option 2: Direct Executable

```
dist\MarkItDown\MarkItDown.exe
```

Or run directly from the explorer.

### Option 3: Command Line

**Windows CMD:**
```cmd
cd dist
MarkItDown.bat
```

**Windows PowerShell:**
```powershell
.\dist\MarkItDown\MarkItDown.exe
```

## 📋 System Requirements

- **OS:** Windows 7 or later (64-bit)
- **RAM:** 512 MB minimum (2 GB recommended)
- **Disk:** 200 MB free space
- **Screen:** 1024x600 minimum resolution

**No additional software needed!**
- ✅ Python NOT required
- ✅ Visual C++ NOT required
- ✅ Administrator NOT required

## ⚠️ First Run

**First launch may take a few seconds** (5-15 seconds) as the application initializes. Subsequent launches are faster.

If Windows shows a security warning:
1. Click "More info"
2. Click "Run anyway"
3. This is normal for unsigned executables

## 📖 Usage

Once the application opens:

1. **Click "📁 Select File"**
   - Choose any document, image, or web URL
   
2. **Click "🔄 Convert"**
   - Wait for conversion to complete
   
3. **Save or Copy**
   - Click "💾 Save Markdown" to save as .md file
   - Click "📋 Copy Text" to copy to clipboard

See [README_GUI.md](../README_GUI.md) for detailed usage guide.

## 🎯 Supported Formats

Works with 20+ file formats:

- **Documents**: PDF, Word, Excel, PowerPoint, EPub
- **Web**: HTML, RSS, Wikipedia, YouTube
- **Media**: Images, Audio
- **Data**: CSV, JSON, XML, ZIP
- **Other**: Jupyter Notebooks, Outlook Messages

## ⚙️ Features

✅ Intuitive graphical interface  
✅ Real-time Markdown preview  
✅ Support for 20+ file formats  
✅ Save to file or copy to clipboard  
✅ Progress indicator and error messages  
✅ Advanced options (plugins, Azure services)  
✅ Fast and efficient conversion  

## 🔧 Troubleshooting

### Application won't start

**Windows Security Warning:**
- Click "More info" → "Run anyway"
- This is normal for unsigned executables

**Application crashes immediately:**
- Try running from Command Prompt to see error messages
- Ensure you have 512 MB free RAM
- Update your graphics drivers

### Conversion fails

**"Format not supported"**
- Not all file formats are included in the basic executable
- For limited formats, use the Python version with full dependencies

**"File not found"**
- Ensure the file path doesn't contain special characters
- Try with a file in the same folder as the executable

**"Out of memory"**
- Close other applications
- Try with a smaller file
- Restart the application

### Slow performance

**First run is slow** (loading libraries) - This is normal!

**Subsequent runs are slow:**
- Large files take time to process
- Some formats are inherently slower
- This is expected behavior

## 📝 Advanced Options

The executable includes support for:

### Plugins
Enable third-party plugins in Options tab (if installed)

### Azure Document Intelligence
For high-quality OCR of scanned documents:
1. Create Azure resource
2. Get endpoint URL
3. Enter in Options → "Azure Document Intelligence"

### Azure Content Understanding
For structured field extraction:
1. Create Content Understanding resource
2. Configure in Options
3. Convert documents with structured output

## 🔄 Updating

To get the latest version:

1. Download the latest executable from [GitHub Releases](https://github.com/yyracine/MarkitDown/releases)
2. Extract to new location (can coexist with old version)
3. Old version can be safely deleted

## 🗑️ Uninstalling

Simply delete the `dist` folder. No registry entries or system files are modified.

**That's it!** No uninstaller needed.

## 📊 File Size Comparison

| Component | Size |
|-----------|------|
| Executable (MarkItDown.exe) | 6.7 MB |
| Dependencies (_internal) | 166 MB |
| **Total** | **172.83 MB** |

The large size is due to:
- PyQt6 GUI framework (90+ MB)
- PDF processing libraries (20+ MB)
- All format converters (30+ MB)
- Python runtime and dependencies (30+ MB)

## ⚡ Performance Tips

1. **First conversion is slower** - Libraries are loaded from disk
2. **Keep files reasonably sized** - 50+ page PDFs take longer
3. **Close other apps** - Frees up RAM for conversion
4. **Use SSD if possible** - Faster file I/O
5. **Recent conversions are cached** - Same file type is faster

## 🔐 Security & Privacy

✅ **Local processing only** - No data sent to internet (unless using Azure)  
✅ **No tracking** - No analytics or telemetry  
✅ **No registry changes** - Portable executable  
✅ **No installation** - Just unzip and run  

**Your files remain on your computer!**

## 📞 Support

### Having issues?

1. Check [Troubleshooting](#troubleshooting) section above
2. Read [README_GUI.md](../README_GUI.md) for detailed documentation
3. Check [QUICKSTART.txt](../QUICKSTART.txt) for quick reference
4. Open an issue on [GitHub](https://github.com/yyracine/MarkitDown/issues)

### Want more features?

Check [ROADMAP](../README.md#-roadmap) in the main README

## 📜 License

MIT License - Free for personal and commercial use

## 🙏 Credits

- **MarkItDown**: [Microsoft AutoGen Team](https://github.com/microsoft/markitdown)
- **PyInstaller**: [PyInstaller Project](https://www.pyinstaller.org/)
- **PyQt6**: [Riverbank Computing](https://www.riverbankcomputing.com/software/pyqt/)

## 🔗 Resources

- **Main GitHub**: https://github.com/yyracine/MarkitDown
- **MarkItDown Original**: https://github.com/microsoft/markitdown
- **PyQt6 Docs**: https://www.riverbankcomputing.com/static/Docs/PyQt6/
- **PyInstaller Guide**: https://pyinstaller.org/en/stable/

---

<div align="center">

### Ready to convert? Just run MarkItDown.bat! 🚀

For questions or feedback, visit the [GitHub repository](https://github.com/yyracine/MarkitDown)

</div>
