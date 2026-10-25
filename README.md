🔍 Détection d'objets en temps réel

Une application de vision par ordinateur (Computer Vision) développée en Python, utilisant OpenCV et YOLO pour détecter des objets à partir d'une webcam en temps réel.

Le système identifie les objets présents dans l'image et affiche des rectangles de détection, les noms des classes ainsi que les scores de confiance associés.

✨ Fonctionnalités

- 📷 Capture vidéo à partir d'une webcam.
- 🤖 Détection d'objets grâce à un modèle YOLO préentraîné.
- 🎯 Affichage des objets détectés avec leurs rectangles de délimitation.
- 📊 Affichage des classes et des scores de confiance.
- 🧩 Architecture modulaire orientée objet.
- 🧪 Tests automatisés avec pytest.

🛠️ Technologies utilisées

- Python : langage de programmation.
- OpenCV : capture vidéo et affichage des images.
- Ultralytics YOLO : détection d'objets.
- NumPy : manipulation des tableaux numériques.
- pytest : tests automatisés.

📁 Architecture du projet

real-time-object-detection/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── camera.py
│   ├── detector.py
│   └── visualizer.py
├── models/
│   └── .gitkeep
├── tests/
│   ├── __init__.py
│   └── test_detector.py
├── docs/
│   └── architecture.md
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
└── .python-version

⚙️ Prérequis

- Python installé sur la machine.
- Une webcam fonctionnelle.
- Une connexion Internet pour télécharger le modèle lors de sa première utilisation.
- Git pour récupérer le projet.

🚀 Installation

1. Cloner le dépôt

Remplacez "l8ne2" par votre nom d'utilisateur GitHub.

git clone https://github.com/l8ne2/real-time-object-detection.git
cd real-time-object-detection

2. Créer un environnement virtuel

python -m venv .venv

Sous Windows PowerShell :

.\.venv\Scripts\Activate.ps1

3. Installer les dépendances

python -m pip install -r requirements.txt

▶️ Utilisation

Depuis le dossier racine du projet, exécutez :

python -m app.main

La webcam s'ouvre et le système commence à détecter les objets visibles.

Pour arrêter l'application, appuyez sur la touche "q".

Le modèle YOLO préentraîné est téléchargé automatiquement lors de sa première utilisation s'il n'est pas déjà disponible localement.

🧪 Exécuter les tests

Pour vérifier le fonctionnement des tests automatisés :

python -m pytest -v

🧠 Architecture logicielle

Le projet repose sur une séparation des responsabilités :

- "main.py" : point d'entrée et coordination de l'application.
- "camera.py" : ouverture de la webcam et capture des images.
- "detector.py" : chargement du modèle YOLO et détection des objets.
- "visualizer.py" : affichage des résultats de détection.
- "test_detector.py" : vérification du comportement du détecteur.

Cette organisation facilite la maintenance, les tests et l'ajout de nouvelles fonctionnalités.

🔮 Améliorations prévues

- [ ] Ajouter un compteur d'images par seconde (FPS).
- [ ] Permettre de modifier le seuil de confiance.
- [ ] Prendre en charge des images et des fichiers vidéo.
- [ ] Améliorer les tests avec des modèles simulés.
- [ ] Ajouter des statistiques sur les objets détectés.
- [ ] Optimiser les performances sur les machines disposant de ressources limitées.

👨‍💻 Auteur

Projet personnel réalisé dans le cadre de l'apprentissage de la vision par ordinateur, du traitement d'images et de l'intelligence artificielle.

📄 Licence

Consultez le fichier "LICENSE" pour connaître les conditions d'utilisation et de distribution du projet.