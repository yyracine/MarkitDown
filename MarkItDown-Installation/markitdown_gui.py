"""
MarkItDown GUI Application
Application graphique pour convertir des fichiers en Markdown
"""

import sys
import os
import traceback
from pathlib import Path
from typing import Optional

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QTextEdit, QLabel, QComboBox,
    QCheckBox, QProgressBar, QSplitter, QMessageBox, QStatusBar,
    QTabWidget, QFormLayout, QLineEdit, QSpinBox, QGroupBox,
    QScrollArea
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt6.QtGui import QIcon, QFont, QTextCursor
from PyQt6.QtCore import QTimer

# Handle both development and PyInstaller bundle environments
def setup_markitdown_path():
    """Configure le chemin d'accès à MarkItDown pour dev et PyInstaller"""
    # Check if running as PyInstaller bundle
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Running as PyInstaller bundle - try _internal first, then root
        possible_paths = [
            os.path.join(sys._MEIPASS, '_internal', 'markitdown', 'packages', 'markitdown', 'src'),
            os.path.join(sys._MEIPASS, 'markitdown', 'packages', 'markitdown', 'src'),
        ]
        markitdown_path = None
        for path in possible_paths:
            if os.path.exists(path):
                markitdown_path = path
                break
        if not markitdown_path:
            markitdown_path = possible_paths[0]
    else:
        # Running in development
        markitdown_path = os.path.join(
            os.path.dirname(__file__),
            'markitdown',
            'packages',
            'markitdown',
            'src'
        )

    if markitdown_path not in sys.path:
        sys.path.insert(0, markitdown_path)

setup_markitdown_path()

# Force PyInstaller to include these modules
try:
    import magika
    import onnxruntime
    import click
except ImportError:
    pass

from markitdown import MarkItDown


class ConversionWorker(QThread):
    """Worker thread pour la conversion sans bloquer l'UI"""
    progress = pyqtSignal(str)
    finished = pyqtSignal(str, str)  # markdown, title
    error = pyqtSignal(str)

    def __init__(self, file_path: str, options: dict):
        super().__init__()
        self.file_path = file_path
        self.options = options

    def run(self):
        try:
            self.progress.emit("Initialisation...")

            # Initialiser MarkItDown avec les options
            md = MarkItDown(
                enable_plugins=self.options.get('use_plugins', False),
                llm_client=None,  # À ajouter si besoin
                llm_model=None
            )

            self.progress.emit(f"Conversion de {Path(self.file_path).name}...")

            # Convertir le fichier
            result = md.convert_local(self.file_path)

            self.progress.emit("Conversion réussie!")
            self.finished.emit(result.markdown, result.title or "Sans titre")

        except FileNotFoundError:
            self.error.emit(f"Fichier non trouvé: {self.file_path}")
        except Exception as e:
            error_msg = f"Erreur lors de la conversion:\n{str(e)}\n\n{traceback.format_exc()}"
            self.error.emit(error_msg)


class MarkItDownGUI(QMainWindow):
    """Application graphique pour MarkItDown"""

    def __init__(self):
        super().__init__()
        self.current_file = None
        self.current_markdown = ""
        self.conversion_worker = None

        self.init_ui()
        self.setWindowTitle("MarkItDown - Convertisseur de Fichiers en Markdown")
        self.setGeometry(100, 100, 1400, 800)
        self.setMinimumSize(1000, 600)

    def init_ui(self):
        """Initialiser l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Toolbar
        toolbar_layout = QHBoxLayout()

        self.select_file_btn = QPushButton("[*] Selectionner un fichier")
        self.select_file_btn.clicked.connect(self.select_file)
        self.select_file_btn.setMinimumHeight(40)
        toolbar_layout.addWidget(self.select_file_btn)

        self.convert_btn = QPushButton("[>] Convertir")
        self.convert_btn.clicked.connect(self.convert_file)
        self.convert_btn.setMinimumHeight(40)
        self.convert_btn.setEnabled(False)
        toolbar_layout.addWidget(self.convert_btn)

        self.save_btn = QPushButton("[S] Enregistrer Markdown")
        self.save_btn.clicked.connect(self.save_markdown)
        self.save_btn.setMinimumHeight(40)
        self.save_btn.setEnabled(False)
        toolbar_layout.addWidget(self.save_btn)

        self.copy_btn = QPushButton("[C] Copier le texte")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.copy_btn.setMinimumHeight(40)
        self.copy_btn.setEnabled(False)
        toolbar_layout.addWidget(self.copy_btn)

        layout.addLayout(toolbar_layout)

        # Fichier sélectionné
        file_info_layout = QHBoxLayout()
        self.file_label = QLabel("Aucun fichier sélectionné")
        self.file_label.setStyleSheet("color: #666; font-style: italic;")
        file_info_layout.addWidget(QLabel("Fichier:"))
        file_info_layout.addWidget(self.file_label)
        file_info_layout.addStretch()
        layout.addLayout(file_info_layout)

        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMaximumHeight(25)
        layout.addWidget(self.progress_bar)

        # Onglets
        tabs = QTabWidget()

        # Onglet 1: Visualisation
        view_widget = QWidget()
        view_layout = QVBoxLayout()

        # Splitter pour diviser l'écran
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Panel gauche: Aperçu du fichier
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("[*] Apercu (optionnel)"))
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setPlaceholderText("L'aperçu du fichier original apparaîtra ici après la conversion")
        left_layout.addWidget(self.preview_text)
        left_widget.setLayout(left_layout)

        # Panel droit: Résultat Markdown
        right_widget = QWidget()
        right_layout = QVBoxLayout()

        markdown_label_layout = QHBoxLayout()
        markdown_label_layout.addWidget(QLabel("[*] Markdown Converti"))
        self.title_label = QLabel()
        self.title_label.setStyleSheet("color: #0066cc; font-weight: bold;")
        markdown_label_layout.addWidget(self.title_label)
        markdown_label_layout.addStretch()
        right_layout.addLayout(markdown_label_layout)

        self.markdown_text = QTextEdit()
        self.markdown_text.setReadOnly(True)
        self.markdown_text.setPlaceholderText("Le Markdown converti apparaîtra ici")
        right_layout.addWidget(self.markdown_text)
        right_widget.setLayout(right_layout)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([700, 700])

        view_layout.addWidget(splitter)
        view_widget.setLayout(view_layout)
        tabs.addTab(view_widget, "[V] Visualisation")

        # Onglet 2: Options
        options_widget = QWidget()
        options_layout = QVBoxLayout()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()

        # Groupe de plugins
        plugins_group = QGroupBox("Plugins")
        plugins_layout = QVBoxLayout()
        self.plugins_checkbox = QCheckBox("Activer les plugins tiers")
        plugins_layout.addWidget(self.plugins_checkbox)
        plugins_group.setLayout(plugins_layout)
        scroll_layout.addWidget(plugins_group)

        # Groupe Azure Document Intelligence
        azure_di_group = QGroupBox("Azure Document Intelligence")
        azure_di_layout = QFormLayout()
        self.use_azure_di = QCheckBox("Utiliser Azure Document Intelligence")
        azure_di_layout.addRow(self.use_azure_di)
        self.azure_endpoint = QLineEdit()
        self.azure_endpoint.setPlaceholderText("https://xxxxx.cognitiveservices.azure.com")
        self.azure_endpoint.setEnabled(False)
        self.use_azure_di.stateChanged.connect(lambda: self.azure_endpoint.setEnabled(self.use_azure_di.isChecked()))
        azure_di_layout.addRow("Endpoint Azure:", self.azure_endpoint)
        azure_di_group.setLayout(azure_di_layout)
        scroll_layout.addWidget(azure_di_group)

        # Groupe Azure Content Understanding
        azure_cu_group = QGroupBox("Azure Content Understanding")
        azure_cu_layout = QFormLayout()
        self.use_azure_cu = QCheckBox("Utiliser Azure Content Understanding")
        azure_cu_layout.addRow(self.use_azure_cu)
        self.azure_cu_endpoint = QLineEdit()
        self.azure_cu_endpoint.setPlaceholderText("https://xxxxx.cognitiveservices.azure.com")
        self.azure_cu_endpoint.setEnabled(False)
        self.use_azure_cu.stateChanged.connect(lambda: self.azure_cu_endpoint.setEnabled(self.use_azure_cu.isChecked()))
        azure_cu_layout.addRow("Endpoint Azure CU:", self.azure_cu_endpoint)

        self.azure_analyzer_id = QLineEdit()
        self.azure_analyzer_id.setPlaceholderText("(Optionnel) ID de l'analyseur personnalisé")
        self.azure_analyzer_id.setEnabled(False)
        self.use_azure_cu.stateChanged.connect(lambda: self.azure_analyzer_id.setEnabled(self.use_azure_cu.isChecked()))
        azure_cu_layout.addRow("Analyzer ID:", self.azure_analyzer_id)
        azure_cu_group.setLayout(azure_cu_layout)
        scroll_layout.addWidget(azure_cu_group)

        scroll_layout.addStretch()
        scroll_content.setLayout(scroll_layout)
        scroll.setWidget(scroll_content)
        options_layout.addWidget(scroll)
        options_widget.setLayout(options_layout)
        tabs.addTab(options_widget, "[#] Options")

        # Onglet 3: À propos
        about_widget = QWidget()
        about_layout = QVBoxLayout()

        about_text = QTextEdit()
        about_text.setReadOnly(True)
        about_text.setMarkdown("""
# MarkItDown GUI

Application graphique pour convertir des fichiers en Markdown.

## Formats supportés

- **Documents**: PDF, Word (.docx), Excel (.xlsx, .xls), PowerPoint (.pptx), EPub
- **Web**: HTML, RSS, Wikipedia, YouTube
- **Média**: Images (JPG, PNG, etc.), Audio, Vidéo
- **Données**: CSV, JSON, XML, ZIP
- **Autres**: Jupyter Notebooks, Outlook Messages

## Caracteristiques

[*] Conversion rapide et de haute qualite
[+] Support des plugins tiers
[cloud] Integration Azure Document Intelligence et Content Understanding
[doc] Previsualisation en temps reel
[save] Sauvegarde facile des resultats

## À propos

MarkItDown est créé par l'équipe AutoGen de Microsoft.

[GitHub](https://github.com/microsoft/markitdown)
""")
        about_layout.addWidget(about_text)
        about_widget.setLayout(about_layout)
        tabs.addTab(about_widget, "[i] A propos")

        layout.addWidget(tabs)

        # Barre de statut
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Prêt")

    def select_file(self):
        """Sélectionner un fichier à convertir"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Sélectionner un fichier à convertir",
            "",
            "Tous les fichiers (*.*)"
        )

        if file_path:
            self.current_file = file_path
            self.file_label.setText(file_path)
            self.convert_btn.setEnabled(True)
            self.status_bar.showMessage(f"Fichier sélectionné: {Path(file_path).name}")

    def convert_file(self):
        """Convertir le fichier sélectionné"""
        if not self.current_file:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un fichier")
            return

        # Préparer les options
        options = {
            'use_plugins': self.plugins_checkbox.isChecked(),
            'use_azure_di': self.use_azure_di.isChecked(),
            'azure_endpoint': self.azure_endpoint.text() if self.use_azure_di.isChecked() else None,
            'use_azure_cu': self.use_azure_cu.isChecked(),
            'azure_cu_endpoint': self.azure_cu_endpoint.text() if self.use_azure_cu.isChecked() else None,
            'azure_analyzer_id': self.azure_analyzer_id.text() if self.use_azure_cu.isChecked() else None,
        }

        # Désactiver les boutons pendant la conversion
        self.select_file_btn.setEnabled(False)
        self.convert_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(50)

        # Lancer le worker
        self.conversion_worker = ConversionWorker(self.current_file, options)
        self.conversion_worker.progress.connect(self.on_progress)
        self.conversion_worker.finished.connect(self.on_conversion_finished)
        self.conversion_worker.error.connect(self.on_conversion_error)
        self.conversion_worker.start()

    def on_progress(self, message: str):
        """Mettre à jour la progression"""
        self.status_bar.showMessage(message)

    def on_conversion_finished(self, markdown: str, title: str):
        """Afficher le résultat de la conversion"""
        self.current_markdown = markdown
        self.markdown_text.setMarkdown(markdown)
        self.title_label.setText(f"Titre: {title}")

        self.select_file_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        self.save_btn.setEnabled(True)
        self.copy_btn.setEnabled(True)

        self.progress_bar.setVisible(False)

        # Afficher un aperçu (premiers 500 caractères)
        preview = markdown[:500] + "..." if len(markdown) > 500 else markdown
        self.preview_text.setMarkdown(preview)

        self.status_bar.showMessage(f"[OK] Conversion reussie! ({len(markdown)} caracteres)")
        QMessageBox.information(self, "Succès", "Fichier converti avec succès!")

    def on_conversion_error(self, error_msg: str):
        """Gérer les erreurs de conversion"""
        self.select_file_btn.setEnabled(True)
        self.convert_btn.setEnabled(True)
        self.progress_bar.setVisible(False)
        self.progress_bar.setValue(0)

        self.status_bar.showMessage("[!] Erreur lors de la conversion")
        QMessageBox.critical(self, "Erreur de conversion", error_msg)

    def save_markdown(self):
        """Enregistrer le Markdown converti"""
        if not self.current_markdown:
            QMessageBox.warning(self, "Erreur", "Aucun Markdown à enregistrer")
            return

        # Proposer un nom par défaut
        default_name = Path(self.current_file).stem + ".md" if self.current_file else "document.md"

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Enregistrer le fichier Markdown",
            default_name,
            "Markdown Files (*.md);;Text Files (*.txt);;All Files (*.*)"
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.current_markdown)
                self.status_bar.showMessage(f"[OK] Fichier enregistre: {file_path}")
                QMessageBox.information(self, "Succès", f"Fichier enregistré: {Path(file_path).name}")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Impossible d'enregistrer le fichier:\n{str(e)}")

    def copy_to_clipboard(self):
        """Copier le Markdown dans le presse-papiers"""
        if not self.current_markdown:
            QMessageBox.warning(self, "Erreur", "Aucun texte à copier")
            return

        clipboard = QApplication.clipboard()
        clipboard.setText(self.current_markdown)
        self.status_bar.showMessage("[OK] Texte copie dans le presse-papiers!")


def main():
    """Point d'entrée de l'application"""
    app = QApplication(sys.argv)

    # Style moderne
    app.setStyle('Fusion')

    window = MarkItDownGUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
