from .level_colors import LevelColors
from ..utility.string_helper import decode_colors_string
from ..utility.type_converter import to_bool, to_int


class LevelStartObject:
    def __init__(self, level_start_object_json: dict) -> None:
        self._json = level_start_object_json

        colors = self._json.get("kS38")
        if colors is not None:
            self._json["kS38"] = LevelColors(decode_colors_string(colors))

    @property
    def audio_track(self) -> int:
        return to_int(self._json.get("kA1"))

    @property
    def gamemode(self) -> int:
        return to_int(self._json.get("kA2"))

    @property
    def mini(self) -> bool:
        return to_bool(self._json.get("kA3"))

    @property
    def speed(self) -> int:
        return to_int(self._json.get("kA4"))

    @property
    def object_two_blending(self) -> bool:
        return to_bool(self._json.get("kA5"))

    @property
    def background_texture_id(self) -> int:
        return to_int(self._json.get("kA6"))

    @property
    def ground_texture_id(self) -> int:
        return to_int(self._json.get("kA7"))

    @property
    def is_dual_mode(self) -> bool:
        return to_bool(self._json.get("kA8"))

    @property
    def is_start_pos_object(self) -> bool:
        return to_bool(self._json.get("kA9"))

    @property
    def is_two_player_mode(self) -> bool:
        return to_bool(self._json.get("kA10"))

    @property
    def flip_gravity(self) -> bool:
        return to_bool(self._json.get("kA11"))

    @property
    def color_three_blending(self) -> bool:
        return to_bool(self._json.get("kA12"))

    @property
    def song_offset(self) -> float:
        return self._json.get("kA13")

    @property
    def guidelines(self) -> str:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/guideline-string
        return self._json.get("kA14")

    @property
    def fade_in(self) -> bool:
        return to_bool(self._json.get("kA15"))

    @property
    def fade_out(self) -> bool:
        return to_bool(self._json.get("kA16"))

    @property
    def ground_line(self) -> int:
        return to_int(self._json.get("kA17"))

    @property
    def font(self) -> int:
        return to_int(self._json.get("kA18"))

    @property
    def target_order(self) -> int:
        return to_int(self._json.get("kA19"))

    @property
    def reverse_gameplay(self) -> bool:
        return to_bool(self._json.get("kA20"))

    @property
    def is_disabled(self) -> bool:
        return to_bool(self._json.get("kA21"))

    @property
    def platformer_mode(self) -> bool:
        return to_bool(self._json.get("kA22"))

    @property
    def middleground_texture_id(self) -> int:
        return to_int(self._json.get("kA25"))

    @property
    def target_channel(self) -> int:
        return to_int(self._json.get("kA26"))

    @property
    def allow_multi_rotation(self) -> bool:
        return to_bool(self._json.get("kA27"))

    @property
    def mirror_mode(self) -> bool:
        return to_bool(self._json.get("kA28"))

    @property
    def rotate_gameplay(self) -> bool:
        return to_bool(self._json.get("kA29"))

    @property
    def enable_player_squeeze(self) -> bool:
        return to_bool(self._json.get("kA31"))

    @property
    def fix_gravity_bug(self) -> bool:
        return to_bool(self._json.get("kA32"))

    @property
    def fix_negative_scale(self) -> bool:
        return to_bool(self._json.get("kA33"))

    @property
    def fix_robot_jump(self) -> bool:
        return to_bool(self._json.get("kA34"))

    @property
    def reset_camera(self) -> bool:
        return to_bool(self._json.get("kA35"))

    @property
    def spawn_group(self) -> int:
        return to_int(self._json.get("kA36"))

    @property
    def dynamic_level_height(self) -> bool:
        return to_bool(self._json.get("kA37"))

    @property
    def sort_groups(self) -> bool:
        return to_bool(self._json.get("kA38"))

    @property
    def fix_radius_collision(self) -> bool:
        return to_bool(self._json.get("kA39"))

    @property
    def enable_two_point_two_changes(self) -> bool:
        return to_bool(self._json.get("kA40"))

    @property
    def allow_static_rotate(self) -> bool:
        return to_bool(self._json.get("kA41"))

    @property
    def reverse_sync(self) -> bool:
        return to_bool(self._json.get("kA42"))

    @property
    def no_time_penalty(self) -> bool:
        return to_bool(self._json.get("kA43"))

    @property
    def decrease_boost_slide(self) -> bool:
        return to_bool(self._json.get("kA45"))

    @property
    def colors(self) -> LevelColors:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/color-string
        return self._json.get("kS38")

    @property
    def color_page(self) -> int:
        return to_int(self._json.get("kS39"))

    @audio_track.setter
    def audio_track(self, value: int) -> None:
        self._json["kA1"] = value

    @gamemode.setter
    def gamemode(self, value: int) -> None:
        self._json["kA2"] = value

    @mini.setter
    def mini(self, value: bool) -> None:
        self._json["kA3"] = value

    @speed.setter
    def speed(self, value: int) -> None:
        self._json["kA4"] = value

    @object_two_blending.setter
    def object_two_blending(self, value: bool) -> None:
        self._json["kA5"] = value

    @background_texture_id.setter
    def background_texture_id(self, value: int) -> None:
        self._json["kA6"] = value

    @ground_texture_id.setter
    def ground_texture_id(self, value: int) -> None:
        self._json["kA7"] = value

    @is_dual_mode.setter
    def is_dual_mode(self, value: bool) -> None:
        self._json["kA8"] = value

    @is_start_pos_object.setter
    def is_start_pos_object(self, value: bool) -> None:
        self._json["kA9"] = value

    @is_two_player_mode.setter
    def is_two_player_mode(self, value: bool) -> None:
        self._json["kA10"] = value

    @flip_gravity.setter
    def flip_gravity(self, value: bool) -> None:
        self._json["kA11"] = value

    @color_three_blending.setter
    def color_three_blending(self, value: bool) -> None:
        self._json["kA12"] = value

    @song_offset.setter
    def song_offset(self, value: float) -> None:
        self._json["kA13"] = value

    @guidelines.setter
    def guidelines(self, value: str) -> None:
        self._json["kA14"] = value

    @fade_in.setter
    def fade_in(self, value: bool) -> None:
        self._json["kA15"] = value

    @fade_out.setter
    def fade_out(self, value: bool) -> None:
        self._json["kA16"] = value

    @ground_line.setter
    def ground_line(self, value: int) -> None:
        self._json["kA17"] = value

    @font.setter
    def font(self, value: int) -> None:
        self._json["kA18"] = value

    @target_order.setter
    def target_order(self, value: int) -> None:
        self._json["kA19"] = value

    @reverse_gameplay.setter
    def reverse_gameplay(self, value: bool) -> None:
        self._json["kA20"] = value

    @is_disabled.setter
    def is_disabled(self, value: bool) -> None:
        self._json["kA21"] = value

    @platformer_mode.setter
    def platformer_mode(self, value: bool) -> None:
        self._json["kA22"] = value

    @middleground_texture_id.setter
    def middleground_texture_id(self, value: int) -> None:
        self._json["kA25"] = value

    @target_channel.setter
    def target_channel(self, value: int) -> None:
        self._json["kA26"] = value

    @allow_multi_rotation.setter
    def allow_multi_rotation(self, value: bool) -> None:
        self._json["kA27"] = value

    @mirror_mode.setter
    def mirror_mode(self, value: bool) -> None:
        self._json["kA28"] = value

    @rotate_gameplay.setter
    def rotate_gameplay(self, value: bool) -> None:
        self._json["kA29"] = value

    @enable_player_squeeze.setter
    def enable_player_squeeze(self, value: bool) -> None:
        self._json["kA31"] = value

    @fix_gravity_bug.setter
    def fix_gravity_bug(self, value: bool) -> None:
        self._json["kA32"] = value

    @fix_negative_scale.setter
    def fix_negative_scale(self, value: bool) -> None:
        self._json["kA33"] = value

    @fix_robot_jump.setter
    def fix_robot_jump(self, value: bool) -> None:
        self._json["kA34"] = value

    @reset_camera.setter
    def reset_camera(self, value: bool) -> None:
        self._json["kA35"] = value

    @spawn_group.setter
    def spawn_group(self, value: int) -> None:
        self._json["kA36"] = value

    @dynamic_level_height.setter
    def dynamic_level_height(self, value: bool) -> None:
        self._json["kA37"] = value

    @sort_groups.setter
    def sort_groups(self, value: bool) -> None:
        self._json["kA38"] = value

    @fix_radius_collision.setter
    def fix_radius_collision(self, value: bool) -> None:
        self._json["kA39"] = value

    @enable_two_point_two_changes.setter
    def enable_two_point_two_changes(self, value: bool) -> None:
        self._json["kA40"] = value

    @allow_static_rotate.setter
    def allow_static_rotate(self, value: bool) -> None:
        self._json["kA41"] = value

    @reverse_sync.setter
    def reverse_sync(self, value: bool) -> None:
        self._json["kA42"] = value

    @no_time_penalty.setter
    def no_time_penalty(self, value: bool) -> None:
        self._json["kA43"] = value

    @decrease_boost_slide.setter
    def decrease_boost_slide(self, value: bool) -> None:
        self._json["kA45"] = value

    @colors.setter
    def colors(self, value: LevelColors) -> None:
        self._json["kS38"] = value

    @color_page.setter
    def color_page(self, value: int) -> None:
        self._json["kS39"] = value

    def pygd_encode(self) -> str:
        result = ""

        for key, value in self._json.items():
            result += f"{key},{value.pygd_encode()},"

        return result[:-1]
