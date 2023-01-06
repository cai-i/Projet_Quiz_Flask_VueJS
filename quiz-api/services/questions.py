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

def create_possibleAnswers(possibleAnswers, question_id, conn):
    for answer in possibleAnswers :
        conn.execute('INSERT INTO possibleAnswers (text, isCorrect, questionId) VALUES (?, ?, ?)',
                         (answer["text"], answer["isCorrect"], question_id))
        
# convertit un objet json en objet Question
def json_to_question(json_obj):
    return Question(json_obj["text"], json_obj["title"], json_obj["image"], json_obj["position"], json_obj["possibleAnswers"])

# convertit un objet Question en json avec en plus les possibleAnswers
def question_to_json(question_obj):
    json_obj = {
        "id": question_obj[0],
        "text": question_obj[2],
        "title": question_obj[1],
        "image": question_obj[3],
        "position": question_obj[4],
        "possibleAnswers": get_answers_by_questionId(question_obj[0])
    }
    return json_obj

def get_all_question() :
    conn = db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    conn.close()
    return questions

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
def get_question_id_by_position(conn, position : int) :
    question = conn.execute('SELECT id FROM questions WHERE position = ?', (position,)).fetchone()
    return question[0]

# retourne la position d'une question si son id est donnée
def get_question_position_by_id(conn, question_id : int) :
    question = conn.execute('SELECT position FROM questions WHERE id = ?', (question_id,)).fetchone()
    return question[0]

def handlePosition(conn, question_id, old_position, new_position) :

    # intervalle des questions à décaler et direction de décalage
    intervalle = ()
    direction = 0
    # position de la denrière question
    last_position = conn.execute('SELECT MAX(position) FROM questions').fetchone()[0]

    # décide des positions à décaler et de la direction de décalage :

    if old_position == -1:
        if question_id == -1: # CAS : add question
            if (not last_position) or (new_position == last_position+1) :
                return None
            intervalle = intervalle + (new_position, last_position)
            direction = 1
        else :  #-------------- CAS : delete question
            if (not last_position) or (new_position == last_position):
                return None
            intervalle = intervalle + (new_position+1, last_position)
            direction = -1
    else : # ------------------ CAS : update question
        if old_position == new_position :
            return None
        # libère l'ancienne place en se mettant en dernière position
        conn.execute('UPDATE questions SET position = ? WHERE id= ?', (last_position+1, question_id,))
        if old_position > new_position :
            intervalle = intervalle + (new_position, old_position-1)
            direction = 1
        else :
            intervalle = intervalle + (old_position+1, new_position)
            direction = -1

    # décale la position des autres questions :

    if direction == 1:
        question_need_to_change_position = conn.execute(
            'SELECT * FROM questions WHERE position BETWEEN ? and ? ORDER BY position DESC', intervalle
        ).fetchall()
    if direction == -1 :
        question_need_to_change_position = conn.execute(
            'SELECT * FROM questions WHERE position BETWEEN ? and ? ORDER BY position ASC', intervalle
        ).fetchall()

    for question in question_need_to_change_position :
        question_id = question[0]
        question_position = question_to_json(question)["position"]
        conn.execute('UPDATE questions SET position = ? WHERE id = ?', (question_position+direction, question_id,))


# ajout d'une question et de ses possibleAnswers dans les tables de la base de données
def add_question():
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # validation du token envoyé en paramètre :
    if not token :
        return 'Unauthorized', 401
    # récupèrer un l'objet json envoyé dans le body de la requête
    payload = request.get_json()
    # récupère les données :
    question = json_to_question(payload)
    # ouvre connexion à la db
    conn = db_connection()
    # prise en charge des positions
    handlePosition(conn=conn, question_id=-1, old_position=-1, new_position=question.position)
    # création de la question
    conn.execute('INSERT INTO questions (text, title, image, position) VALUES (?, ?, ?, ?)',
                         (question.text, question.title, question.image, question.position))
    conn.commit()
    conn.rollback()
    # récupère l'id de la question créée
    question_id = get_question_id_by_position(conn, question.position)
    # création des possibleAnswers
    create_possibleAnswers(question.possibleAnswers, question_id, conn)
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
    question_position = get_question_position_by_id(conn, question_id)
    # suppression des réponses associées
    conn.execute('DELETE FROM possibleAnswers WHERE questionId = ?', (question_id,))
    # suppression des questions
    conn.execute('DELETE FROM questions WHERE id = ?', (question_id,))
    # prise en charge des positions
    handlePosition(conn=conn, question_id=question_id, old_position=-1, new_position=question_position)
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
    # parcourt chaque question
    for question in get_all_question() :
        # suppression des réponses associées
        conn.execute('DELETE FROM possibleAnswers WHERE questionId = ?', (question[0],))
        # suppression des questions
        conn.execute('DELETE FROM questions WHERE id = ?', (question[0],))
    conn.commit()
    conn.rollback()
    return {}, 204


def change_question(question_id):

    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # validation du token envoyé en paramètre :
    if not token :
        return 'Unauthorized', 401
    # vérifie que la question qui doit être supprimée est dans la base de données
    old_question = get_question_by_id(question_id)
    if len(old_question) == 2:
        return f"Question with id {question_id} not found", 404
    
    # récupèrer un l'objet json envoyé dans le body de la requête
    payload = request.get_json()
    # récupère les données :
    new_question = json_to_question(payload)

    # ouvre connexion à la db
    conn = db_connection()

    # changement des positions de l'ensemble des questions 
    # entre l'ancienne et la nouvelle position si cette dernière change
    old_position = old_question["position"]
    new_position = new_question.position
    handlePosition(conn=conn, question_id= question_id, old_position=old_position, new_position=new_position)
    
    # changement de la question
    conn.execute('UPDATE questions SET text = ?, title = ?, image = ?, position = ? WHERE id = ?',
                         (new_question.text, new_question.title, new_question.image, new_position, question_id))

    # changement des possiblesAnswers (choix de tous supprimer puis recréer avec les nouvelles si les réponses changes)
    for  answer in old_question["possibleAnswers"]:
        del answer["id"]
        del answer["questionId"]
    old_possibleAnswers = old_question["possibleAnswers"]
    new_possibleAnswers = new_question.possibleAnswers
    if old_possibleAnswers != new_possibleAnswers :
        conn.execute('DELETE FROM possibleAnswers WHERE questionId = ?', (question_id, ))
        create_possibleAnswers(new_question.possibleAnswers, question_id, conn)
    
    conn.commit()
    conn.rollback()
    conn.close()
    return {}, 204