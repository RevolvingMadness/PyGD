from .level_color import LevelColor


class LevelColors:
    def __init__(self, level_colors_list: list) -> None:
        self._list = []

        for color_dict in level_colors_list:
            self._list.append(LevelColor(color_dict))

    def add_color(self, color: LevelColor) -> None:
        self._list.append(color)

    def get_color(self, color_channel: int) -> LevelColor:
        for color in self._list:
            if color.color_channel_index == color_channel:
                return color

    def pygd_encode(self) -> str:
        result = ""

        for color in self._list:
            result += f"{color.pygd_encode()}|"

        return result
