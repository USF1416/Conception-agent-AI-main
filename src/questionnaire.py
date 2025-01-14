from transformers import pipeline
from flask import Flask, request, render_template_string
import json

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

# Flask application
app = Flask(__name__)

# Template HTML pour le questionnaire avec CSS intégré
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Questionnaire SISR/SLAM</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #444;
            text-align: center;
        }
        form {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 10px;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        h2 {
            text-align: center;
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <h1>Questionnaire d'orientation SISR/SLAM</h1>
    <form method="POST" action="/">
        <label for="q1">Qu'est-ce qui vous intéresse le plus dans l'informatique ?</label>
        <textarea id="q1" name="q1" rows="3" required></textarea>

        <label for="q2">Décrivez un projet ou une activité que vous aimeriez réaliser en informatique :</label>
        <textarea id="q2" name="q2" rows="3" required></textarea>

        <label for="q3">Quelles compétences techniques souhaitez-vous maîtriser ?</label>
        <textarea id="q3" name="q3" rows="3" required></textarea>

        <label for="q4">Parlez de vos expériences passées ou de ce que vous aimeriez apprendre en informatique :</label>
        <textarea id="q4" name="q4" rows="3" required></textarea>

        <button type="submit">Soumettre</button>
    </form>

    {% if resultat %}
    <h2>Résultat : {{ resultat }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    resultat = None
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']

        tab_questions = [q1, q2, q3, q4]
        resultat = calculateur_reponse_ia(tab_questions)
        print("Questions soumises :", tab_questions)
        print("Résultat généré :", resultat)

        # Exporter les résultats (optionnel)
        try:
            with open('resultats.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({"questions": tab_questions, "resultat": resultat})

        with open('resultats.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    return render_template_string(HTML_TEMPLATE, resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
