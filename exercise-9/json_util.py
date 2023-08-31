import json
from typing import Type

@staticmethod
def from_json_string(json_string: str, class_name: Type) -> object:
    json_data = json.loads(json_string)

    def convert_to_class(d):
        return class_name(**d)

    return convert_to_class(json_data)


@staticmethod
def json_to_dict(json_data):
    return json.loads(json_data)