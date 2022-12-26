from flask import Flask, request
from flask_cors import CORS
from flask_expects_json import expects_json

from schema import login, question, participation

from services.admin import verify_admin_pw
from services.questions import add_question, get_question_by_id, get_question_by_position, remove_question, remove_all_questions, change_question
from services.quiz_participants import quiz_info, submit_answers, remove_all_participants
from db.init_db import init_db

# instance d'application Flask 
app = Flask(__name__)
	#__name__ : nom du module Python actuel
		#indique à l'instance où il se trouve
CORS(app)

# @app.routeest un décorateur 
	# qui transforme une fonction Python standard 
	# en une fonction d'affichage Flask
	# qui convertit la valeur de retour de la fonction 
	# en une réponse HTTP à afficher par un client HTTP (ex : navigateur web)
@app.route('/')
def hello_world():
	x = 'you'
	return f"Hello, {x}"

@app.route('/rebuild-db', methods=['POST'])
def create_db():
	return init_db()

@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
	return quiz_info()

@app.route('/login', methods=['POST'])
@expects_json(login)
def verify_pw():
	return verify_admin_pw()

@app.route('/questions/<question_id>', methods=['GET'])
def get_question_given_id(question_id):
	return get_question_by_id(question_id)

@app.route('/questions', methods=['GET'])
def get_question_given_position():
	position = request.args.get('position')
	return get_question_by_position(position)

@app.route('/questions', methods=['POST'])
@expects_json(question)
def create_question():
	return add_question()

@app.route('/questions/<question_id>', methods=['DELETE'])
def delete_question(question_id):
	return remove_question(question_id)

@app.route('/questions/all', methods=['DELETE'])
def delete_all_questions():
	return remove_all_questions()

@app.route('/questions/<question_id>', methods=['PUT'])
@expects_json(question)
def update_question(question_id):
	return change_question(question_id)

@app.route('/participations', methods=['POST'])
@expects_json(participation)
def submit_participant_answers():
	return submit_answers()

@app.route('/participations/all', methods=['DELETE'])
def delete_all_participants():
	return remove_all_participants()

if __name__ == "__main__":
    app.run()