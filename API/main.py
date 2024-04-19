import json
import string
import random

def generate_random_sequence() -> str:
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(12))


def load_data(filename: str, target_dict: dict) -> None:
    with open(f"ru/{filename}.json", "r", encoding="utf8") as f:
        data_dict: dict = json.load(f)
    for level in data_dict:
        for k, v in data_dict[level].items():
            q = v.replace("\n", "")
            if "q" in k:
                pass
                print(f"Value [{q}] is passed per request.")
            else:
                key = generate_random_sequence()
                target_dict[key] = q
                print(f"Value {q} successfully written!")

def write_data_to_json(source_dict: dict, target_file: str) -> None:
    with open(f"data/{target_file}", "w", encoding="utf8") as f:
        json.dump(source_dict, f, ensure_ascii=False, indent=4)
        print(f"\n{target_file} successfully written!")

tdata: dict = {}
ddata: dict = {}
ndata: dict = {}

load_data("truth", tdata)
load_data("dare", ddata)
load_data("never", ndata)

write_data_to_json(tdata, "gTruth.json")
write_data_to_json(ddata, "gDare.json")
write_data_to_json(ndata, "gNever.json")

"""I am developing an app, where people would be able to play Truth and Dare game, but note, that it is a Christian content. I am asking you to generate unique truth questions. Let's start from 20.  Data must be in a json format, where key is random 12 uppercase chanracters data, and the value is the generated question itself."""

