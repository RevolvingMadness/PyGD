from .level_start_object import *


class LevelData:
    def __init__(self, level_data_json: dict) -> None:
        self.level_start_object = LevelStartObject(level_data_json["level_start_object"])
        self.objects = level_data_json["objects"]
