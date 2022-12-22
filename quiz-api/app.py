from flask import Flask, request
from flask_cors import CORS
from flask_expects_json import expects_json

from schema import login, question

from services.admin import verify_admin_pw
from services.Questions_Answers import add_question, get_question_by_id, get_question_by_position, remove_question, remove_all_questions, change_question
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

# exemple de json qui peut être retourné à l'url : /quiz-info
json_ex = {
			"scores": [
				{
					"date": "18/04/2022 11:57:48",
					"playerName": "Emil",
					"score": 10
				},
				{
					"date": "18/04/2022 11:57:48",
					"playerName": "Dora",
					"score": 8
				},
				{
					"date": "18/04/2022 11:57:49",
					"playerName": "Gustav",
					"score": 7
				}
			],
			"size": 10
		}

@app.route('/quiz-info', methods=['GET'])
def get_quiz_info():
	return {"size": 0, "scores": []}, 200

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
def update_question(question_id):
	return change_question(question_id)

if __name__ == "__main__":
    app.run()