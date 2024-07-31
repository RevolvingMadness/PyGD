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

    def __repr__(self) -> str:
        return f"({self.from_color_red},{self.from_color_green},{self.from_color_blue})"
