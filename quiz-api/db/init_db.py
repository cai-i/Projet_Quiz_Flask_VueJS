import sqlite3

# create a connection to a db file named database.db
    # file will be created when execute this file
connection = sqlite3.connect('db/database.db')

# pr ouvrir le fichier "schema.sql"
with open("db/schema.sql") as f:
    connection.executescript(f.read())
    # exécute contenu du fichier
    # créera notre table questions

# crée objet Cursor : 
# permet de traiter des lignes dans une base de données
cur = connection.cursor()

# valide les modification
connection.commit()
# ferme la connexion
connection.close()