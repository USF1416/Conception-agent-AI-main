# Conception d'un Agent IA pour l'Orientation SISR/SLAM

Ce projet utilise une IA simple pour classifier les préférences des utilisateurs entre les deux spécialisations du BTS SIO : **SISR** et **SLAM**.

## Fonctionnalités

-   **Questionnaire interactif** : Pose des questions pour identifier les préférences de l'utilisateur.
-   **Classifieur basé sur des mots-clés** : Utilise des listes de mots-clés spécifiques pour évaluer les réponses.
-   **Tests unitaires** : Vérifie la validité des prédictions grâce à `pytest`.
-   **Pipeline CI/CD** : Automatisation des tests et du déploiement via GitHub Actions.

## Technologies utilisées

-   **Langage** : Python 3.8+
-   **Bibliothèques** :
-   `pytest` : Pour les tests unitaires.
-   `json` : Pour la gestion des résultats des réponses.
-   **CI/CD** : GitHub Actions pour l'automatisation des tests et des déploiements.
-   **Environnement** : Virtualenv pour isoler les dépendances.

## Installation

1.  Clonez ce dépôt :

git clone <url\_du\_dépôt>
cd Conception-agent-AI-main

1.  Assurez-vous que Python 3.8 ou une version supérieure est installé.
2.  Créez un environnement virtuel (recommandé) :

python -m venv venv
source venv/bin/activate  # Sur Windows : venv\\Scripts\\activate

1.  Installez les dépendances Python :

pip install -r requirements.txt

## Utilisation

### Exécuter le questionnaire

Pour lancer le questionnaire interactif, exécutez :

python src/questionnaire.py

**Exemple de sortie :**

Bienvenue dans le questionnaire d'orientation SISR/SLAM !

Question 1 : Préférez-vous travailler avec des réseaux ou développer des applications ?
Votre réponse : développer des applications

Question 2 : Aimez-vous configurer des serveurs ?
Votre réponse : non

---
Suggestion : Vous êtes plutôt orienté SLAM.

### Exécuter les tests

Pour exécuter les tests unitaires et vérifier le fonctionnement du classifieur :

pytest

**Exemple de sortie :**

\=============== test session starts ================

collected 5 items

tests/test\_classifieur.py .....                                          \[100%\]

=============== 5 passed in 0.03s =================

## Structure du Projet

-   `src/questionnaire.py` : Contient le script principal du questionnaire interactif.
-   `src/resultats.json` : Contient les résultats des réponses pour les sessions passées.
-   `.github/workflows/ci.yml` : Configuration du pipeline CI/CD pour automatiser les tests.
-   `requirements.txt` : Liste des dépendances Python nécessaires.
-   `README.md` : Documentation du projet.

## Améliorations futures

-   Ajouter une interface graphique (GUI) pour rendre le questionnaire plus interactif.
-   Intégrer un système d'apprentissage machine pour une classification plus précise.
-   Permettre l'export des résultats sous forme de rapport PDF.

## Contributeurs

N'hésitez pas à soumettre des suggestions, signaler des bugs ou proposer des améliorations en créant une pull request ou en ouvrant une issue.