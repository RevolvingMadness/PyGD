from ..utility.type_converter import to_bool, to_int


class Object:
    def __init__(self, object_json: dict) -> None:
        self._json = object_json

    @property
    def id(self) -> int:
        return to_int(self._json.get("1"))

    @property
    def x(self) -> float:
        return self._json.get("2")

    @property
    def y(self) -> float:
        return self._json.get("3")

    @property
    def flipped_horizontally(self) -> bool:
        return to_bool(self._json.get("4"))

    @property
    def flipped_vertically(self) -> bool:
        return to_bool(self._json.get("5"))

    @property
    def rotation(self) -> float:
        return self._json.get("6")

    @property
    def red(self) -> int:
        return to_int(self._json.get("7"))

    @property
    def green(self) -> int:
        return to_int(self._json.get("8"))

    @property
    def blue(self) -> int:
        return to_int(self._json.get("9"))

    @property
    def duration(self) -> float:
        return self._json.get("10")

    @property
    def touch_triggered(self) -> bool:
        return to_bool(self._json.get("11"))

    @property
    def secret_coin_id(self) -> int:
        return to_int(self._json.get("12"))

    @property
    def special_object_checked(self) -> bool:
        return to_bool(self._json.get("13"))

    @property
    def tint_ground(self) -> bool:
        return to_bool(self._json.get("14"))

    @property
    def player_color_one(self) -> bool:
        return to_bool(self._json.get("15"))

    @property
    def player_color_two(self) -> bool:
        return to_bool(self._json.get("16"))

    @property
    def blending(self) -> bool:
        return to_bool(self._json.get("17"))

    @property
    def one_point_nine_color_channel_id(self) -> int:
        return to_int(self._json.get("19"))

    @property
    def editor_layer_one(self) -> int:
        return to_int(self._json.get("20"))

    @property
    def main_color_channel_id(self) -> int:
        return to_int(self._json.get("21"))

    @property
    def secondary_color_channel_id(self) -> int:
        return to_int(self._json.get("22"))

    @property
    def target_color_id(self) -> int:
        return to_int(self._json.get("23"))

    @property
    def z_layer(self) -> int:
        return to_int(self._json.get("24"))

    @property
    def z_order(self) -> int:
        return to_int(self._json.get("25"))

    @property
    def offset_x(self) -> int:
        return to_int(self._json.get("28"))

    @property
    def offset_y(self) -> int:
        return to_int(self._json.get("29"))

    @property
    def easing(self) -> int:
        return to_int(self._json.get("30"))

    @property
    def text(self) -> str:
        return self._json.get("31")

    @property
    def scaling(self) -> float:
        return self._json.get("32")

    @property
    def single_group_id(self) -> int:
        return to_int(self._json.get("33"))

    @property
    def group_parent(self) -> bool:
        return to_bool(self._json.get("34"))

    @property
    def opacity(self) -> float:
        return self._json.get("35")

    @property
    def main_color_hsv_enabled(self) -> bool:
        return to_bool(self._json.get("41"))

    @property
    def secondary_color_hsv_enabled(self) -> bool:
        return to_bool(self._json.get("42"))

    # @property
    # def main_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._json.get("43")

    # @property
    # def secondary_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._json.get("44")

    @property
    def fade_in(self) -> float:
        return self._json.get("45")

    @property
    def hold(self) -> float:
        return self._json.get("46")

    @property
    def fade_out(self) -> float:
        return self._json.get("47")

    @property
    def pulse_mode(self) -> int:
        return to_int(self._json.get("48"))

    # @property
    # def copied_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._json.get("49")

    @property
    def copied_color_id(self) -> int:
        return to_int(self._json.get("50"))

    @property
    def target_group_id(self) -> int:
        return to_int(self._json.get("51"))

    @property
    def pulse_target_type(self) -> int:
        return to_int(self._json.get("52"))

    @property
    def yellow_teleportation_portal_y_offset(self) -> float:
        return self._json.get("54")

    @property
    def teleport_portal_ease(self) -> bool:
        return to_bool(self._json.get("55"))

    @property
    def activate_group(self) -> bool:
        return to_bool(self._json.get("56"))

    @property
    def group_ids(self) -> int:
        return to_int(self._json.get("57"))

    @property
    def lock_to_player_x(self) -> bool:
        return to_bool(self._json.get("58"))

    @property
    def lock_to_player_y(self) -> bool:
        return to_bool(self._json.get("59"))

    @property
    def copy_opacity(self) -> bool:
        return to_bool(self._json.get("60"))

    @property
    def editor_layer_two(self) -> int:
        return to_int(self._json.get("61"))

    @property
    def spawn_triggered(self) -> bool:
        return to_bool(self._json.get("62"))

    @property
    def spawn_delay(self) -> float:
        return self._json.get("63")

    @property
    def dont_fade(self) -> bool:
        return to_bool(self._json.get("64"))

    @property
    def main_only(self) -> bool:
        return to_bool(self._json.get("65"))

    @property
    def detail_only(self) -> bool:
        return to_bool(self._json.get("66"))

    @property
    def dont_enter(self) -> bool:
        return to_bool(self._json.get("67"))

    @property
    def degrees(self) -> int:
        return to_int(self._json.get("68"))

    @property
    def times_three_sixty(self) -> int:
        return to_int(self._json.get("69"))

    @property
    def lock_object_rotation(self) -> bool:
        return to_bool(self._json.get("70"))

    @property
    def secondary_group_id(self) -> int:
        return to_int(self._json.get("71"))

    @property
    def x_mod(self) -> float:
        return self._json.get("72")

    @property
    def y_mod(self) -> float:
        return self._json.get("73")

    @property
    def strength(self) -> float:
        return self._json.get("75")

    @property
    def animation_id(self) -> int:
        return to_int(self._json.get("76"))

    @property
    def count(self) -> int:
        return to_int(self._json.get("77"))

    @property
    def subtract_count(self) -> int:
        return to_int(self._json.get("78"))

    @property
    def pickup_mode(self) -> int:
        return to_int(self._json.get("79"))

    @property
    def item_block_id(self) -> int:
        return to_int(self._json.get("80"))

    @property
    def hold_mode(self) -> bool:
        return to_bool(self._json.get("81"))

    @property
    def toggle_mode(self) -> int:
        return to_int(self._json.get("82"))

    @property
    def interval(self) -> float:
        return self._json.get("84")

    @property
    def easing_rate(self) -> float:
        return self._json.get("85")

    @property
    def exclusive(self) -> bool:
        return to_bool(self._json.get("86"))

    @property
    def multi_trigger(self) -> bool:
        return to_bool(self._json.get("87"))

    @property
    def comparison(self) -> int:
        return to_int(self._json.get("88"))

    @property
    def dual_mode(self) -> bool:
        return to_bool(self._json.get("89"))

    @property
    def speed(self) -> float:
        return self._json.get("90")

    @property
    def follow_delay(self) -> float:
        return self._json.get("91")

    @property
    def y_offset(self) -> float:
        return self._json.get("92")

    @property
    def trigger_on_exit(self) -> bool:
        return to_bool(self._json.get("93"))

    @property
    def dynamic_block(self) -> bool:
        return to_bool(self._json.get("94"))

    @property
    def block_b_id(self) -> int:
        return to_int(self._json.get("95"))

    @property
    def disable_glow(self) -> bool:
        return to_bool(self._json.get("96"))

    @property
    def custom_rotation_speed(self) -> bool:
        return to_bool(self._json.get("97"))

    @property
    def disable_rotation(self) -> bool:
        return to_bool(self._json.get("98"))

    @property
    def multi_activate_orb(self) -> bool:
        return to_bool(self._json.get("99"))

    @property
    def enable_use_target(self) -> bool:
        return to_bool(self._json.get("100"))

    # @property
    # def target_pos_coordinates(self) -> TargetPosCoordinates: # No documentation
    #     return self._json.get("101")

    @property
    def editor_disable(self) -> bool:
        return to_bool(self._json.get("102"))

    @property
    def high_detail(self) -> bool:
        return to_bool(self._json.get("103"))

    @property
    def multi_activate_trigger(self) -> bool:
        return to_bool(self._json.get("104"))

    @property
    def max_speed(self) -> float:
        return self._json.get("105")

    @property
    def randomize_start(self) -> bool:
        return to_bool(self._json.get("106"))

    @property
    def animation_speed(self) -> float:
        return self._json.get("107")

    @property
    def linked_group_id(self) -> int:
        return to_int(self._json.get("108"))

    @property
    def exit_static(self) -> bool:
        return to_bool(self._json.get("110"))

    @property
    def free_mode(self) -> bool:
        return to_bool(self._json.get("111"))

    @property
    def edit_camera_settings(self) -> bool:
        return to_bool(self._json.get("112"))

    @property
    def easing_free_mode(self) -> int:
        return to_int(self._json.get("113"))

    @property
    def padding(self) -> bool:
        return to_bool(self._json.get("114"))

    @property
    def ord(self) -> int:  # I don't know what "ord" is. Maybe order?
        return to_int(self._json.get("115"))

    @property
    def no_effects(self) -> bool:
        return to_bool(self._json.get("116"))

    @property
    def reverse(self) -> bool:
        return to_bool(self._json.get("117"))

    @property
    def time_mod(self) -> float:
        return self._json.get("120")

    @property
    def no_touch(self) -> bool:
        return to_bool(self._json.get("121"))

    @property
    def scale_x(self) -> float:
        return self._json.get("128")

    @property
    def scale_y(self) -> float:
        return self._json.get("129")

    @property
    def warp_y_angle(self) -> float:
        return self._json.get("131")

    @property
    def warp_x_angle(self) -> float:
        return self._json.get("132")

    @staticmethod
    def default() -> "Object":
        return Object({
            "1": 1,  # id
            "2": 15,  # x
            "3": 15  # y
        })
