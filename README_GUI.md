# MarkItDown GUI - Application Graphique

Application graphique moderne et intuitive pour convertir vos fichiers en Markdown facilement! 

## Prérequis

- Python 3.10 ou supérieur  
- PyQt6 (interface graphique)
- Dépendances de MarkItDown (pdfminer, mammoth, pandas, etc.)

Tous les prérequis ont déjà été installés dans votre environnement virtuel.

## Démarrage rapide

### Sur Windows

Deux options:

**Option 1 - Double-cliquez sur le fichier batch:**
```
launch_gui.bat
```

**Option 2 - Ligne de commande PowerShell:**
```powershell
.\.venv\Scripts\python .\markitdown_gui.py
```

**Option 3 - Ligne de commande CMD:**
```cmd
.venv\Scripts\python markitdown_gui.py
```

### Sur macOS/Linux

```bash
source .venv/bin/activate
python markitdown_gui.py
```

## Interface de l'application

### 1. Barre d'outils principale
- **📁 Sélectionner un fichier** - Ouvrir un explorateur de fichiers
- **🔄 Convertir** - Lancer la conversion du fichier sélectionné
- **💾 Enregistrer Markdown** - Sauvegarder le résultat en fichier .md
- **📋 Copier le texte** - Copier le Markdown dans le presse-papiers

### 2. Onglet "Visualisation"
- **Panel gauche** - Aperçu du fichier original (si disponible)
- **Panel droit** - Contenu Markdown complet et modifiable

### 3. Onglet "Options"
Configuration des paramètres avancés:
- **Plugins** - Activer les plugins tiers (markitdown-ocr, etc.)
- **Azure Document Intelligence** - Pour OCR de documents complexes
- **Azure Content Understanding** - Pour extraction structurée avec YAML

### 4. Onglet "À propos"
Informations sur le projet et formats supportés

## Formats supportés

✅ **Documents**
- PDF (pdfminer.six, pdfplumber)
- Word (.docx) avec mammoth
- Excel (.xlsx, .xls) avec pandas
- PowerPoint (.pptx) avec python-pptx
- EPub

✅ **Web**
- HTML avec BeautifulSoup
- RSS Feeds
- Wikipedia (URLs)
- YouTube (URLs avec transcription)

✅ **Médias**
- Images (JPG, PNG, GIF, etc.)
- Audio (transcription)
- Métadonnées EXIF

✅ **Données**
- CSV
- JSON
- XML
- ZIP (itération sur contenu)

✅ **Autres**
- Jupyter Notebooks (.ipynb)
- Outlook Messages (.msg)
- Texte brut

## Workflow typique

1. **Sélectionner le fichier**
   ```
   Cliquez: "📁 Sélectionner un fichier"
   Choisir: rapport.pdf, presentation.pptx, etc.
   ```

2. **Configurer les options (optionnel)**
   ```
   Onglet: "⚙️ Options"
   Cocher: Options désirées
   ```

3. **Lancer la conversion**
   ```
   Cliquez: "🔄 Convertir"
   Attendre: Affichage du résultat
   ```

4. **Sauvegarder le résultat**
   ```
   Cliquez: "💾 Enregistrer Markdown"
   Choisir: Chemin et nom du fichier
   ```

## Exemples d'utilisation

### Convertir un PDF
```
1. Sélectionner → mon-document.pdf
2. Cliquer → Convertir
3. Attendre ~5 secondes
4. Cliquer → Enregistrer Markdown
5. Résultat → mon-document.md
```

### Convertir une présentation PowerPoint
```
1. Sélectionner → ma-presentation.pptx
2. Cliquer → Convertir
3. Attendre ~3 secondes
4. Copier → le texte dans le presse-papiers
```

### Convertir un Excel avec plusieurs feuilles
```
1. Sélectionner → donnees.xlsx
2. Cliquer → Convertir
3. Résultat → Tableau Markdown structuré
4. Enregistrer → données.md
```

### Extraire du texte d'une image
```
1. Sélectionner → screenshot.jpg
2. Cliquer → Convertir
3. Résultat → Texte reconnu + métadonnées
```

### Récupérer la transcription YouTube
```
1. Sélectionner → https://youtube.com/...
2. Cliquer → Convertir
3. Attendre ~ 10 secondes
4. Résultat → Transcription en Markdown
```

## Raccourcis clavier

| Action | Raccourci |
|--------|-----------|
| Aller à l'onglet Visualisation | `Ctrl+1` |
| Aller à l'onglet Options | `Ctrl+2` |
| Aller à l'onglet À propos | `Ctrl+3` |

*Note: Autres raccourcis standard (Ctrl+C, Ctrl+A) fonctionnent dans le texte Markdown*

## Dépannage

### "File not found: Module PyQt6"
**Solution:**
```bash
.venv\Scripts\pip install PyQt6
```

### "Module 'markitdown' not found"
**Solution:**
```bash
cd markitdown/packages/markitdown
pip install -e .
```

### Erreur "Format non supporté"
**Le format de votre fichier n'est pas supporté ou la dépendance est manquante**

Installation des dépendances supplémentaires:
```bash
# Pour PDF avancé
pip install pdfplumber pdfminer.six

# Pour Word
pip install mammoth lxml

# Pour Excel
pip install pandas openpyxl xlrd

# Pour PowerPoint
pip install python-pptx

# Pour tout
pip install -e 'markitdown/packages/markitdown[all]'
```

### L'application est très lente
- C'est normal pour le premier fichier (chargement des bibliothèques)
- Les fichiers volumineux prennent plus de temps
- Les gros PDF peuvent prendre 20-30 secondes

### Le texte Markdown n'apparaît pas
- Attendez la fin de la conversion (barre de progression)
- Vérifiez le message d'erreur dans la barre de statut
- Essayez avec un fichier plus simple

### Azure Document Intelligence/Content Understanding ne fonctionne pas
- Vous n'avez pas d'endpoint Azure configuré
- C'est optionnel - décochez l'option pour utiliser la conversion locale
- Pour l'activer, créez une ressource Azure et entrez l'endpoint

## Configuration avancée

### Activer les plugins OCR

1. Installer le plugin:
   ```bash
   pip install markitdown-ocr
   ```

2. Cocher "Activer les plugins tiers" dans Options

3. Les images dans les PDFs seront converties par OCR

### Utiliser Azure Document Intelligence

1. Créer une ressource dans Azure Portal
2. Copier l'endpoint Azure
3. Cocher "Utiliser Azure Document Intelligence"
4. Entrer l'endpoint dans le champ "Endpoint Azure"
5. Convertir - qualité OCR améliorée!

### Utiliser Azure Content Understanding

1. Créer une ressource Content Understanding dans Azure
2. Copier l'endpoint
3. (Optionnel) Créer un analyseur personnalisé
4. Cocher "Utiliser Azure Content Understanding"
5. Configurer l'endpoint et l'analyzer ID
6. Convertir - extraction structurée en YAML!

## Performance

Temps de conversion typiques:

| Type | Taille | Temps |
|------|--------|-------|
| TXT | < 1 MB | < 1 sec |
| PDF simple | < 10 pages | 2-5 sec |
| PDF complexe | 50+ pages | 15-30 sec |
| Image | 5 MB | 2-5 sec |
| Excel | 1000 lignes | 3-8 sec |
| PowerPoint | 20 slides | 3-8 sec |
| ZIP | 50 fichiers | 5-15 sec |

*Performance dépendante de votre machine et des options activées*

## Sécurité

⚠️ **Important:**
- MarkItDown accède aux fichiers avec les permissions du processus
- Ne convertissez que des fichiers de confiance
- Attention aux archives ZIP (peuvent contenir du code)
- Attention aux fichiers Office macro (risques de sécurité)

## Structure du projet

```
ConvertMarkdown/
├── markitdown/                      # Projet MarkItDown original (Microsoft)
│   └── packages/markitdown/
│       ├── src/markitdown/          # Code source
│       └── tests/                   # Tests
├── markitdown_gui.py                # Application graphique principale ⭐
├── launch_gui.bat                   # Script de lancement Windows
├── launch_gui.ps1                   # Script PowerShell
├── check_requirements.py             # Vérification des prérequis
├── README_GUI.md                    # Ce fichier
└── GUIDE_GUI.md                     # Guide détaillé d'utilisation
```

## Améliorations futures

- [ ] Support du Drag & Drop
- [ ] Historique des fichiers récents
- [ ] Conversion par batch (plusieurs fichiers)
- [ ] Thèmes sombres/clairs
- [ ] Recherche et remplacement dans Markdown
- [ ] Export en HTML, PDF (depuis Markdown)
- [ ] Paramètres LLM (GPT-4o) pour descriptions
- [ ] Raccourcis clavier personnalisables
- [ ] Support des favoris (formats fréquents)

## Contribution

L'application GUI et les scripts sont des additions au projet MarkItDown original.

Pour contribuer au projet MarkItDown:
- GitHub: https://github.com/microsoft/markitdown
- Issues: https://github.com/microsoft/markitdown/issues

## Licence

MIT (même que MarkItDown)

## Support

**Pour les problèmes de la GUI:**
- Vérifiez que Python 3.10+ est utilisé
- Exécutez: `.venv\Scripts\python check_requirements.py`
- Lisez GUIDE_GUI.md pour plus de détails

**Pour les problèmes de MarkItDown:**
- Consultez: https://github.com/microsoft/markitdown
- Ouvrez une issue: https://github.com/microsoft/markitdown/issues

## Crédits

- **MarkItDown**: Créé par l'équipe AutoGen de Microsoft
- **GUI**: Créée avec PyQt6
- **Objectif**: Faciliter l'utilisation de MarkItDown pour tous

---

**Version**: 1.0  
**Dernière mise à jour**: Août 2026  
**Statut**: ✅ Fonctionnel et prêt à l'emploi
