import sqlite3

def init_db(): 
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

    # exécute des instructions sql :

    # cur.execute('INSERT INTO questions (text, title, image, position) VALUES (?, ?, ?, ?)',
    #                          (question.text, question.title, question.image, question.position)
    #             )

    # valide les modification
    connection.commit()
    # ferme la connexion
    connection.close()
    return  "Ok", 200