# Contribuer

Merci de ton intérêt pour ce projet !

## Mettre en place l'environnement

```bash
git clone https://github.com/l8ne2/real-time-object-detection.git
cd real-time-object-detection
python -m venv .venv
# Activer l'environnement (voir le README)
python -m pip install -e ".[dev]"
```

## Workflow

1. Crée une branche à partir de `main` : `git checkout -b feature/ma-fonctionnalite`.
2. Fais tes modifications, avec des tests.
3. Vérifie la qualité (voir ci-dessous).
4. Ouvre une Pull Request vers `main` en décrivant ce qui change et pourquoi.

## Vérifications avant une Pull Request

```bash
python -m ruff check .
python -m ruff format .
python -m pytest --cov
```

La CI lance les mêmes contrôles : une Pull Request doit être verte pour être fusionnée.

## Conventions

- **Code** : annotations de types, docstrings courtes, noms et messages de journaux en anglais.
- **Tests** : toute nouvelle fonctionnalité ou correction s'accompagne de tests ; les tests ne doivent dépendre ni d'une webcam ni d'un modèle téléchargé.
- **Commits** : messages courts au format `type: description`, avec les types `feat`, `fix`, `docs`, `test`, `refactor`, `build`, `ci`, `chore`, `style`.

## Signaler un problème

Ouvre une issue avec :
- ce que tu attendais et ce qui s'est passé,
- ton système et ta version de Python,
- le message d'erreur complet.