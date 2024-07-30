class LevelColor:
    def __init__(self, level_color_json: dict) -> None:
        self.from_color_red = level_color_json.get("from_color_red", None)
        self.from_color_green = level_color_json.get("from_color_green", None)
        self.from_color_blue = level_color_json.get("from_color_blue", None)
        self.player_color = level_color_json.get("player_color", None)
        self.blending = level_color_json.get("blending", None)
        self.color_channel_index = level_color_json.get("color_channel_index", None)
        self.from_opacity = level_color_json.get("from_opacity", None)
        self.toggle_opacity = level_color_json.get("toggle_opacity", None)
        self.inherited_color_channel_index = level_color_json.get("inherited_color_channel_index", None)
        self.hsv = level_color_json.get("hsv", None)
        self.to_color_red = level_color_json.get("to_color_red", None)
        self.to_color_green = level_color_json.get("to_color_green", None)
        self.to_color_blue = level_color_json.get("to_color_blue", None)
        self.delta_time = level_color_json.get("delta_time", None)
        self.to_opacity = level_color_json.get("to_opacity", None)
        self.duration = level_color_json.get("duration", None)
        self.copy_opacity = level_color_json.get("copy_opacity", None)

    def __repr__(self) -> str:
        return f"({self.from_color_red},{self.from_color_green},{self.from_color_blue})"
