from flask import request
import sqlite3

# class Question
class Question :
    def __init__(self, title : str, text : str, image : str, position : int, possibleAnswers):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers
        
def json_to_question(json_obj):
    return Question(json_obj["text"], json_obj["title"], json_obj["image"], json_obj["position"], json_obj["possibleAnswers"])

def question_to_json(question_obj):
    json_obj = {
        "text": question_obj.text,
        "title": question_obj.title,
        "image": question_obj.image,
        "position": question_obj.position,
        "possibleAnswers": question_obj.possibleAnswer
    }
    return json_obj

# connection à la base de donnée
def db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
        # pr avoir accès basé sur le nom des colonnes
        # => renverra des lignes qui se comporteront 
        # comme des dictionnaires Python
    return conn # pr accéder à base de données

def add_question():
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # validation du token envoyé en paramètre :
    if not token :
        return 'Unauthorized', 401
    # récupèrer un l'objet json envoyé dans le body de la requète
    payload = request.get_json()
    # récupère les données :
    question = json_to_question(payload)
    # ouvre connexion à la db
    conn = db_connection()
    # exécute requête SQL
    conn.execute('INSERT INTO questions (text, title, image, position, possibleAnswers) VALUES (?, ?, ?, ?, ?)',
                         (question.text, question.title, question.image, question.position, question.possibleAnswers))
    conn.commit()
    conn.close()
    return id
    