from ..level.level_color import LevelColor
from ..utility.string_helper import decode_color_string
from ..utility.type_converter import to_bool, to_int


class LevelStartObject:
    def __init__(self, level_start_object_json: dict) -> None:
        self._json = level_start_object_json

        colors = self._json.get("kS38")
        if colors is not None:
            decoded_colors = decode_color_string(colors)

            decoded_colors_classes = []

            for color in decoded_colors:
                decoded_colors_classes.append(LevelColor(color))

            self._json["kS38"] = decoded_colors_classes

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
        return to_bool(self._json.get("object_two_blending"))

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
    def colors(self) -> list[LevelColor]:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/color-string
        return self._json.get("kS38")

    @property
    def color_page(self) -> int:
        return to_int(self._json.get("kS39"))
