from flask import request

from .questions import db_connection, get_all_question, get_question_id_by_position

def quiz_info():
	nb_question = len(get_all_question())
	# recupère les scores des participants
	conn = db_connection()
	participants_scores = conn.execute('SELECT date, player_name, score FROM participants ORDER BY score DESC').fetchall()
	conn.close()
	scores = []
	for score in participants_scores:
		scores.append({
			"date": score[0],
			"playerName": score[1],
			"score" : score[2]
		})
	return {"size": nb_question, "scores": scores}

def submit_answers() :
	payload = request.get_json()
	# récupère les réponses du participant
	answers = payload["answers"]
	# vérifie que le nombre de réponse est bon :
	if len(get_all_question()) > len(answers):
		return "You did not answer all the questions", 400
	if len(get_all_question()) < len(answers):
		return "Too much answers for the quantity of question", 400
	# crée la liste d'objet answerSummary
	answersSummaries = []
	position = 1
	score = 0
	for answer in answers :
		# recupère la position de la bonne réponse :
		conn = db_connection()
		question_answers= conn.execute('SELECT isCorrect FROM possibleAnswers WHERE questionId = ?', (get_question_id_by_position(conn, position),)).fetchall()
		conn.close()
		correctAnswerPosition = [a[0] for a in question_answers].index(1)+1
		# ajoute un point si la réponse est correct
		if correctAnswerPosition == answer:
			score +=1
		# ajoute le tout dans la liste
		answersSummaries.append({
			"correctAnswerPosition" : correctAnswerPosition, 
			"wasCorrect" : answer
		})
		#incrémente pour avoir la même chose pour la prochaine question
		position+=1
	response = {
		"answersSummaries" : answersSummaries,
		"playerName" : payload["playerName"],
		"score" : score
	}
	# ajoute le participant à la table des participants
	add_participant(payload["playerName"], score)
	return response

def add_participant(playerName, score):
	conn = db_connection()
	conn.execute('INSERT INTO participants (player_name, score) VALUES (?, ?)',
                         (playerName, score))
	conn.commit()
	conn.rollback()
	conn.close()

def remove_all_participants():
	# Récupérer le token envoyé en paramètre
	token = request.headers.get('Authorization')
	# validation du token envoyé en paramètre :
	if not token :
		return 'Unauthorized', 401
	# suppresion des éléments de la table participants
	conn = db_connection()
	conn.execute('DELETE FROM participants')
	conn.commit()
	conn.rollback()
	conn.close()
	return {}, 204