from ..utility.type_converter import to_bool, to_int


class LevelColor:
    def __init__(self, level_color_json: dict) -> None:
        self._json = level_color_json

    @property
    def from_color_red(self) -> int:
        return to_int(self._json.get("1"))

    @property
    def from_color_green(self) -> int:
        return to_int(self._json.get("2"))

    @property
    def from_color_blue(self) -> int:
        return to_int(self._json.get("3"))

    @property
    def player_color(self) -> int:
        return to_int(self._json.get("4"))

    @property
    def blending(self) -> bool:
        return to_bool(self._json.get("5"))

    @property
    def color_channel_index(self) -> int:
        return to_int(self._json.get("6"))

    @property
    def from_opacity(self) -> float:
        return self._json.get("7")

    @property
    def toggle_opacity(self) -> bool:
        return to_bool(self._json.get("8"))

    @property
    def inherited_color_channel_index(self) -> int:
        return to_int(self._json.get("9"))

    @property
    def hsv(self) -> int:
        return to_int(self._json.get("10"))

    @property
    def to_color_red(self) -> int:
        return to_int(self._json.get("11"))

    @property
    def to_color_green(self) -> int:
        return to_int(self._json.get("12"))

    @property
    def to_color_blue(self) -> int:
        return to_int(self._json.get("13"))

    @property
    def delta_time(self) -> float:
        return self._json.get("14")

    @property
    def to_opacity(self) -> float:
        return self._json.get("15")

    @property
    def duration(self) -> float:
        return self._json.get("16")

    @property
    def copy_opacity(self) -> bool:
        return to_bool(self._json.get("17"))

    @from_color_red.setter
    def from_color_red(self, value: int) -> None:
        self._json["1"] = value

    @from_color_green.setter
    def from_color_green(self, value: int) -> None:
        self._json["2"] = value

    @from_color_blue.setter
    def from_color_blue(self, value: int) -> None:
        self._json["3"] = value

    @player_color.setter
    def player_color(self, value: int) -> None:
        self._json["4"] = value

    @blending.setter
    def blending(self, value: bool) -> None:
        self._json["5"] = value

    @color_channel_index.setter
    def color_channel_index(self, value: int) -> None:
        self._json["6"] = value

    @from_opacity.setter
    def from_opacity(self, value: float) -> None:
        self._json["7"] = value

    @toggle_opacity.setter
    def toggle_opacity(self, value: bool) -> None:
        self._json["8"] = value

    @inherited_color_channel_index.setter
    def inherited_color_channel_index(self, value: int) -> None:
        self._json["9"] = value

    @hsv.setter
    def hsv(self, value: int) -> None:
        self._json["10"] = value

    @to_color_red.setter
    def to_color_red(self, value: int) -> None:
        self._json["11"] = value

    @to_color_green.setter
    def to_color_green(self, value: int) -> None:
        self._json["12"] = value

    @to_color_blue.setter
    def to_color_blue(self, value: int) -> None:
        self._json["13"] = value

    @delta_time.setter
    def delta_time(self, value: float) -> None:
        self._json["14"] = value

    @to_opacity.setter
    def to_opacity(self, value: float) -> None:
        self._json["15"] = value

    @duration.setter
    def duration(self, value: float) -> None:
        self._json["16"] = value

    @copy_opacity.setter
    def copy_opacity(self, value: bool) -> None:
        self._json["17"] = value

    def __repr__(self) -> str:
        return f"({self.from_color_red},{self.from_color_green},{self.from_color_blue})"

    def pygd_encode(self) -> str:
        result = ""

        for key, value in self._json.items():
            result += f"{key}_{value.pygd_encode()}_"

        return result[:-1]
