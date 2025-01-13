# Conception d'un Agent IA pour l'Orientation SISR/SLAM

Ce projet utilise une IA simple pour classifier les préférences des utilisateurs entre les deux spécialisations du BTS SIO : **SISR** et **SLAM**.

## Fonctionnalités

- **Questionnaire interactif** : Pose des questions pour identifier les préférences de l'utilisateur.
- **Classifieur basé sur des mots-clés** : Utilise des listes de mots-clés spécifiques pour évaluer les réponses.
- **Tests unitaires** : Vérifie la validité des prédictions grâce à `pytest`.
- **Pipeline CI/CD** : Automatisation des tests et du déploiement via GitHub Actions.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone <url_du_dépôt>
   cd Conception-agent-AI-main
   ```

2. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Exécuter le questionnaire
Pour lancer le questionnaire interactif, exécutez :
```bash
python src/questionnaire.py
```

Répondez aux questions posées pour obtenir une suggestion d'orientation entre SISR et SLAM.

### Exécuter les tests
Pour exécuter les tests unitaires et vérifier le fonctionnement du classifieur :
```bash
pytest
```

## Structure du Projet

- `src/questionnaire.py` : Contient le script principal du questionnaire interactif.
- `.github/workflows/ci.yml` : Configuration du pipeline CI/CD pour automatiser les tests.
- `requirements.txt` : Liste des dépendances Python nécessaires.
- `README.md` : Documentation du projet.

## Contributeurs

N'hésitez pas à soumettre des suggestions, signaler des bugs ou proposer des améliorations en créant une pull request ou en ouvrant une issue.

---
**Contact** : Pour toute question, contactez [Votre Nom/Email].
