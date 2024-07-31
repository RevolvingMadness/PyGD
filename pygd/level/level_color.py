from ..utility.type_converter import to_bool, to_int


class LevelColor:
    def __init__(self, level_color_json: dict) -> None:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/color-string
        self.properties = {
            "1": level_color_json.get("1"),  # from_color_red
            "2": level_color_json.get("2"),  # from_color_green
            "3": level_color_json.get("3"),  # from_color_blue
            "4": level_color_json.get("4"),  # player_color
            "5": level_color_json.get("5"),  # blending
            "6": level_color_json.get("6"),  # color_channel_index
            "7": level_color_json.get("7"),  # from_opacity
            "8": level_color_json.get("8"),  # toggle_opacity
            "9": level_color_json.get("9"),  # inherited_color_channel_index
            "10": level_color_json.get("10"),  # hsv
            "11": level_color_json.get("11"),  # to_color_red
            "12": level_color_json.get("12"),  # to_color_green
            "13": level_color_json.get("13"),  # to_color_blue
            "14": level_color_json.get("14"),  # delta_time
            "15": level_color_json.get("15"),  # to_opacity
            "16": level_color_json.get("16"),  # duration
            "17": level_color_json.get("17")  # copy_opacity
        }

    @property
    def from_color_red(self) -> int:
        return to_int(self.properties["1"])

    @property
    def from_color_green(self) -> int:
        return to_int(self.properties["2"])

    @property
    def from_color_blue(self) -> int:
        return to_int(self.properties["3"])

    @property
    def player_color(self) -> int:
        return to_int(self.properties["4"])

    @property
    def blending(self) -> bool:
        return to_bool(self.properties["5"])

    @property
    def color_channel_index(self) -> int:
        return to_int(self.properties["6"])

    @property
    def from_opacity(self) -> float:
        return self.properties["7"]

    @property
    def toggle_opacity(self) -> bool:
        return to_bool(self.properties["8"])

    @property
    def inherited_color_channel_index(self) -> int:
        return to_int(self.properties["9"])

    @property
    def hsv(self) -> int:
        return to_int(self.properties["10"])

    @property
    def to_color_red(self) -> int:
        return to_int(self.properties["11"])

    @property
    def to_color_green(self) -> int:
        return to_int(self.properties["12"])

    @property
    def to_color_blue(self) -> int:
        return to_int(self.properties["13"])

    @property
    def delta_time(self) -> float:
        return self.properties["14"]

    @property
    def to_opacity(self) -> float:
        return self.properties["15"]

    @property
    def duration(self) -> float:
        return self.properties["16"]

    @property
    def copy_opacity(self) -> bool:
        return to_bool(self.properties["17"])

    def __repr__(self) -> str:
        return f"({self.from_color_red},{self.from_color_green},{self.from_color_blue})"

    @staticmethod
    def decode_color_string(encoded_color_string: str) -> list["LevelColor"]:
        split_encoded_color_string = encoded_color_string.split("|")[:-1]
        result = []

        key = None

        for color_string in split_encoded_color_string:
            color_string_split = color_string.split("_")

            color = {}

            for color_property in color_string_split:
                if key is None:
                    key = color_property
                else:
                    if key is None:
                        raise Exception("Level Colors are in the incorrect format.")

                    color[key] = color_property
                    key = None

            result.append(LevelColor(color))

        return result
