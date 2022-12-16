from flask import Flask, request
from flask_cors import CORS
from flask_expects_json import expects_json

from schema import login
from jwt_utils import build_token

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world you'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 3, "scoreEntry": [
		{
			"playerName" : "Emilie",
			"score" : 98
		},
		{
			"playerName" : "Emilie 2",
			"score" : 21
		},
		{
			"playerName" : "Emilie 3",
			"score" : 68
		}
	]}, 200

# pw = {"password" : "flask2023"}
pw = "flask2023"

@app.route('/login', methods=['POST'])
@expects_json(login)
def verify_admin_pw():
	payload = request.get_json()
	if payload["password"] == pw :
		token = build_token()
		return { "token" : token }
	else : 
		return 'Unauthorized', 401

# @app.route('/questions', methods=['POST'])


if __name__ == "__main__":
    app.run()