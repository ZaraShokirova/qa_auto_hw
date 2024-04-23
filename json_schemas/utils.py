import json
import os


def load_schema(name):

    path = os.path.join('json_schemas', name)
    with open(path) as file:
        json_schema = json.loads(file.read())
    return json_schema
