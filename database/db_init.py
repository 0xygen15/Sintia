import os
import sqlite3
import json

connection = sqlite3.connect("db.db")
c = connection.cursor()

def get_data(file):
    with open(file, 'r', encoding='utf8') as f:
        jsondata = json.load(f)
    return {"fileName": os.path.basename(f.name), "jsondata": jsondata}

def fillDB(file):
    fileName = get_data(file).get("fileName").split(sep=".")[0]
    data = get_data(file).get('jsondata')
    levels = [key for key, value in get_data(file).get('jsondata').items()]

    createTable = """CREATE TABLE ? (
    number INTEGER PRIMARY KEY,
    question CHAR,
    level CHAR);"""
    c.execute(createTable, fileName)

    def insert_data(level):
        for key, question in data.get(level).items():
            insertData = """INSERT INTO ? VALUES (?, ?);"""
            c.execute(insertData, (fileName, question, level))

    for level in levels:
        insert_data(level)

    connection.commit()
    connection.close()

fileList = [i for i in os.listdir(r"C:\Users\QA\PycharmProjects\TORD4\database")]

for file in fileList:
    path = file
    fillDB(file)
