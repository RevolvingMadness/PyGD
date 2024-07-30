from ..utility.xml_helper import to_bool


class LevelColor:
    def __init__(self, level_color_json: dict) -> None:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/color-string
        self.properties = {
            1: level_color_json.get("from_color_red"),
            2: level_color_json.get("from_color_green"),
            3: level_color_json.get("from_color_blue"),
            4: level_color_json.get("player_color"),
            5: level_color_json.get("blending"),
            6: level_color_json.get("color_channel_index"),
            7: level_color_json.get("from_opacity"),
            8: level_color_json.get("toggle_opacity"),
            9: level_color_json.get("inherited_color_channel_index"),
            10: level_color_json.get("hsv"),
            11: level_color_json.get("to_color_red"),
            12: level_color_json.get("to_color_green"),
            13: level_color_json.get("to_color_blue"),
            14: level_color_json.get("delta_time"),
            15: level_color_json.get("to_opacity"),
            16: level_color_json.get("duration"),
            17: level_color_json.get("copy_opacity")
        }

    @property
    def from_color_red(self) -> int | None:
        return self.properties[1]

    @property
    def from_color_green(self) -> int | None:
        return self.properties[1]

    @property
    def from_color_blue(self) -> int | None:
        return self.properties[1]

    @property
    def player_color(self) -> int | None:
        return self.properties[1]

    @property
    def blending(self) -> bool | None:
        return to_bool(self.properties[1])

    @property
    def color_channel_index(self) -> int | None:
        return self.properties[1]

    @property
    def from_opacity(self) -> float | None:
        return self.properties[1]

    @property
    def toggle_opacity(self) -> bool | None:
        return to_bool(self.properties[1])

    @property
    def inherited_color_channel_index(self) -> int | None:
        return self.properties[1]

    @property
    def hsv(self) -> int | None:
        return self.properties[1]

    @property
    def to_color_red(self) -> int | None:
        return self.properties[1]

    @property
    def to_color_green(self) -> int | None:
        return self.properties[1]

    @property
    def to_color_blue(self) -> int | None:
        return self.properties[1]

    @property
    def delta_time(self) -> float | None:
        return self.properties[1]

    @property
    def to_opacity(self) -> float | None:
        return self.properties[1]

    @property
    def duration(self) -> float | None:
        return self.properties[1]

    @property
    def copy_opacity(self) -> bool | None:
        return to_bool(self.properties[1])

    def __repr__(self) -> str:
        return f"({self.from_color_red},{self.from_color_green},{self.from_color_blue})"

    def to_xml(self) -> str:
        result = ""

        for key, value in self.properties.items():
            if value is not None:
                result += f"{key}_{value}_"

        return result[:-1]
