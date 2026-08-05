# -*- coding: utf-8 -*-
"""
Script de verification des prerequis pour MarkItDown GUI
Verifie que toutes les dependances requises sont installees
"""

import sys
import os
import subprocess
from pathlib import Path

# Forcer l'encodage UTF-8 sur Windows
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"


def check_python_version():
    """Verifier la version de Python"""
    if sys.version_info < (3, 10):
        print(f"[FAIL] Python 3.10+ requis. Vous avez Python {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print(f"[OK] Python {sys.version_info.major}.{sys.version_info.minor} - OK")
    return True


def check_module(module_name, package_name=None):
    """Verifier si un module Python est installe"""
    if package_name is None:
        package_name = module_name

    try:
        __import__(module_name)
        print(f"[OK] {package_name} - installe")
        return True
    except ImportError:
        print(f"[FAIL] {package_name} - NON INSTALLE")
        return False


def check_pyqt6():
    """Verifier PyQt6"""
    return check_module("PyQt6", "PyQt6")


def check_markitdown():
    """Verifier MarkItDown"""
    try:
        sys.path.insert(0, str(Path(__file__).parent / "markitdown" / "packages" / "markitdown" / "src"))
        from markitdown import MarkItDown
        print("[OK] MarkItDown - installe")
        return True
    except ImportError as e:
        print(f"[FAIL] MarkItDown - NON INSTALLE ({e})")
        return False


def check_markitdown_dependencies():
    """Verifier les dependances de MarkItDown"""
    required = [
        ("bs4", "BeautifulSoup4"),
        ("requests", "Requests"),
        ("markdownify", "Markdownify"),
        ("magika", "Magika"),
        ("charset_normalizer", "Charset-Normalizer"),
        ("defusedxml", "DefusedXML"),
    ]

    all_ok = True
    for module, name in required:
        if not check_module(module, name):
            all_ok = False

    return all_ok


def check_optional_formats():
    """Verifier les convertisseurs optionnels disponibles"""
    optional = [
        ("python_pptx", "PowerPoint (.pptx)"),
        ("mammoth", "Word (.docx)"),
        ("pandas", "Excel (.xlsx)"),
        ("pdfminer", "PDF avance"),
        ("PIL", "Images (PIL/Pillow)"),
        ("youtube_transcript_api", "YouTube"),
    ]

    print("\nModules optionnels (pour formats supplementaires):")
    for module, name in optional:
        try:
            __import__(module)
            print(f"  [OK] {name}")
        except ImportError:
            print(f"  [INFO] {name} - non installe")


def main():
    """Effectuer toutes les verifications"""
    print("=" * 60)
    print("Verification des prerequis - MarkItDown GUI")
    print("=" * 60)

    print("\nPrerequisites obligatoires:")

    checks = [
        ("Python", check_python_version),
        ("PyQt6", check_pyqt6),
        ("MarkItDown", check_markitdown),
    ]

    all_required_ok = True
    for name, check_func in checks:
        try:
            if not check_func():
                all_required_ok = False
        except Exception as e:
            print(f"[FAIL] {name} - Erreur: {e}")
            all_required_ok = False

    print("\nDependances de MarkItDown:")
    if not check_markitdown_dependencies():
        all_required_ok = False

    check_optional_formats()

    print("\n" + "=" * 60)
    if all_required_ok:
        print("[OK] Tous les prerequis sont installes!")
        print("Vous pouvez lancer l'application:")
        print("  python markitdown_gui.py")
        print("  ou")
        print("  .\\launch_gui.bat")
        return 0
    else:
        print("[FAIL] Il manque certains prerequis.")
        print("\nPour installer les dependances manquantes:")
        print("  pip install PyQt6")
        print("  pip install -e 'markitdown/packages/markitdown[all]'")
        return 1


if __name__ == "__main__":
    sys.exit(main())
