from .level_start_object import *
from .object import Object


class LevelData:
    def __init__(self, level_data_json: dict) -> None:
        self.level_start_object = LevelStartObject(level_data_json["level_start_object"])

        self.objects = []
        for level_object in level_data_json["objects"]:
            self.objects.append(Object.from_json(level_object))
