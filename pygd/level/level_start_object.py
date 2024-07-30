from .level_color import LevelColor


class LevelStartObject:
    def __init__(self, level_start_object_json: dict) -> None:
        self.audio_track = level_start_object_json.get("audio_track", None)
        self.gamemode = level_start_object_json.get("gamemode", None)
        self.mini = level_start_object_json.get("mini", None)
        self.speed = level_start_object_json.get("speed", None)
        self.background_texture_id = level_start_object_json.get("background_texture_id", None)
        self.ground_texture_id = level_start_object_json.get("ground_texture_id", None)
        self.dual_mode = level_start_object_json.get("dual_mode", None)
        self.is_start_pos_object = level_start_object_json.get("is_start_pos_object", None)
        self.two_player_mode = level_start_object_json.get("two_player_mode", None)
        self.flip_gravity = level_start_object_json.get("flip_gravity", None)
        self.song_offset = level_start_object_json.get("song_offset", None)
        self.guidelines = level_start_object_json.get("guidelines", None)
        self.fade_in = level_start_object_json.get("fade_in", None)
        self.fade_out = level_start_object_json.get("fade_out", None)
        self.ground_line = level_start_object_json.get("ground_line", None)
        self.font = level_start_object_json.get("font", None)
        self.target_order = level_start_object_json.get("target_order", None)
        self.reverse_gameplay = level_start_object_json.get("reverse_gameplay", None)
        self.disable = level_start_object_json.get("disable", None)
        self.platformer_mode = level_start_object_json.get("platformer_mode", None)
        self.middleground_texture_id = level_start_object_json.get("middleground_texture_id", None)
        self.target_channel = level_start_object_json.get("target_channel", None)
        self.allow_multi_rotation = level_start_object_json.get("allow_multi_rotation", None)
        self.mirror_mode = level_start_object_json.get("mirror_mode", None)
        self.rotate_gameplay = level_start_object_json.get("rotate_gameplay", None)
        self.enable_player_squeeze = level_start_object_json.get("enable_player_squeeze", None)
        self.fix_gravity_bug = level_start_object_json.get("fix_gravity_bug", None)
        self.fix_negative_scale = level_start_object_json.get("fix_negative_scale", None)
        self.fix_robot_jump = level_start_object_json.get("fix_robot_jump", None)
        self.reset_camera = level_start_object_json.get("reset_camera", None)
        self.spawn_group = level_start_object_json.get("spawn_group", None)
        self.dynamic_level_height = level_start_object_json.get("dynamic_level_height", None)
        self.sort_groups = level_start_object_json.get("sort_groups", None)
        self.fix_radius_collision = level_start_object_json.get("fix_radius_collision", None)
        self.enable_two_point_two_changes = level_start_object_json.get("enable_two_point_two_changes", None)
        self.allow_static_rotate = level_start_object_json.get("allow_static_rotate", None)
        self.reverse_sync = level_start_object_json.get("reverse_sync", None)
        self.no_time_penalty = level_start_object_json.get("no_time_penalty", None)
        self.decrease_boost_slide = level_start_object_json.get("decrease_boost_slide", None)

        self.colors = level_start_object_json.get("colors", None)
        if self.colors is not None:
            result = []

            for color in self.colors:
                result.append(LevelColor(color))

            self.colors = result
            
        self.color_page = level_start_object_json.get("color_page", None)
