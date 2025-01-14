from transformers import pipeline
import json
import pytest

# Chargement d'un modèle IA adapté pour le traitement de texte
def charger_modele():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Chargement du modèle
classifieur = charger_modele()

# Catégories pour SISR et SLAM
categories = ["SISR", "SLAM"]

# Fonction IA pré-entraînée
def calculateur_reponse_ia(tab_questions):
    """
    Utilise un modèle IA pré-entraîné pour classifier SISR ou SLAM.
    """
    scores = {"SISR": 0, "SLAM": 0}

    for question in tab_questions:
        resultat = classifieur(question, categories)
        label = resultat['labels'][0]  # La meilleure catégorie prédite
        scores[label] += 1

    if scores["SISR"] > scores["SLAM"]:
        return 'SISR est plus adaptée'
    elif scores["SISR"] < scores["SLAM"]:
        return 'SLAM est plus adaptée'
    else:
        return 'Les deux options conviennent'

# Exporter les résultats pour analyse
def exporter_resultats(tab_questions, fichier="resultats.json"):
    resultats = {
        "questions": tab_questions,
        "classification": calculateur_reponse_ia(tab_questions)
    }
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(resultats, f, ensure_ascii=False, indent=4)
    print(f"Résultats exportés dans {fichier}")

# Questionnaire interactif
def questionnaire():
    print("--- Questionnaire d'orientation SISR/SLAM ---")
    q1 = input("Décrivez ce qui vous intéresse dans le domaine informatique : ").strip()
    q2 = input("Quelles sont les activités que vous aimeriez explorer dans votre futur métier ? ").strip()
    q3 = input("Quelles compétences techniques souhaitez-vous acquérir ? ").strip()
    q4 = input("Parlez de vos préférences ou expériences passées liées à l'informatique : ").strip()

    tab_questions = [q1, q2, q3, q4]

    resultat = calculateur_reponse_ia(tab_questions)
    print(f"Résultat : {resultat}")

    exporter_resultats(tab_questions)

if __name__ == "__main__":
    questionnaire()


# Tests unitaires
def test_calculateur_reponse_ia_sisr():
    responses = ["Je suis intéressé par les systèmes et réseaux", "J'aime résoudre des problèmes techniques", "Je souhaite gérer des infrastructures", "J'ai de l'expérience en maintenance réseau"]
    assert calculateur_reponse_ia(responses) == 'SISR est plus adaptée'

def test_calculateur_reponse_ia_slam():
    responses = ["J'aime créer des applications", "Je souhaite concevoir des logiciels", "Je veux apprendre à programmer", "J'ai fait un projet en développement web"]
    assert calculateur_reponse_ia(responses) == 'SLAM est plus adaptée'

def test_calculateur_reponse_ia_equal():
    responses = ["Je m'intéresse aux systèmes et au développement", "J'aime explorer différents aspects de l'informatique", "Je veux apprendre les réseaux et la programmation", "J'ai travaillé sur des serveurs et des applications"]
    assert calculateur_reponse_ia(responses) == 'Les deux options conviennent'