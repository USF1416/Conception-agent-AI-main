from transformers import pipeline
import json
import pytest

# Chargement d'un modèle IA adapté pour le traitement de texte
def charger_modele():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Chargement du modèle
classifieur = charger_modele()

# Catégories pour SISR et SLAM (renommées pour une meilleure compréhension)
categories = ["Travail sur les systèmes et réseaux", "Développement d'applications"]

# Fonction IA pré-entraînée
def calculateur_reponse_ia(tab_questions):
    """
    Utilise un modèle IA pré-entraîné pour classifier les réponses utilisateur entre SISR et SLAM.
    """
    scores = {"SISR": 0, "SLAM": 0}

    for question in tab_questions:
        resultat = classifieur(question, categories)
        label = resultat['labels'][0]  # Catégorie avec le score le plus élevé
        if label == "Travail sur les systèmes et réseaux":
            scores["SISR"] += 1
        elif label == "Développement d'applications":
            scores["SLAM"] += 1

    if scores["SISR"] > scores["SLAM"]:
        return 'SISR est plus adaptée'
    elif scores["SISR"] < scores["SLAM"]:
        return 'SLAM est plus adaptée'
    else:
        return 'Les deux options conviennent'

# Exporter les résultats pour analyse
def exporter_resultats(tab_questions, fichier="resultats.json"):
    """
    Enregistre les questions et le résultat final dans un fichier JSON.
    """
    resultats = {
        "questions": tab_questions,
        "classification": calculateur_reponse_ia(tab_questions)
    }
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, ensure_ascii=False, indent=4)
    print(f"Résultats exportés dans {fichier}")

# Questionnaire interactif
def questionnaire():
    """
    Collecte des réponses utilisateur et affiche le résultat de l'orientation.
    """
    print("--- Questionnaire d'orientation SISR/SLAM ---")
    q1 = input("Qu'est-ce qui vous intéresse le plus dans l'informatique ? ").strip()
    q2 = input("Décrivez un projet ou une activité que vous aimeriez réaliser en informatique : ").strip()
    q3 = input("Quelles compétences techniques souhaitez-vous maîtriser ? ").strip()
    q4 = input("Parlez de vos expériences passées ou de ce que vous aimeriez apprendre en informatique : ").strip()

    tab_questions = [q1, q2, q3, q4]

    resultat = calculateur_reponse_ia(tab_questions)
    print(f"Résultat : {resultat}")

    exporter_resultats(tab_questions)

if __name__ == "__main__":
    questionnaire()

# Tests unitaires
def test_calculateur_reponse_ia_sisr():
    responses = [
        "Je suis intéressé par les systèmes et réseaux",
        "Je souhaite travailler sur des infrastructures",
        "J'aime gérer des serveurs et des réseaux",
        "Mon expérience est orientée vers la maintenance réseau"
    ]
    assert calculateur_reponse_ia(responses) == 'SISR est plus adaptée'

def test_calculateur_reponse_ia_slam():
    responses = [
        "J'aime concevoir des applications",
        "Je veux travailler sur des logiciels innovants",
        "Je souhaite améliorer mes compétences en programmation",
        "J'ai déjà travaillé sur des projets de développement web"
    ]
    assert calculateur_reponse_ia(responses) == 'SLAM est plus adaptée'

def test_calculateur_reponse_ia_equal():
    responses = [
        "J'aime explorer les réseaux et le développement",
        "Je suis curieux des infrastructures et des applications",
        "Je veux apprendre les systèmes et la programmation",
        "Je suis intéressé par tous les aspects de l'informatique"
    ]
    assert calculateur_reponse_ia(responses) == 'Les deux options conviennent'