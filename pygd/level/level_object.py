from ..utility.type_converter import to_bool, to_int


class LevelObject:
    def __init__(self, level_object_json: dict) -> None:
        self._json = level_object_json

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

    @id.setter
    def id(self, value: int) -> None:
        self._json["1"] = value

    @x.setter
    def x(self, value: float) -> None:
        self._json["2"] = value

    @y.setter
    def y(self, value: float) -> None:
        self._json["3"] = value

    @flipped_horizontally.setter
    def flipped_horizontally(self, value: bool) -> None:
        self._json["4"] = value

    @flipped_vertically.setter
    def flipped_vertically(self, value: bool) -> None:
        self._json["5"] = value

    @rotation.setter
    def rotation(self, value: float) -> None:
        self._json["6"] = value

    @red.setter
    def red(self, value: int) -> None:
        self._json["7"] = value

    @green.setter
    def green(self, value: int) -> None:
        self._json["8"] = value

    @blue.setter
    def blue(self, value: int) -> None:
        self._json["9"] = value

    @duration.setter
    def duration(self, value: float) -> None:
        self._json["10"] = value

    @touch_triggered.setter
    def touch_triggered(self, value: bool) -> None:
        self._json["11"] = value

    @secret_coin_id.setter
    def secret_coin_id(self, value: int) -> None:
        self._json["12"] = value

    @special_object_checked.setter
    def special_object_checked(self, value: bool) -> None:
        self._json["13"] = value

    @tint_ground.setter
    def tint_ground(self, value: bool) -> None:
        self._json["14"] = value

    @player_color_one.setter
    def player_color_one(self, value: bool) -> None:
        self._json["15"] = value

    @player_color_two.setter
    def player_color_two(self, value: bool) -> None:
        self._json["16"] = value

    @blending.setter
    def blending(self, value: bool) -> None:
        self._json["17"] = value

    @one_point_nine_color_channel_id.setter
    def one_point_nine_color_channel_id(self, value: int) -> None:
        self._json["19"] = value

    @editor_layer_one.setter
    def editor_layer_one(self, value: int) -> None:
        self._json["20"] = value

    @main_color_channel_id.setter
    def main_color_channel_id(self, value: int) -> None:
        self._json["21"] = value

    @secondary_color_channel_id.setter
    def secondary_color_channel_id(self, value: int) -> None:
        self._json["22"] = value

    @target_color_id.setter
    def target_color_id(self, value: int) -> None:
        self._json["23"] = value

    @z_layer.setter
    def z_layer(self, value: int) -> None:
        self._json["24"] = value

    @z_order.setter
    def z_order(self, value: int) -> None:
        self._json["25"] = value

    @offset_x.setter
    def offset_x(self, value: int) -> None:
        self._json["28"] = value

    @offset_y.setter
    def offset_y(self, value: int) -> None:
        self._json["29"] = value

    @easing.setter
    def easing(self, value: int) -> None:
        self._json["30"] = value

    @text.setter
    def text(self, value: str) -> None:
        self._json["31"] = value

    @scaling.setter
    def scaling(self, value: float) -> None:
        self._json["32"] = value

    @single_group_id.setter
    def single_group_id(self, value: int) -> None:
        self._json["33"] = value

    @group_parent.setter
    def group_parent(self, value: bool) -> None:
        self._json["34"] = value

    @opacity.setter
    def opacity(self, value: float) -> None:
        self._json["35"] = value

    @main_color_hsv_enabled.setter
    def main_color_hsv_enabled(self, value: bool) -> None:
        self._json["41"] = value

    @secondary_color_hsv_enabled.setter
    def secondary_color_hsv_enabled(self, value: bool) -> None:
        self._json["42"] = value

    @fade_in.setter
    def fade_in(self, value: float) -> None:
        self._json["45"] = value

    @hold.setter
    def hold(self, value: float) -> None:
        self._json["46"] = value

    @fade_out.setter
    def fade_out(self, value: float) -> None:
        self._json["47"] = value

    @pulse_mode.setter
    def pulse_mode(self, value: int) -> None:
        self._json["48"] = value

    @copied_color_id.setter
    def copied_color_id(self, value: int) -> None:
        self._json["50"] = value

    @target_group_id.setter
    def target_group_id(self, value: int) -> None:
        self._json["51"] = value

    @pulse_target_type.setter
    def pulse_target_type(self, value: int) -> None:
        self._json["52"] = value

    @yellow_teleportation_portal_y_offset.setter
    def yellow_teleportation_portal_y_offset(self, value: float) -> None:
        self._json["54"] = value

    @teleport_portal_ease.setter
    def teleport_portal_ease(self, value: bool) -> None:
        self._json["55"] = value

    @activate_group.setter
    def activate_group(self, value: bool) -> None:
        self._json["56"] = value

    @group_ids.setter
    def group_ids(self, value: int) -> None:
        self._json["57"] = value

    @lock_to_player_x.setter
    def lock_to_player_x(self, value: bool) -> None:
        self._json["58"] = value

    @lock_to_player_y.setter
    def lock_to_player_y(self, value: bool) -> None:
        self._json["59"] = value

    @copy_opacity.setter
    def copy_opacity(self, value: bool) -> None:
        self._json["60"] = value

    @editor_layer_two.setter
    def editor_layer_two(self, value: int) -> None:
        self._json["61"] = value

    @spawn_triggered.setter
    def spawn_triggered(self, value: bool) -> None:
        self._json["62"] = value

    @spawn_delay.setter
    def spawn_delay(self, value: float) -> None:
        self._json["63"] = value

    @dont_fade.setter
    def dont_fade(self, value: bool) -> None:
        self._json["64"] = value

    @main_only.setter
    def main_only(self, value: bool) -> None:
        self._json["65"] = value

    @detail_only.setter
    def detail_only(self, value: bool) -> None:
        self._json["66"] = value

    @dont_enter.setter
    def dont_enter(self, value: bool) -> None:
        self._json["67"] = value

    @degrees.setter
    def degrees(self, value: int) -> None:
        self._json["68"] = value

    @times_three_sixty.setter
    def times_three_sixty(self, value: int) -> None:
        self._json["69"] = value

    @lock_object_rotation.setter
    def lock_object_rotation(self, value: bool) -> None:
        self._json["70"] = value

    @secondary_group_id.setter
    def secondary_group_id(self, value: int) -> None:
        self._json["71"] = value

    @x_mod.setter
    def x_mod(self, value: float) -> None:
        self._json["72"] = value

    @y_mod.setter
    def y_mod(self, value: float) -> None:
        self._json["73"] = value

    @strength.setter
    def strength(self, value: float) -> None:
        self._json["75"] = value

    @animation_id.setter
    def animation_id(self, value: int) -> None:
        self._json["76"] = value

    @count.setter
    def count(self, value: int) -> None:
        self._json["77"] = value

    @subtract_count.setter
    def subtract_count(self, value: int) -> None:
        self._json["78"] = value

    @pickup_mode.setter
    def pickup_mode(self, value: int) -> None:
        self._json["79"] = value

    @item_block_id.setter
    def item_block_id(self, value: int) -> None:
        self._json["80"] = value

    @hold_mode.setter
    def hold_mode(self, value: bool) -> None:
        self._json["81"] = value

    @toggle_mode.setter
    def toggle_mode(self, value: int) -> None:
        self._json["82"] = value

    @interval.setter
    def interval(self, value: float) -> None:
        self._json["84"] = value

    @easing_rate.setter
    def easing_rate(self, value: float) -> None:
        self._json["85"] = value

    @exclusive.setter
    def exclusive(self, value: bool) -> None:
        self._json["86"] = value

    @multi_trigger.setter
    def multi_trigger(self, value: bool) -> None:
        self._json["87"] = value

    @comparison.setter
    def comparison(self, value: int) -> None:
        self._json["88"] = value

    @dual_mode.setter
    def dual_mode(self, value: bool) -> None:
        self._json["89"] = value

    @speed.setter
    def speed(self, value: float) -> None:
        self._json["90"] = value

    @follow_delay.setter
    def follow_delay(self, value: float) -> None:
        self._json["91"] = value

    @y_offset.setter
    def y_offset(self, value: float) -> None:
        self._json["92"] = value

    @trigger_on_exit.setter
    def trigger_on_exit(self, value: bool) -> None:
        self._json["93"] = value

    @dynamic_block.setter
    def dynamic_block(self, value: bool) -> None:
        self._json["94"] = value

    @block_b_id.setter
    def block_b_id(self, value: int) -> None:
        self._json["95"] = value

    @disable_glow.setter
    def disable_glow(self, value: bool) -> None:
        self._json["96"] = value

    @custom_rotation_speed.setter
    def custom_rotation_speed(self, value: bool) -> None:
        self._json["97"] = value

    @disable_rotation.setter
    def disable_rotation(self, value: bool) -> None:
        self._json["98"] = value

    @multi_activate_orb.setter
    def multi_activate_orb(self, value: bool) -> None:
        self._json["99"] = value

    @enable_use_target.setter
    def enable_use_target(self, value: bool) -> None:
        self._json["100"] = value

    @editor_disable.setter
    def editor_disable(self, value: bool) -> None:
        self._json["102"] = value

    @high_detail.setter
    def high_detail(self, value: bool) -> None:
        self._json["103"] = value

    @multi_activate_trigger.setter
    def multi_activate_trigger(self, value: bool) -> None:
        self._json["104"] = value

    @max_speed.setter
    def max_speed(self, value: float) -> None:
        self._json["105"] = value

    @randomize_start.setter
    def randomize_start(self, value: bool) -> None:
        self._json["106"] = value

    @animation_speed.setter
    def animation_speed(self, value: float) -> None:
        self._json["107"] = value

    @linked_group_id.setter
    def linked_group_id(self, value: int) -> None:
        self._json["108"] = value

    @exit_static.setter
    def exit_static(self, value: bool) -> None:
        self._json["110"] = value

    @free_mode.setter
    def free_mode(self, value: bool) -> None:
        self._json["111"] = value

    @edit_camera_settings.setter
    def edit_camera_settings(self, value: bool) -> None:
        self._json["112"] = value

    @easing_free_mode.setter
    def easing_free_mode(self, value: int) -> None:
        self._json["113"] = value

    @padding.setter
    def padding(self, value: bool) -> None:
        self._json["114"] = value

    @ord.setter
    def ord(self, value: int) -> None:
        self._json["115"] = value

    @no_effects.setter
    def no_effects(self, value: bool) -> None:
        self._json["116"] = value

    @reverse.setter
    def reverse(self, value: bool) -> None:
        self._json["117"] = value

    @time_mod.setter
    def time_mod(self, value: float) -> None:
        self._json["120"] = value

    @no_touch.setter
    def no_touch(self, value: bool) -> None:
        self._json["121"] = value

    @scale_x.setter
    def scale_x(self, value: float) -> None:
        self._json["128"] = value

    @scale_y.setter
    def scale_y(self, value: float) -> None:
        self._json["129"] = value

    @warp_y_angle.setter
    def warp_y_angle(self, value: float) -> None:
        self._json["131"] = value

    @warp_x_angle.setter
    def warp_x_angle(self, value: float) -> None:
        self._json["132"] = value

    @staticmethod
    def default() -> "LevelObject":
        return LevelObject({
            "1": 1,  # id
            "2": 15,  # x
            "3": 15  # y
        })

    def encode_to_string(self) -> str:
        result = ""

        for key, value in self._json.items():
            result += f"{key},{value.encode_to_string()},"

        return result[:-1]
