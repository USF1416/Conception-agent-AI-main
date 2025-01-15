
from flask import Flask, request, render_template_string
import mysql.connector
import json

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="agent-ai-netlify"
    )

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            questions TEXT NOT NULL,
            result VARCHAR(255) NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

def save_to_mysql(questions, result):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO results (questions, result) VALUES (%s, %s)",
        (json.dumps(questions), result)
    )
    connection.commit()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def questionnaire():
    resultat = None
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']

        tab_questions = [q1, q2, q3, q4]
        resultat = "Votre résultat ici"  # Appelez la fonction IA ici

        init_db()
        save_to_mysql(tab_questions, resultat)

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
            <label>Décrivez un projet ou une activité :</label>
            <textarea name="q2" required></textarea>
            <label>Quelles compétences techniques voulez-vous acquérir ?</label>
            <textarea name="q3" required></textarea>
            <label>Parlez de vos expériences passées :</label>
            <textarea name="q4" required></textarea>
            <button type="submit">Soumettre</button>
        </form>
        {% if resultat %}
            <h2>Résultat : {{ resultat }}</h2>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(HTML_TEMPLATE, resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
