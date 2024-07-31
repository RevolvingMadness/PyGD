from ..level.level_color import LevelColor
from ..utility.string_helper import decode_level_start_object_string
from ..utility.type_converter import to_bool, to_int


class LevelStartObject:
    def __init__(self, level_start_object_string: str) -> None:
        level_start_object_json = decode_level_start_object_string(
            level_start_object_string
        )

        self._properties = {
            "kA1": level_start_object_json.get("audio_track"),
            "kA2": level_start_object_json.get("gamemode"),
            "kA3": level_start_object_json.get("mini"),
            "kA4": level_start_object_json.get("speed"),
            "kA5": level_start_object_json.get("object_two_blending"),  # deprecated
            "kA6": level_start_object_json.get("background_texture_id"),
            "kA7": level_start_object_json.get("ground_texture_id"),
            "kA8": level_start_object_json.get("is_dual_mode"),
            "kA9": level_start_object_json.get("is_start_pos_object"),
            "kA10": level_start_object_json.get("is_two_player_mode"),
            "kA11": level_start_object_json.get("flip_gravity"),
            "kA12": level_start_object_json.get("color_three_blending"),  # deprecated
            "kA13": level_start_object_json.get("song_offset"),
            "kA14": level_start_object_json.get("guidelines"),
            "kA15": level_start_object_json.get("fade_in"),
            "kA16": level_start_object_json.get("fade_out"),
            "kA17": level_start_object_json.get("ground_line"),
            "kA18": level_start_object_json.get("font"),
            "kA19": level_start_object_json.get("target_order"),
            "kA20": level_start_object_json.get("reverse_gameplay"),
            "kA21": level_start_object_json.get("is_disabled"),
            "kA22": level_start_object_json.get("platformer_mode"),
            # kA23
            # kA24
            "kA25": level_start_object_json.get("middleground_texture_id"),
            "kA26": level_start_object_json.get("target_channel"),
            "kA27": level_start_object_json.get("allow_multi_rotation"),
            "kA28": level_start_object_json.get("mirror_mode"),
            "kA29": level_start_object_json.get("rotate_gameplay"),
            # kA30
            "kA31": level_start_object_json.get("enable_player_squeeze"),
            "kA32": level_start_object_json.get("fix_gravity_bug"),
            "kA33": level_start_object_json.get("fix_negative_scale"),
            "kA34": level_start_object_json.get("fix_robot_jump"),
            "kA35": level_start_object_json.get("reset_camera"),
            "kA36": level_start_object_json.get("spawn_group"),
            "kA37": level_start_object_json.get("dynamic_level_height"),
            "kA38": level_start_object_json.get("sort_groups"),
            "kA39": level_start_object_json.get("fix_radius_collision"),
            "kA40": level_start_object_json.get("enable_two_point_two_changes"),
            "kA41": level_start_object_json.get("allow_static_rotate"),
            "kA42": level_start_object_json.get("reverse_sync"),
            "kA43": level_start_object_json.get("no_time_penalty"),
            # kA44
            "kA45": level_start_object_json.get("decrease_boost_slide"),
            "kS38": level_start_object_json.get("colors"),
            "kS39": level_start_object_json.get("color_page"),
        }

    @property
    def audio_track(self) -> int:
        return to_int(self._properties["kA1"])

    @property
    def gamemode(self) -> int:
        return to_int(self._properties["kA2"])

    @property
    def mini(self) -> bool:
        return to_bool(self._properties["kA3"])

    @property
    def speed(self) -> int:
        return to_int(self._properties["kA4"])

    @property
    def object_two_blending(self) -> bool:
        return to_bool(self._properties["object_two_blending"])

    @property
    def background_texture_id(self) -> int:
        return to_int(self._properties["kA6"])

    @property
    def ground_texture_id(self) -> int:
        return to_int(self._properties["kA7"])

    @property
    def is_dual_mode(self) -> bool:
        return to_bool(self._properties["kA8"])

    @property
    def is_start_pos_object(self) -> bool:
        return to_bool(self._properties["kA9"])

    @property
    def is_two_player_mode(self) -> bool:
        return to_bool(self._properties["kA10"])

    @property
    def flip_gravity(self) -> bool:
        return to_bool(self._properties["kA11"])

    @property
    def color_three_blending(self) -> bool:
        return to_bool(self._properties["kA12"])

    @property
    def song_offset(self) -> float:
        return self._properties["kA13"]

    @property
    def guidelines(self) -> str:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/guideline-string
        return self._properties["kA14"]

    @property
    def fade_in(self) -> bool:
        return to_bool(self._properties["kA15"])

    @property
    def fade_out(self) -> bool:
        return to_bool(self._properties["kA16"])

    @property
    def ground_line(self) -> int:
        return to_int(self._properties["kA17"])

    @property
    def font(self) -> int:
        return to_int(self._properties["kA18"])

    @property
    def target_order(self) -> int:
        return to_int(self._properties["kA19"])

    @property
    def reverse_gameplay(self) -> bool:
        return to_bool(self._properties["kA20"])

    @property
    def is_disabled(self) -> bool:
        return to_bool(self._properties["kA21"])

    @property
    def platformer_mode(self) -> bool:
        return to_bool(self._properties["kA22"])

    @property
    def middleground_texture_id(self) -> int:
        return to_int(self._properties["kA25"])

    @property
    def target_channel(self) -> int:
        return to_int(self._properties["kA26"])

    @property
    def allow_multi_rotation(self) -> bool:
        return to_bool(self._properties["kA27"])

    @property
    def mirror_mode(self) -> bool:
        return to_bool(self._properties["kA28"])

    @property
    def rotate_gameplay(self) -> bool:
        return to_bool(self._properties["kA29"])

    @property
    def enable_player_squeeze(self) -> bool:
        return to_bool(self._properties["kA31"])

    @property
    def fix_gravity_bug(self) -> bool:
        return to_bool(self._properties["kA32"])

    @property
    def fix_negative_scale(self) -> bool:
        return to_bool(self._properties["kA33"])

    @property
    def fix_robot_jump(self) -> bool:
        return to_bool(self._properties["kA34"])

    @property
    def reset_camera(self) -> bool:
        return to_bool(self._properties["kA35"])

    @property
    def spawn_group(self) -> int:
        return to_int(self._properties["kA36"])

    @property
    def dynamic_level_height(self) -> bool:
        return to_bool(self._properties["kA37"])

    @property
    def sort_groups(self) -> bool:
        return to_bool(self._properties["kA38"])

    @property
    def fix_radius_collision(self) -> bool:
        return to_bool(self._properties["kA39"])

    @property
    def enable_two_point_two_changes(self) -> bool:
        return to_bool(self._properties["kA40"])

    @property
    def allow_static_rotate(self) -> bool:
        return to_bool(self._properties["kA41"])

    @property
    def reverse_sync(self) -> bool:
        return to_bool(self._properties["kA42"])

    @property
    def no_time_penalty(self) -> bool:
        return to_bool(self._properties["kA43"])

    @property
    def decrease_boost_slide(self) -> bool:
        return to_bool(self._properties["kA45"])

    @property
    def colors(self) -> list[LevelColor]:
        # https://wyliemaster.github.io/gddocs/#/resources/client/level-components/color-string
        return self._properties["kS38"]

    @property
    def color_page(self) -> int:
        return to_int(self._properties["kS39"])
