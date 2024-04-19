from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import json

uri = "mongodb+srv://felix:example@maincluster.z9ibsco.mongodb.net/?retryWrites=true&w=majority&appName=maincluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["apidata"]

truth = mydb["truth"]
dare = mydb["dare"]
never = mydb["never"]
truth_themes = mydb["truth_themes"]

truth_list: list = [str]
dare_list: list = [str]
never_list: list = [str]
themes_truth_list: dict = {str:list}

def data():
    global truth_list, dare_list, never_list

    def load_data(filename: str, target_list: list):
        with open(f"ru/{filename}.json", "r", encoding="utf8") as f:
            data_dict: dict = json.load(f)
        for level in data_dict:
            for k, v in data_dict[level].items():
                q = v.replace("\n", "")
                target_list.append(q)

    load_data("truth", truth_list)
    load_data("dare", dare_list)
    load_data("never", never_list)

def themes_data():
    global themes_truth_list
    with open(f"../database/ru/themes_truth.json", "r", encoding="utf8") as f:
        data_dict: dict = json.load(f)
    for level in data_dict:
        target_list:list  = [str]
        for k, v in data_dict[level].items():
            target_list.append(v)
        themes_truth_list[level] = target_list

data()

for q in truth_list:
    my_dict = {"q": q}
    x = truth.insert_one(my_dict)

for q in dare_list:
    my_dict = {"q": q}
    x = dare.insert_one(my_dict)

for q in never_list:
    my_dict = {"q": q}
    x = never.insert_one(my_dict)

themes_data()

for k, v in themes_truth_list.items():
    my_dict = {k, v}
    x = truth_themes.insert_one(my_dict)

for x in truth.find({}, {"q": 1}):
    print(x)