from .level_object import LevelObject


# I don't really know what to add to this class.
# I only created this because I needed an
# `pygd_encode` method.
# If any of you have ideas, open an issue.


class LevelObjects:
    def __init__(self, level_objects_list: list) -> None:
        self._list = []

        for level_object_dict in level_objects_list:
            self._list.append(LevelObject(level_object_dict))

    def delete_all_objects(self) -> None:
        self._list.clear()

    def add_object(self, level_object: LevelObject) -> None:
        self._list.append(level_object)

    def pygd_encode(self) -> str:
        result = ""

        for level_object in self._list:
            result += f"{level_object.pygd_encode()};"

        return result
