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
    q1 = input("Aimez-vous travailler sur des serveurs et la virtualisation ? (Oui/Non) ").lower()
    q2 = input("Êtes-vous intéressé(e) par la maintenance et la sécurité réseau ? (Oui/Non) ").lower()
    q3 = input("Souhaitez-vous développer des applications ? (Oui/Non) ").lower()
    q4 = input("Avez-vous de l’appétence pour la programmation ? (Oui/Non) ").lower()

    tab_questions = [q1, q2, q3, q4]

    resultat = calculateur_reponse_ia(tab_questions)
    print(f"Résultat : {resultat}")

    exporter_resultats(tab_questions)

if __name__ == "__main__":
    questionnaire()