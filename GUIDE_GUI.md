# Guide d'utilisation - MarkItDown GUI

## Installation

### Prérequis
- Python 3.10+
- Les dépendances de MarkItDown ([all] pour les formats complets)

### Installation de PyQt6

```bash
pip install PyQt6
```

Ou si vous utilisez un environnement virtuel:

```bash
.venv\Scripts\pip install PyQt6
```

## Lancement de l'application

### Option 1: Directement avec Python

```bash
python markitdown_gui.py
```

### Option 2: Depuis un script de lancement (Windows)

Créez un fichier `launch_gui.bat`:

```batch
@echo off
cd /d "%~dp0"
.venv\Scripts\python markitdown_gui.py
pause
```

Puis double-cliquez sur `launch_gui.bat`

### Option 3: Depuis PowerShell

```powershell
.\.venv\Scripts\python .\markitdown_gui.py
```

## Utilisation

### Interface principale

L'application se compose de 3 onglets principaux:

#### 1. 👁️ Visualisation
- **Panel gauche**: Aperçu du fichier converti (premiers 500 caractères)
- **Panel droit**: Contenu Markdown complet

#### 2. ⚙️ Options
Configure les paramètres avancés:
- **Plugins**: Activer les plugins tiers (markitdown-ocr, etc.)
- **Azure Document Intelligence**: Pour conversion OCR avancée
- **Azure Content Understanding**: Pour extraction structurée avec YAML

#### 3. ℹ️ À propos
Informations sur le projet et liens utiles

### Workflow de base

1. **Sélectionner un fichier** 
   - Cliquez sur "📁 Sélectionner un fichier"
   - Choisissez le fichier à convertir

2. **(Optionnel) Configurer les options**
   - Allez à l'onglet "⚙️ Options"
   - Cochez les options désirées

3. **Convertir**
   - Cliquez sur "🔄 Convertir"
   - Attendez la fin de la conversion
   - Le Markdown s'affiche dans le panel droit

4. **Enregistrer ou copier**
   - **💾 Enregistrer Markdown**: Sauvegarde dans un fichier .md
   - **📋 Copier le texte**: Copie dans le presse-papiers

## Formats supportés

### Sans options supplémentaires
- PDF (extraction basique)
- Word (.docx)
- Excel (.xlsx, .xls)
- PowerPoint (.pptx)
- HTML, CSS
- Images (JPG, PNG, GIF, etc.)
- Texte brut (TXT, CSV, JSON, XML)
- EPub
- Jupyter Notebooks
- Outlook Messages
- Fichiers ZIP
- YouTube URLs
- Wikipedia URLs
- RSS Feeds

### Avec Azure Document Intelligence
- PDF avancé (OCR pour documents scannés)
- Extraction structurée
- Meilleure détection de layouts complexes
- Tables détectées précisément

### Avec Azure Content Understanding
- Support vidéo
- Support audio avancé
- Extraction de champs personnalisés
- Sortie YAML structurée

## Exemples de fichiers à tester

```
✓ rapport.pdf               # Document PDF
✓ présentation.pptx         # Présentation PowerPoint
✓ données.xlsx              # Feuille Excel
✓ document.docx             # Document Word
✓ image.jpg                 # Image (avec description)
✓ https://wikipedia.org/... # URL Wikipedia
✓ https://youtube.com/...   # URL YouTube
```

## Raccourcis clavier

| Action | Raccourci |
|--------|-----------|
| Sélectionner fichier | `Ctrl+O` |
| Convertir | `Ctrl+R` |
| Enregistrer | `Ctrl+S` |
| Copier | `Ctrl+C` |

*Note: Les raccourcis peuvent être ajoutés dans les futures versions*

## Dépannage

### "Erreur: Format non supporté"
- Installez les dépendances optionnelles pour le format:
  ```bash
  pip install markitdown[pdf,docx,pptx,xlsx]
  ```

### "La conversion est lente"
- Les premiers accès aux converters sont lents (import des dépendances)
- Les conversions suivantes sont plus rapides
- Pour les gros fichiers, c'est normal que cela prenne du temps

### "Azure Document Intelligence non configuré"
- Laissez l'option décochée si vous n'avez pas d'endpoint Azure
- Pour l'activer, créez une ressource Azure Document Intelligence
- Copiez l'endpoint dans le champ "Endpoint Azure"

### La fenêtre est trop petite
- Redimensionnez la fenêtre
- La taille par défaut est 1400x800
- Taille minimale: 1000x600

## Configuration avancée

### Utiliser avec des API LLM

Pour les descriptions d'images (via GPT-4o):

Créez un fichier `config.py`:

```python
from markitdown import MarkItDown
from openai import OpenAI

# Dans le GUI, il suffirait de passer le client LLM
# C'est une feature future à ajouter
```

### Activer les plugins

Dans l'onglet Options, cochez "Activer les plugins tiers".

Les plugins disponibles:
- `markitdown-ocr`: OCR via LLM
- Et autres depuis https://github.com/search?q=%23markitdown-plugin

## Performance

| Type de fichier | Temps typique |
|-----------------|---------------|
| TXT simple | < 1 sec |
| PDF (< 10 pages) | 2-5 sec |
| PDF (> 50 pages) | 10-30 sec |
| Image (description) | 5-10 sec |
| Excel (données massives) | 5-15 sec |
| PowerPoint | 3-8 sec |

*Les temps peuvent varier selon votre machine et les dépendances installées*

## Sécurité

⚠️ **Important**: MarkItDown accède aux fichiers avec les permissions du processus courant.

### Bonnes pratiques
- Ne convertissez que des fichiers de confiance
- Validez le chemin des fichiers avant conversion
- Soyez prudent avec les archives ZIP (peuvent contenir du code)
- Les fichiers Office peuvent contenir des macros - n'ouvrez que des sources de confiance

## Améliorations futures

- [ ] Raccourcis clavier personnalisables
- [ ] Support du drag & drop
- [ ] Historique des conversions récentes
- [ ] Support de l'intégration LLM (GPT-4o) pour descriptions
- [ ] Batch conversion (convertir plusieurs fichiers)
- [ ] Thèmes sombres/clairs
- [ ] Recherche et remplacement dans le Markdown
- [ ] Export en plusieurs formats (PDF, HTML, etc.)

## Support

Pour les problèmes:
1. Vérifiez que Python 3.10+ est installé
2. Vérifiez que toutes les dépendances sont installées
3. Consultez https://github.com/microsoft/markitdown
4. Ouvrez une issue sur GitHub

## Licence

MIT - Voir le fichier LICENSE dans markitdown/

## Crédit

Application GUI créée pour faciliter l'utilisation de MarkItDown.
MarkItDown original: © Microsoft - Équipe AutoGen
