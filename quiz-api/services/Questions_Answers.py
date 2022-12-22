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
    # create a connection
    conn = sqlite3.connect('db/database.db')
    conn.isolation_level = None
    conn.execute("begin")
    return conn # pr accéder à base de données

def get_question_by_position(position : int) :
    conn = db_connection()
    question = conn.execute('SELECT * FROM questions WHERE position = ?', (position,)).fetchone()
    conn.close()
    # if question is None:
    #     return f"question with position {position} not found", 404
    return question

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
    # création de la question
    conn.execute('INSERT INTO questions (text, title, image, position) VALUES (?, ?, ?, ?)',
                         (question.text, question.title, question.image, question.position))
    conn.commit()
    conn.rollback()
    # récupère la question créée
    question_added = get_question_by_position(question.position)
    print(f" !!!!!!!!!!!!! PAY ATTENTION !!!!!!!!!!!!!! : {question_added}")
    question_id = question_added[0]
    # création des possibleAnswers
    for answer in question.possibleAnswers :
        conn.execute('INSERT INTO possibleAnswers (text, isCorrect, questionId) VALUES (?, ?, ?)',
                         (answer["text"], answer["isCorrect"], question_id))
    conn.commit()
    conn.rollback()
    conn.close()
    return { "id" : question_id}, 200
    