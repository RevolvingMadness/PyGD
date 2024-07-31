from .level import Level


class Levels:
    def __init__(self, levels_json: dict) -> None:
        del levels_json["_isArr"]

        self.levels = {}

        for key, value in levels_json.items():
            level = Level(value)
            level._key = key

            self.levels[level.name] = level

    def get(self, name: str) -> Level:
        return self.levels.get(name)

    def delete(self, name: str) -> Level:
        return self.levels.pop(name)
