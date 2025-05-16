import json
import os

def read_json(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as file:
        return json.load(file)

def write_json(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
