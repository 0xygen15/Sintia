import sqlite3
import json

connection = sqlite3.connect("db.db")
c = connection.cursor()

def get_data(file):
    with open(file, 'r', encoding='utf8') as f:
        jsondata = json.load(f)
    return jsondata

def create_and_fill_never(file):
    data = get_data(file)
    levels = [key for key, value in get_data(file).items()]

    createTable = """CREATE TABLE NEVER (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR(255) NOT NULL,
    level VARCHAR(16) NOT NULL
    );"""
    c.execute(createTable)

    def insert_data(level):
        for key, question in data.get(level).items():
            insertData = """INSERT INTO NEVER (question, level) VALUES (?, ?);"""
            c.execute(insertData, (question, level))

    for level in levels:
        insert_data(level)

    connection.commit()

def create_and_fill_dare(file):
    data = get_data(file)
    levels = [key for key, value in get_data(file).items()]

    createTable = """CREATE TABLE DARE (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR(255) NOT NULL,
    level VARCHAR(16) NOT NULL
    );"""
    c.execute(createTable)

    def insert_data(level):
        for key, question in data.get(level).items():
            insertData = """INSERT INTO DARE (question, level) VALUES (?, ?);"""
            c.execute(insertData, (question, level))

    for level in levels:
        insert_data(level)

    connection.commit()

def create_and_fill_truth(file):
    data = get_data(file)
    levels = [key for key, value in get_data(file).items()]

    createTable = """CREATE TABLE TRUTH (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR(255) NOT NULL,
    level VARCHAR(16) NOT NULL
    );"""
    c.execute(createTable)

    def insert_data(level):
        for key, question in data.get(level).items():
            insertData = """INSERT INTO TRUTH (question, level) VALUES (?, ?);"""
            c.execute(insertData, (question, level))

    for level in levels:
        insert_data(level)

    connection.commit()

create_and_fill_never("../database/never.json")
create_and_fill_truth("../database/truth.json")
create_and_fill_dare("../database/dare.json")

connection.close()
