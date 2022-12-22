from flask import request

from .jwt_utils import build_token

# le bon mdp
pw = "flask2023"

def verify_admin_pw() :
    payload = request.get_json() 
            # recup json ds body de la requête
    if payload["password"] == pw :
        token = build_token()
        return { "token" : token }
    else : 
        return 'Unauthorized', 401