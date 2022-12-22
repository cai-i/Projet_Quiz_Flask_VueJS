from flask import request
import sqlite3

# connection à la base de donnée
def db_connection():
    # create a connection
    conn = sqlite3.connect('db/database.db')
    conn.isolation_level = None
    conn.execute("begin")
    return conn # pr accéder à base de données

# class Question
class Question :
    def __init__(self, title : str, text : str, image : str, position : int, possibleAnswers):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

def get_answers_by_questionId(questionId) :
    conn = db_connection()
    possibleAnswers = conn.execute('SELECT * FROM possibleAnswers WHERE questionId = ?', (questionId,)).fetchall()
    conn.close()
    possibleAnswers = [{"id" : x[0], "text" : x[1], "isCorrect" : x[2], "questionId" : x[3]} for x in possibleAnswers]
    for answer in possibleAnswers:
        if answer["isCorrect"] == 0 :
            answer["isCorrect"] = False
        else :
            answer["isCorrect"] = True
    return possibleAnswers
        
# convertit un objet json en objet Question
def json_to_question(json_obj):
    return Question(json_obj["text"], json_obj["title"], json_obj["image"], json_obj["position"], json_obj["possibleAnswers"])

# convertit un objet Question en json avec en plus les possibleAnswers
def question_to_json(question_obj):
    json_obj = {
        "text": question_obj[2],
        "title": question_obj[1],
        "image": question_obj[3],
        "position": question_obj[4],
        "possibleAnswers": get_answers_by_questionId(question_obj[0])
    }
    return json_obj

def get_question_by_id(question_id : int) :
    conn = db_connection()
    question = conn.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
    conn.close()
    if question is None:
        return f"question with id {question_id} not found", 404
    return question_to_json(question)

def get_question_by_position(position : int) :
    conn = db_connection()
    question = conn.execute('SELECT * FROM questions WHERE position = ?', (position,)).fetchone()
    conn.close()
    if question is None:
        return f"question with position {position} not found", 404
    return question_to_json(question)

# retourne l'id d'une question si sa position est donnée
def get_question_id_by_position(position : int) :
    conn = db_connection()
    question = conn.execute('SELECT * FROM questions WHERE position = ?', (position,)).fetchone()
    conn.close()
    return question[0]

# ajout d'une question et de ses possibleAnswers dans les tables de la base de données
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
    question_id = get_question_id_by_position(question.position)
    # création des possibleAnswers
    for answer in question.possibleAnswers :
        conn.execute('INSERT INTO possibleAnswers (text, isCorrect, questionId) VALUES (?, ?, ?)',
                         (answer["text"], answer["isCorrect"], question_id))
    conn.commit()
    conn.rollback()
    conn.close()
    return { "id" : question_id}, 200

# ajout d'une question et de ses possibleAnswers dans les tables de la base de données
def remove_question(question_id):
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # validation du token envoyé en paramètre :
    if not token :
        return 'Unauthorized', 401
    # vérifie que la question qui doit être supprimée est dans la base de données
    if len(get_question_by_id(question_id)) == 2:
        return f"Question with id {question_id} not found", 404
    # ouvre connexion à la db
    conn = db_connection()
    # suppression des réponses associées
    conn.execute('DELETE FROM possibleAnswers WHERE questionId = ?', (question_id,))
    # suppression des questions
    conn.execute('DELETE FROM questions WHERE id = ?', (question_id,))
    conn.commit()
    conn.rollback()
    return {}, 204

def remove_all_questions():
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # validation du token envoyé en paramètre :
    if not token :
        return 'Unauthorized', 401
    # ouvre connexion à la db
    conn = db_connection()
    # récupère toutes les questions de la base de données
    questions = conn.execute('SELECT * FROM questions').fetchall()
    # parcourt chaque question
    for question in questions :
        # suppression des réponses associées
        conn.execute('DELETE FROM possibleAnswers WHERE questionId = ?', (question[0],))
        # suppression des questions
        conn.execute('DELETE FROM questions WHERE id = ?', (question[0],))
    conn.commit()
    conn.rollback()
    return {}, 204


# def change_question():
#     # Récupérer le token envoyé en paramètre
#     token = request.headers.get('Authorization')
#     # validation du token envoyé en paramètre :
#     if not token :
#         return 'Unauthorized', 401
#     # récupèrer un l'objet json envoyé dans le body de la requète
#     payload = request.get_json()
#     # récupère les données :
#     question = json_to_question(payload)
#     # ouvre connexion à la db
#     conn = db_connection()
#     # création de la question
#     conn.execute('INSERT INTO questions (text, title, image, position) VALUES (?, ?, ?, ?)',
#                          (question.text, question.title, question.image, question.position))
#     conn.commit()
#     conn.rollback()
#     # récupère la question créée
#     question_id = get_question_id_by_position(question.position)
#     # création des possibleAnswers
#     for answer in question.possibleAnswers :
#         conn.execute('INSERT INTO possibleAnswers (text, isCorrect, questionId) VALUES (?, ?, ?)',
#                          (answer["text"], answer["isCorrect"], question_id))
#     conn.commit()
#     conn.rollback()
#     conn.close()
#     return { "id" : question_id}, 200