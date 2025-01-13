from transformers import pipeline
import pytest

def calculateur_reponse(tab_questions):
    """
    Classifie un texte vers SISR ou SLAM en se basant sur un modèle pré-entraîné.
    """
    # Chargement d'un modèle IA pré-entraîné pour le NLP
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    sisr_keywords = [
        "virtualisation", "maintenance des réseaux", "sécurité des infrastructures", "serveurs", "cloud computing"
    ]

    slam_keywords = [
        "programmation", "développement web", "applications", "API", "bases de données"]

    combined_text = " ".join(tab_questions)

    result = classifier(
        combined_text,
        candidate_labels=["SISR", "SLAM"],
        hypothesis_template="Ce texte est lié à {}."
    )

    best_label = result["labels"][0]
    return f"L'orientation recommandée est : {best_label}"

def questionnaire():
    q1 = input("Aimez-vous travailler sur des serveurs et la virtualisation ? (Oui/Non) ").lower()
    q2 = input("Êtes-vous intéressé(e) par la maintenance et la sécurité réseau ? (Oui/Non) ").lower()
    q3 = input("Souhaitez-vous développer des applications ? (Oui/Non) ").lower()
    q4 = input("Avez-vous de l’appétence pour la programmation ? (Oui/Non) ").lower()

    tab_questions = [q1, q2, q3, q4]
    return calculateur_reponse(tab_questions)

if __name__ == "__main__":
    print(questionnaire())
