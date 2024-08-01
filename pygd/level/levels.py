from .level import Level


class Levels:
    def __init__(self, levels_json: dict) -> None:
        if "_isArr" in levels_json:
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

    def pygd_encode(self) -> dict:
        result = {}

        current_level = 0

        for key, value in self.levels.items():
            result[f"k_{current_level}"] = value.pygd_encode()

            current_level += 1

        return result
