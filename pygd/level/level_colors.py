from .level_color import LevelColor


# TODO
# Add functionality to get the following:
# background color
# ground / ground 2 color
# line color
# middleground / middleground 2 color
# color channel


class LevelColors:
    def __init__(self, level_colors_list: list) -> None:
        self._list = []

        for color_dict in level_colors_list:
            self._list.append(LevelColor(color_dict))

    def pygd_encode(self) -> str:
        result = ""

        for color in self._list:
            result += f"{color.pygd_encode()}|"

        return result
