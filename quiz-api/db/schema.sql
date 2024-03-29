DROP TABLE IF EXISTS questions;

CREATE TABLE questions(
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "text" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "position" INTEGER NOT NULL UNIQUE
);

DROP TABLE IF EXISTS possibleAnswers;

CREATE TABLE possibleAnswers (
    "id" INTEGER NOT NULL UNIQUE,
    "text" TEXT NOT NULL,
    "isCorrect" INTEGER NOT NULL,
    "questionId" INTEGER NOT NULL,
    FOREIGN KEY("questionId") REFERENCES questions("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS participants;

CREATE TABLE participants (
    "id" INTEGER NOT NULL UNIQUE,
    "player_name" TEXT NOT NULL,
    "score" INTEGER NOT NULL,
    "reussite" INTEGER NOT NULL,
    "date" TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
	PRIMARY KEY("id" AUTOINCREMENT)
);