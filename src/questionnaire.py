from flask import Flask, request, render_template_string
from flask_serverless import serverless
import json
from transformers import pipeline

# Chargement du modèle IA
def charger_modele():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

classifieur = charger_modele()

# Flask application
app = Flask(__name__)

# Questions et catégories
categories = [
    "virtualisation", "sécurité", "cloud", "routage", "configuration réseau",
    "programmation", "bases de données", "design logiciel", "gestion de projet", "intégration continue"
]

def calculateur_reponse_ia(tab_questions):
    scores = {"SISR": 0, "SLAM": 0}
    for question in tab_questions:
        resultat = classifieur(question, categories)
        label = resultat['labels'][0]
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

        # Exporter les résultats
        try:
            with open('resultats.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    data = [data]
        except FileNotFoundError:
            data = []

        data.append({"questions": tab_questions, "resultat": resultat})

        with open('resultats.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    HTML_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Questionnaire</title>
    </head>
    <body>
        <h1>Questionnaire SISR/SLAM</h1>
        <form method="POST" action="/">
            <label>Qu'est-ce qui vous intéresse le plus ?</label>
            <textarea name="q1" required></textarea>
            <button type="submit">Soumettre</button>
        </form>
        {% if resultat %}
            <h2>Résultat : {{ resultat }}</h2>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(HTML_TEMPLATE, resultat=resultat)

# Ajout du support serverless
handler = serverless(app)

if __name__ == "__main__":
    app.run(debug=True)
