from pygd.utility.string_helper import decode_object_string
from ..utility.type_converter import to_bool, to_int


###
# potentially discarded, bottom of page
# undiscovered, bottom of page
# https://wyliemaster.github.io/gddocs/#/resources/client/level-components/level-object
###


class Object:
    def __init__(self, object_string: str) -> None:
        object_json = decode_object_string(object_string)

        self._properties = {
            "1": object_json.get("1"),  # id
            "2": object_json.get("2"),  # x
            "3": object_json.get("3"),  # y
            "4": object_json.get("4"),  # flipped_horizontally
            "5": object_json.get("5"),  # flipped_vertically
            "6": object_json.get("6"),  # rotation
            "7": object_json.get("7"),  # red
            "8": object_json.get("8"),  # green
            "9": object_json.get("9"),  # blue
            "10": object_json.get("10"),  # duration
            "11": object_json.get("11"),  # touch_triggered
            "12": object_json.get("12"),  # secret_coin_id
            "13": object_json.get("13"),  # special_object_checked
            "14": object_json.get("14"),  # tint_ground
            "15": object_json.get("15"),  # player_color_one
            "16": object_json.get("16"),  # player_color_two
            "17": object_json.get("17"),  # blending
            "18": object_json.get("18"),  # unknown - potentially discarded
            "19": object_json.get("19"),  # one_point_nine_color_channel_id
            "20": object_json.get("20"),  # editor_layer_one
            "21": object_json.get("21"),  # main_color_channel_id
            "22": object_json.get("22"),  # secondary_color_channel_id
            "23": object_json.get("23"),  # target_color_id
            "24": object_json.get("24"),  # z_layer
            "25": object_json.get("25"),  # z_order
            "26": object_json.get("26"),  # unknown - potentially discarded
            "27": object_json.get("27"),  # unknown - potentially discarded
            "28": object_json.get("28"),  # offset_x
            "29": object_json.get("29"),  # offset_y
            "30": object_json.get("30"),  # easing
            "31": object_json.get("31"),  # text
            "32": object_json.get("32"),  # scaling
            "33": object_json.get("33"),  # single_group_id
            "34": object_json.get("34"),  # group_parent
            "35": object_json.get("35"),  # opacity
            # suspected to be handling whether an object's X position is locked and unaffected by a Move trigger
            "36": object_json.get("36"),  # unknown - undiscovered
            "37": object_json.get("37"),  # unknown - potentially discarded
            "38": object_json.get("38"),  # unknown - potentially discarded
            "39": object_json.get("39"),  # unknown - potentially discarded
            "40": object_json.get("40"),  # unknown - potentially discarded
            "41": object_json.get("41"),  # main_color_hsv_enabled
            "42": object_json.get("42"),  # secondary_color_hsv_enabled
            "43": object_json.get("43"),  # main_color_hsv
            "44": object_json.get("44"),  # secondary_color_hsv
            "45": object_json.get("45"),  # fade_in
            "46": object_json.get("46"),  # hold
            "47": object_json.get("47"),  # fade_out
            "48": object_json.get("48"),  # pulse_mode
            "49": object_json.get("49"),  # copied_color_hsv
            "50": object_json.get("50"),  # copied_color_id
            "51": object_json.get("51"),  # target_group_id
            "52": object_json.get("52"),  # pulse_target_type
            "53": object_json.get("53"),  # unknown - potentially discarded
            "54": object_json.get("54"),  # yellow_teleportation_portal_y_offset
            "55": object_json.get("55"),  # teleport_portal_ease
            "56": object_json.get("56"),  # activate_group
            "57": object_json.get("57"),  # group_ids
            "58": object_json.get("58"),  # lock_to_player_x
            "59": object_json.get("59"),  # lock_to_player_y
            "60": object_json.get("60"),  # copy_opacity
            "61": object_json.get("61"),  # editor_layer_two
            "62": object_json.get("62"),  # spawn_triggered
            "63": object_json.get("63"),  # spawn_delay
            "64": object_json.get("64"),  # dont_fade
            "65": object_json.get("65"),  # main_only
            "66": object_json.get("66"),  # detail_only
            "67": object_json.get("67"),  # dont_enter
            "68": object_json.get("68"),  # degrees
            "69": object_json.get("69"),  # times_three_sixty
            "70": object_json.get("70"),  # lock_object_rotation
            "71": object_json.get("71"),  # secondary_group_id
            "72": object_json.get("72"),  # x_mod
            "73": object_json.get("73"),  # y_mod
            # only found in the Follow Player Y trigger
            "74": object_json.get("74"),  # unknown - undiscovered
            "75": object_json.get("75"),  # strength
            "76": object_json.get("76"),  # animation_id
            "77": object_json.get("77"),  # count
            "78": object_json.get("78"),  # subtract_count
            "79": object_json.get("79"),  # pickup_mode
            "80": object_json.get("80"),  # item_block_id
            "81": object_json.get("81"),  # hold_mode
            "82": object_json.get("82"),  # toggle_mode
            "83": object_json.get("83"),  # unknown - potentially discarded
            "84": object_json.get("84"),  # interval
            "85": object_json.get("85"),  # easing_rate
            "86": object_json.get("86"),  # exclusive
            "87": object_json.get("87"),  # multi_trigger
            "88": object_json.get("88"),  # comparison
            "89": object_json.get("89"),  # dual_mode
            "90": object_json.get("90"),  # speed
            "91": object_json.get("91"),  # follow_delay
            "92": object_json.get("92"),  # y_offset
            "93": object_json.get("93"),  # trigger_on_exit
            "94": object_json.get("94"),  # dynamic_block
            "95": object_json.get("95"),  # block_b_id
            "96": object_json.get("96"),  # disable_glow
            "97": object_json.get("97"),  # custom_rotation_speed
            "98": object_json.get("98"),  # disable_rotation
            "99": object_json.get("99"),  # multi_activate_orb
            "100": object_json.get("100"),  # enable_use_target
            "101": object_json.get("101"),  # target_pos_coordinates
            "102": object_json.get("102"),  # editor_disable
            "103": object_json.get("103"),  # high_detail
            "104": object_json.get("104"),  # multi_activate_trigger
            "105": object_json.get("105"),  # max_speed
            "106": object_json.get("106"),  # randomize_start
            "107": object_json.get("107"),  # animation_speed
            "108": object_json.get("108"),  # linked_group_id
            "109": object_json.get("109"),  # unknown - potentially discarded
            "110": object_json.get("110"),  # exit_static
            "111": object_json.get("111"),  # free_mode
            "112": object_json.get("112"),  # edit_camera_settings
            "113": object_json.get("113"),  # easing_free_mode
            "114": object_json.get("114"),  # padding
            "115": object_json.get("115"),  # ord
            "116": object_json.get("116"),  # no_effects
            "117": object_json.get("117"),  # reverse
            "118": object_json.get("118"),  # unknown - potentially discarded
            "119": object_json.get("119"),  # unknown - potentially discarded
            "120": object_json.get("120"),  # time_mod
            "121": object_json.get("121"),  # no_touch
            "122": object_json.get("122"),  # unknown - potentially discarded
            "123": object_json.get("123"),  # unknown - potentially discarded
            "124": object_json.get("124"),  # unknown - potentially discarded
            "125": object_json.get("125"),  # unknown - potentially discarded
            "126": object_json.get("126"),  # unknown - potentially discarded
            "127": object_json.get("127"),  # unknown - potentially discarded
            "128": object_json.get("128"),  # scale_x
            "129": object_json.get("129"),  # scale_y, not sure (documentation is bugged)
            "130": object_json.get("130"),  # unknown - potentially discarded
            "131": object_json.get("131"),  # warp_y_angle
            "132": object_json.get("132"),  # warp_x_angle
            # Suspected to be something related to optimizing colors. Appears on all objects
            "155": object_json.get("155"),  # unknown - undiscovered
            # Same as 155
            "156": object_json.get("156"),  # unknown - undiscovered
        }

    @property
    def id(self) -> int:
        return to_int(self._properties["1"])

    @property
    def x(self) -> float:
        return self._properties["2"]

    @property
    def y(self) -> float:
        return self._properties["3"]

    @property
    def flipped_horizontally(self) -> bool:
        return to_bool(self._properties["4"])

    @property
    def flipped_vertically(self) -> bool:
        return to_bool(self._properties["5"])

    @property
    def rotation(self) -> float:
        return self._properties["6"]

    @property
    def red(self) -> int:
        return to_int(self._properties["7"])

    @property
    def green(self) -> int:
        return to_int(self._properties["8"])

    @property
    def blue(self) -> int:
        return to_int(self._properties["9"])

    @property
    def duration(self) -> float:
        return self._properties["10"]

    @property
    def touch_triggered(self) -> bool:
        return to_bool(self._properties["11"])

    @property
    def secret_coin_id(self) -> int:
        return to_int(self._properties["12"])

    @property
    def special_object_checked(self) -> bool:
        return to_bool(self._properties["13"])

    @property
    def tint_ground(self) -> bool:
        return to_bool(self._properties["14"])

    @property
    def player_color_one(self) -> bool:
        return to_bool(self._properties["15"])

    @property
    def player_color_two(self) -> bool:
        return to_bool(self._properties["16"])

    @property
    def blending(self) -> bool:
        return to_bool(self._properties["17"])

    @property
    def one_point_nine_color_channel_id(self) -> int:
        return to_int(self._properties["19"])

    @property
    def editor_layer_one(self) -> int:
        return to_int(self._properties["20"])

    @property
    def main_color_channel_id(self) -> int:
        return to_int(self._properties["21"])

    @property
    def secondary_color_channel_id(self) -> int:
        return to_int(self._properties["22"])

    @property
    def target_color_id(self) -> int:
        return to_int(self._properties["23"])

    @property
    def z_layer(self) -> int:
        return to_int(self._properties["24"])

    @property
    def z_order(self) -> int:
        return to_int(self._properties["25"])

    @property
    def offset_x(self) -> int:
        return to_int(self._properties["28"])

    @property
    def offset_y(self) -> int:
        return to_int(self._properties["29"])

    @property
    def easing(self) -> int:
        return to_int(self._properties["30"])

    @property
    def text(self) -> str:
        return self._properties["31"]

    @property
    def scaling(self) -> float:
        return self._properties["32"]

    @property
    def single_group_id(self) -> int:
        return to_int(self._properties["33"])

    @property
    def group_parent(self) -> bool:
        return to_bool(self._properties["34"])

    @property
    def opacity(self) -> float:
        return self._properties["35"]

    @property
    def main_color_hsv_enabled(self) -> bool:
        return to_bool(self._properties["41"])

    @property
    def secondary_color_hsv_enabled(self) -> bool:
        return to_bool(self._properties["42"])

    # @property
    # def main_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._properties["43"]

    # @property
    # def secondary_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._properties["44"]

    @property
    def fade_in(self) -> float:
        return self._properties["45"]

    @property
    def hold(self) -> float:
        return self._properties["46"]

    @property
    def fade_out(self) -> float:
        return self._properties["47"]

    @property
    def pulse_mode(self) -> int:
        return to_int(self._properties["48"])

    # @property
    # def copied_color_hsv(self) -> HSV:  # I'm confused how to "decode" HSV
    #     return self._properties["49"]

    @property
    def copied_color_id(self) -> int:
        return to_int(self._properties["50"])

    @property
    def target_group_id(self) -> int:
        return to_int(self._properties["51"])

    @property
    def pulse_target_type(self) -> int:
        return to_int(self._properties["52"])

    @property
    def yellow_teleportation_portal_y_offset(self) -> float:
        return self._properties["54"]

    @property
    def teleport_portal_ease(self) -> bool:
        return to_bool(self._properties["55"])

    @property
    def activate_group(self) -> bool:
        return to_bool(self._properties["56"])

    @property
    def group_ids(self) -> int:
        return to_int(self._properties["57"])

    @property
    def lock_to_player_x(self) -> bool:
        return to_bool(self._properties["58"])

    @property
    def lock_to_player_y(self) -> bool:
        return to_bool(self._properties["59"])

    @property
    def copy_opacity(self) -> bool:
        return to_bool(self._properties["60"])

    @property
    def editor_layer_two(self) -> int:
        return to_int(self._properties["61"])

    @property
    def spawn_triggered(self) -> bool:
        return to_bool(self._properties["62"])

    @property
    def spawn_delay(self) -> float:
        return self._properties["63"]

    @property
    def dont_fade(self) -> bool:
        return to_bool(self._properties["64"])

    @property
    def main_only(self) -> bool:
        return to_bool(self._properties["65"])

    @property
    def detail_only(self) -> bool:
        return to_bool(self._properties["66"])

    @property
    def dont_enter(self) -> bool:
        return to_bool(self._properties["67"])

    @property
    def degrees(self) -> int:
        return to_int(self._properties["68"])

    @property
    def times_three_sixty(self) -> int:
        return to_int(self._properties["69"])

    @property
    def lock_object_rotation(self) -> bool:
        return to_bool(self._properties["70"])

    @property
    def secondary_group_id(self) -> int:
        return to_int(self._properties["71"])

    @property
    def x_mod(self) -> float:
        return self._properties["72"]

    @property
    def y_mod(self) -> float:
        return self._properties["73"]

    @property
    def strength(self) -> float:
        return self._properties["75"]

    @property
    def animation_id(self) -> int:
        return to_int(self._properties["76"])

    @property
    def count(self) -> int:
        return to_int(self._properties["77"])

    @property
    def subtract_count(self) -> int:
        return to_int(self._properties["78"])

    @property
    def pickup_mode(self) -> int:
        return to_int(self._properties["79"])

    @property
    def item_block_id(self) -> int:
        return to_int(self._properties["80"])

    @property
    def hold_mode(self) -> bool:
        return to_bool(self._properties["81"])

    @property
    def toggle_mode(self) -> int:
        return to_int(self._properties["82"])

    @property
    def interval(self) -> float:
        return self._properties["84"]

    @property
    def easing_rate(self) -> float:
        return self._properties["85"]

    @property
    def exclusive(self) -> bool:
        return to_bool(self._properties["86"])

    @property
    def multi_trigger(self) -> bool:
        return to_bool(self._properties["87"])

    @property
    def comparison(self) -> int:
        return to_int(self._properties["88"])

    @property
    def dual_mode(self) -> bool:
        return to_bool(self._properties["89"])

    @property
    def speed(self) -> float:
        return self._properties["90"]

    @property
    def follow_delay(self) -> float:
        return self._properties["91"]

    @property
    def y_offset(self) -> float:
        return self._properties["92"]

    @property
    def trigger_on_exit(self) -> bool:
        return to_bool(self._properties["93"])

    @property
    def dynamic_block(self) -> bool:
        return to_bool(self._properties["94"])

    @property
    def block_b_id(self) -> int:
        return to_int(self._properties["95"])

    @property
    def disable_glow(self) -> bool:
        return to_bool(self._properties["96"])

    @property
    def custom_rotation_speed(self) -> bool:
        return to_bool(self._properties["97"])

    @property
    def disable_rotation(self) -> bool:
        return to_bool(self._properties["98"])

    @property
    def multi_activate_orb(self) -> bool:
        return to_bool(self._properties["99"])

    @property
    def enable_use_target(self) -> bool:
        return to_bool(self._properties["100"])

    # @property
    # def target_pos_coordinates(self) -> TargetPosCoordinates: # No documentation
    #     return self._properties["101"]

    @property
    def editor_disable(self) -> bool:
        return to_bool(self._properties["102"])

    @property
    def high_detail(self) -> bool:
        return to_bool(self._properties["103"])

    @property
    def multi_activate_trigger(self) -> bool:
        return to_bool(self._properties["104"])

    @property
    def max_speed(self) -> float:
        return self._properties["105"]

    @property
    def randomize_start(self) -> bool:
        return to_bool(self._properties["106"])

    @property
    def animation_speed(self) -> float:
        return self._properties["107"]

    @property
    def linked_group_id(self) -> int:
        return to_int(self._properties["108"])

    @property
    def exit_static(self) -> bool:
        return to_bool(self._properties["110"])

    @property
    def free_mode(self) -> bool:
        return to_bool(self._properties["111"])

    @property
    def edit_camera_settings(self) -> bool:
        return to_bool(self._properties["112"])

    @property
    def easing_free_mode(self) -> int:
        return to_int(self._properties["113"])

    @property
    def padding(self) -> bool:
        return to_bool(self._properties["114"])

    @property
    def ord(self) -> int:  # I don't know what "ord" is. Maybe order?
        return to_int(self._properties["115"])

    @property
    def no_effects(self) -> bool:
        return to_bool(self._properties["116"])

    @property
    def reverse(self) -> bool:
        return to_bool(self._properties["117"])

    @property
    def time_mod(self) -> float:
        return self._properties["120"]

    @property
    def no_touch(self) -> bool:
        return to_bool(self._properties["121"])

    @property
    def scale_x(self) -> float:
        return self._properties["128"]

    @property
    def scale_y(self) -> float:
        return self._properties["129"]

    @property
    def warp_y_angle(self) -> float:
        return self._properties["131"]

    @property
    def warp_x_angle(self) -> float:
        return self._properties["132"]
