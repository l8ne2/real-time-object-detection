# 🔍 Détection d'objets en temps réel

[![CI](https://github.com/l8ne2/real-time-object-detection/actions/workflows/ci.yml/badge.svg)](https://github.com/l8ne2/real-time-object-detection/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
[![Licence MIT](https://img.shields.io/badge/licence-MIT-green)](LICENSE)
[![Ruff](https://img.shields.io/badge/lint-ruff-261230)](https://github.com/astral-sh/ruff)

Application de vision par ordinateur en Python qui détecte des objets en temps réel avec **OpenCV** et **YOLO** (Ultralytics), à partir d'une webcam, d'un fichier vidéo ou d'une image.

<p align="center">
  <img src="docs/demo.gif" alt="Démonstration de la détection d'objets en temps réel" width="640">
</p>

## ✨ Fonctionnalités

- 📷 Trois sources d'entrée : webcam, fichier vidéo, image.
- 🤖 Détection par un modèle YOLO préentraîné, au choix.
- 🎯 Rectangles de détection, classes et scores de confiance affichés à l'écran.
- ⏱️ Compteur d'images par seconde (FPS) lissé et nombre d'objets par image.
- 📊 Résumé de session à la fin : images traitées et objets les plus fréquents.
- ⚙️ Interface en ligne de commande avec seuil de confiance réglable.
- 🧩 Architecture modulaire, typée et testée, avec intégration continue.

## ⚙️ Prérequis

- Python 3.11 ou plus.
- Une webcam (uniquement pour le mode temps réel).
- Une connexion Internet à la première exécution, pour télécharger le modèle.

## 🚀 Installation

```bash
git clone https://github.com/l8ne2/real-time-object-detection.git
cd real-time-object-detection

python -m venv .venv
```

Activer l'environnement virtuel :

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

Installer le projet :

```bash
python -m pip install -e .
```

L'installation peut prendre quelques minutes : Ultralytics dépend de PyTorch, qui est volumineux.

## ▶️ Utilisation

```bash
object-detect                              # webcam par défaut
object-detect --source 1                   # deuxième webcam
object-detect --source video.mp4           # fichier vidéo
object-detect --source photo.jpg           # image
object-detect --model yolov8s.pt --conf 0.7
```

Si le chemin d'un fichier contient des espaces, mets-le entre guillemets.

| Option | Description | Défaut |
| --- | --- | --- |
| `--model` | Nom ou chemin du modèle YOLO | `yolov8n.pt` |
| `--conf` | Seuil de confiance, entre 0 et 1 | `0.5` |
| `--source` | Index de webcam, fichier vidéo ou image | `0` |
| `-v`, `--verbose` | Active les journaux de débogage | désactivé |
| `--version` | Affiche la version | |

**Commandes clavier** : `q` quitte l'application. En mode image, la fenêtre reste ouverte jusqu'à l'appui sur une touche.

Le modèle est téléchargé automatiquement à la première utilisation s'il n'est pas déjà présent.

## 🛠️ Développement

```bash
python -m pip install -e ".[dev]"

python -m ruff check .          # lint
python -m ruff format .         # formatage
python -m pytest --cov          # tests et couverture
```

Les tests utilisent des objets simulés (mocks) : ils ne nécessitent ni webcam ni modèle téléchargé. La CI GitHub Actions lance le lint et les tests à chaque push. Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour contribuer.

## 🧠 Architecture

```text
real-time-object-detection/
├── app/
│   ├── main.py          # point d'entrée et coordination
│   ├── cli.py           # arguments de la ligne de commande
│   ├── config.py        # configuration de l'application
│   ├── camera.py        # capture webcam et vidéo
│   ├── detector.py      # chargement du modèle YOLO et détection
│   ├── visualizer.py    # affichage des résultats
│   ├── fps.py           # compteur de FPS
│   └── stats.py         # statistiques de détection
├── tests/               # tests unitaires
├── docs/                # documentation et démonstration
├── .github/workflows/   # intégration continue
└── pyproject.toml       # métadonnées, dépendances, outils
```

Chaque module a une seule responsabilité, ce qui facilite les tests et l'ajout de fonctionnalités. Le détail et le schéma du flux de données sont dans [docs/architecture.md](docs/architecture.md).

## 🔮 Pistes d'amélioration

- [ ] Suivi d'objets (tracking) pour compter des objets uniques.
- [ ] Export des statistiques (CSV ou JSON).
- [ ] Enregistrement de la vidéo annotée.
- [ ] Prise en charge de dossiers d'images.
- [ ] Image Docker.

## 🙏 Remerciements et licence

Ce projet utilise [Ultralytics YOLO](https://github.com/ultralytics/ultralytics), [OpenCV](https://opencv.org/) et [NumPy](https://numpy.org/). Ultralytics est distribué sous sa propre licence (AGPL-3.0, avec une licence commerciale en option, à vérifier sur son dépôt) : consulte-la avant tout usage commercial.

Le code de ce projet est distribué sous licence MIT. Voir [LICENSE](LICENSE).

## 👨‍💻 Auteur

**Aliou BA**, étudiant en informatique, projet réalisé dans le cadre de l'apprentissage de la vision par ordinateur. [GitHub](https://github.com/l8ne2)