# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for MarkItDown GUI
Creates a standalone executable for Windows
"""

block_cipher = None

a = Analysis(
    ['markitdown_gui.py'],
    pathex=[],
    binaries=[
        # Include onnxruntime binaries for magika
        ('.venv/Lib/site-packages/onnxruntime', 'onnxruntime'),
    ],
    datas=[
        # Include markitdown source
        ('markitdown/packages/markitdown/src', 'markitdown/packages/markitdown/src'),
        # Include data files from markitdown
        ('markitdown/packages/markitdown', 'markitdown/packages/markitdown'),
        # Include full magika package
        ('.venv/Lib/site-packages/magika', 'magika'),
    ],
    hiddenimports=[
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'markitdown',
        'markitdown.converters',
        'bs4',
        'requests',
        'markdownify',
        'charset_normalizer',
        'defusedxml',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MarkItDown',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if False else None,  # Set to True if icon exists
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MarkItDown',
)
