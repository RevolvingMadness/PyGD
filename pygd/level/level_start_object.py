from .level_color import LevelColor


class LevelStartObject:
    def __init__(self, level_start_object_json: dict) -> None:
        self.audio_track = level_start_object_json.get("audio_track")
        self.gamemode = level_start_object_json.get("gamemode")
        self.mini = level_start_object_json.get("mini")
        self.speed = level_start_object_json.get("speed")
        self.background_texture_id = level_start_object_json.get("background_texture_id")
        self.ground_texture_id = level_start_object_json.get("ground_texture_id")
        self.dual_mode = level_start_object_json.get("dual_mode")
        self.is_start_pos_object = level_start_object_json.get("is_start_pos_object")
        self.two_player_mode = level_start_object_json.get("two_player_mode")
        self.flip_gravity = level_start_object_json.get("flip_gravity")
        self.song_offset = level_start_object_json.get("song_offset")
        self.guidelines = level_start_object_json.get("guidelines")
        self.fade_in = level_start_object_json.get("fade_in")
        self.fade_out = level_start_object_json.get("fade_out")
        self.ground_line = level_start_object_json.get("ground_line")
        self.font = level_start_object_json.get("font")
        self.target_order = level_start_object_json.get("target_order")
        self.reverse_gameplay = level_start_object_json.get("reverse_gameplay")
        self.disable = level_start_object_json.get("disable")
        self.platformer_mode = level_start_object_json.get("platformer_mode")
        self.middleground_texture_id = level_start_object_json.get("middleground_texture_id")
        self.target_channel = level_start_object_json.get("target_channel")
        self.allow_multi_rotation = level_start_object_json.get("allow_multi_rotation")
        self.mirror_mode = level_start_object_json.get("mirror_mode")
        self.rotate_gameplay = level_start_object_json.get("rotate_gameplay")
        self.enable_player_squeeze = level_start_object_json.get("enable_player_squeeze")
        self.fix_gravity_bug = level_start_object_json.get("fix_gravity_bug")
        self.fix_negative_scale = level_start_object_json.get("fix_negative_scale")
        self.fix_robot_jump = level_start_object_json.get("fix_robot_jump")
        self.reset_camera = level_start_object_json.get("reset_camera")
        self.spawn_group = level_start_object_json.get("spawn_group")
        self.dynamic_level_height = level_start_object_json.get("dynamic_level_height")
        self.sort_groups = level_start_object_json.get("sort_groups")
        self.fix_radius_collision = level_start_object_json.get("fix_radius_collision")
        self.enable_two_point_two_changes = level_start_object_json.get("enable_two_point_two_changes")
        self.allow_static_rotate = level_start_object_json.get("allow_static_rotate")
        self.reverse_sync = level_start_object_json.get("reverse_sync")
        self.no_time_penalty = level_start_object_json.get("no_time_penalty")
        self.decrease_boost_slide = level_start_object_json.get("decrease_boost_slide")

        self.colors = level_start_object_json.get("colors")
        if self.colors is not None:
            result = []

            for color in self.colors:
                result.append(LevelColor(color))

            self.colors = result

        self.color_page = level_start_object_json.get("color_page")
