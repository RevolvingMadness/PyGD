import base64
import zlib

from .rename_key import _rename_key


def _rename_color(color: dict) -> None:
    _rename_key(color, "1", "from_color_red")
    _rename_key(color, "2", "from_color_green")
    _rename_key(color, "3", "from_color_blue")
    _rename_key(color, "4", "player_color")
    _rename_key(color, "5", "blending")
    _rename_key(color, "6", "color_channel_index")
    _rename_key(color, "7", "from_opacity")
    _rename_key(color, "8", "toggle_opacity")
    _rename_key(color, "9", "inherited_color_channel_index")
    _rename_key(color, "10", "hsv")
    _rename_key(color, "11", "to_color_red")
    _rename_key(color, "12", "to_color_green")
    _rename_key(color, "13", "to_color_blue")
    _rename_key(color, "14", "delta_time")
    _rename_key(color, "15", "to_opacity")
    _rename_key(color, "16", "duration")
    _rename_key(color, "17", "copy_opacity")


def _format_colors(data: str) -> list:
    data = data.split("|")[:-1]
    result = []

    key = None

    for color_string in data:
        color_string_split = color_string.split("_")

        color = {}

        for color_property in color_string_split:
            if key is None:
                key = color_property
            else:
                if key is None:
                    raise Exception("Format is incorrect.")

                color[key] = color_property
                key = None

        _rename_color(color)
        result.append(color)

    return result


def _rename_object(object_: dict) -> None:
    _rename_key(object_, "1", "id")
    _rename_key(object_, "2", "x")
    _rename_key(object_, "3", "y")
    _rename_key(object_, "4", "flipped_horizontally")
    _rename_key(object_, "5", "flipped_vertically")
    _rename_key(object_, "6", "rotation")
    _rename_key(object_, "7", "red")
    _rename_key(object_, "8", "green")
    _rename_key(object_, "9", "blue")
    _rename_key(object_, "10", "duration")
    _rename_key(object_, "11", "touch_triggered")
    _rename_key(object_, "12", "secret_coin_id")
    _rename_key(object_, "13", "special_object_checked")
    _rename_key(object_, "14", "tint_ground")
    _rename_key(object_, "15", "player_color_one")
    _rename_key(object_, "16", "player_color_two")
    _rename_key(object_, "17", "blending")
    # _rename_key(object, "18", "") # deprecated
    _rename_key(object_, "19", "one_point_nine_color_channel_id")
    _rename_key(object_, "20", "editor_layer_one")
    _rename_key(object_, "21", "main_color_channel_id")
    _rename_key(object_, "22", "secondary_color_channel_id")
    _rename_key(object_, "23", "target_color_id")
    _rename_key(object_, "24", "z_layer")
    _rename_key(object_, "25", "z_order")
    # _rename_key(object, "26", "") # deprecated
    # _rename_key(object, "27", "") # deprecated
    _rename_key(object_, "28", "offset_x")
    _rename_key(object_, "29", "offset_y")
    _rename_key(object_, "30", "easing")
    _rename_key(object_, "31", "text")
    _rename_key(object_, "32", "scaling")
    _rename_key(object_, "33", "single_group_id")
    _rename_key(object_, "34", "group_parent")
    _rename_key(object_, "35", "opacity")
    # _rename_key(object, "36", "") # suspected to be handling whether an object's X position is locked and unaffected by a move trigger, unknown
    # _rename_key(object, "37", "") # deprecated
    # _rename_key(object, "38", "") # deprecated
    # _rename_key(object, "39", "") # deprecated
    # _rename_key(object, "40", "") # deprecated
    _rename_key(object_, "41", "main_color_hsv_enabled")
    _rename_key(object_, "42", "secondary_color_hsv_enabled")
    _rename_key(object_, "43", "main_color_hsv")
    _rename_key(object_, "44", "secondary_color_hsv")
    _rename_key(object_, "45", "fade_in")
    _rename_key(object_, "46", "hold")
    _rename_key(object_, "47", "fade_out")
    _rename_key(object_, "48", "pulse_mode")
    _rename_key(object_, "49", "copied_color_hsv")
    _rename_key(object_, "50", "copied_color_id")
    _rename_key(object_, "51", "target_group_id")
    _rename_key(object_, "52", "pulse_target_type")
    # _rename_key(object, "53", "") # deprecated
    _rename_key(object_, "54", "yellow_teleportation_portal_y_offset")
    _rename_key(object_, "55", "teleport_portal_ease")
    _rename_key(object_, "56", "activate_group")
    _rename_key(object_, "57", "group_ids")
    _rename_key(object_, "58", "lock_to_player_x")
    _rename_key(object_, "59", "lock_to_player_y")
    _rename_key(object_, "60", "copy_opacity")
    _rename_key(object_, "61", "editor_layer_two")
    _rename_key(object_, "62", "spawn_triggered")
    _rename_key(object_, "63", "spawn_delay")
    _rename_key(object_, "64", "dont_fade")
    _rename_key(object_, "65", "main_only")
    _rename_key(object_, "66", "detail_only")
    _rename_key(object_, "67", "dont_enter")
    _rename_key(object_, "68", "degrees")
    _rename_key(object_, "69", "times_three_sixty")
    _rename_key(object_, "70", "lock_object_rotation")
    _rename_key(object_, "71", "secondary_group_id")
    _rename_key(object_, "72", "x_mod")
    _rename_key(object_, "73", "y_mod")
    # _rename_key(object, "74", "") # unknown, only found in follow player Y trigger
    _rename_key(object_, "75", "strength")
    _rename_key(object_, "76", "animation_id")
    _rename_key(object_, "77", "count")
    _rename_key(object_, "78", "subtract_count")
    _rename_key(object_, "79", "pickup_mode")
    _rename_key(object_, "80", "item_block_id")
    _rename_key(object_, "81", "hold_mode")
    _rename_key(object_, "82", "toggle_mode")
    # _rename_key(object, "83", "") # deprecated
    _rename_key(object_, "84", "interval")
    _rename_key(object_, "85", "easing_rate")
    _rename_key(object_, "86", "exclusive")
    _rename_key(object_, "87", "multi_trigger")
    _rename_key(object_, "88", "comparison")
    _rename_key(object_, "89", "dual_mode")
    _rename_key(object_, "90", "speed")
    _rename_key(object_, "91", "follow_delay")
    _rename_key(object_, "92", "y_offset")
    _rename_key(object_, "93", "trigger_on_exit")
    _rename_key(object_, "94", "dynamic_block")
    _rename_key(object_, "95", "block_b_id")
    _rename_key(object_, "96", "disable_glow")
    _rename_key(object_, "97", "custom_rotation_speed")
    _rename_key(object_, "98", "disable_rotation")
    _rename_key(object_, "99", "multi_activate_orb")
    _rename_key(object_, "100", "enable_use_target")
    _rename_key(object_, "101", "target_pos_coordinates")
    _rename_key(object_, "102", "editor_disable")
    _rename_key(object_, "103", "high_detail")
    _rename_key(object_, "104", "multi_activate_trigger")
    _rename_key(object_, "105", "max_speed")
    _rename_key(object_, "106", "randomize_start")
    _rename_key(object_, "107", "animation_speed")
    _rename_key(object_, "108", "linked_group_id")
    # _rename_key(object, "109", "") # not documented
    _rename_key(object_, "110", "exit_static")
    _rename_key(object_, "111", "free_mode")
    _rename_key(object_, "112", "edit_camera_settings")
    _rename_key(object_, "113", "easing_free_mode")
    _rename_key(object_, "114", "padding")
    _rename_key(object_, "115", "ord")
    _rename_key(object_, "116", "no_effects")
    _rename_key(object_, "117", "reverse")
    # _rename_key(object, "118", "") # not documented
    # _rename_key(object, "119", "") # not documented
    _rename_key(object_, "120", "time_mod")
    _rename_key(object_, "121", "no_touch")
    # _rename_key(object, "122", "") # not documented
    # _rename_key(object, "123", "") # not documented
    # _rename_key(object, "124", "") # not documented
    # _rename_key(object, "125", "") # not documented
    # _rename_key(object, "126", "") # not documented
    # _rename_key(object, "127", "") # not documented
    _rename_key(object_, "128", "scale_x")
    _rename_key(object_, "129", "scale_y")  # not sure, documentation is bugged.
    # _rename_key(object, "130", "") # not documented
    _rename_key(object_, "131", "warp_y_angle")  # not sure, y is first which usually isn't the case.
    _rename_key(object_, "132", "warp_x_angle")  # not sure, x is last which usually isn't the case.
    # _rename_key(object, "155", "")  # Suspected to be something related to optimizing colors. Appears on all objects.
    # _rename_key(object, "156", "")  # Suspected to be something related to optimizing colors. Appears on all objects.


def _format_objects(data: str) -> list:
    data = data.split(";")[:-1]
    result = []

    key = None

    for object_string in data:
        object_string_split = object_string.split(",")

        object_ = {}

        for color_property in object_string_split:
            if key is None:
                key = color_property
            else:
                if key is None:
                    raise Exception("Format is incorrect.")

                object_[key] = color_property
                key = None

        _rename_object(object_)
        result.append(object_)

    return result


def _rename_level_start_object(level_start_object: dict) -> None:
    _rename_key(level_start_object, "kA1", "audio_track")
    _rename_key(level_start_object, "kA2", "gamemode")
    _rename_key(level_start_object, "kA3", "mini")
    _rename_key(level_start_object, "kA4", "speed")
    # _rename_key(result, "kA5", "obj_two_blending") # deprecated
    _rename_key(level_start_object, "kA6", "background_texture_id")
    _rename_key(level_start_object, "kA7", "ground_texture_id")
    _rename_key(level_start_object, "kA8", "dual_mode")
    _rename_key(level_start_object, "kA9", "is_start_pos_object")
    _rename_key(level_start_object, "kA10", "two_player_mode")
    _rename_key(level_start_object, "kA11", "flip_gravity")
    # _rename_key(result, "kA12", "color_three_blending") # not used
    _rename_key(level_start_object, "kA13", "song_offset")
    _rename_key(level_start_object, "kA14", "guidelines")
    _rename_key(level_start_object, "kA15", "fade_in")
    _rename_key(level_start_object, "kA16", "fade_out")
    _rename_key(level_start_object, "kA17", "ground_line")
    _rename_key(level_start_object, "kA18", "font")
    _rename_key(level_start_object, "kA19", "target_order")
    _rename_key(level_start_object, "kA20", "reverse_gameplay")
    _rename_key(level_start_object, "kA21", "disable")
    _rename_key(level_start_object, "kA22", "platformer_mode")
    # _rename_key(result, "kA23", "") # not documented
    # _rename_key(result, "kA24", "") # not documented
    _rename_key(level_start_object, "kA25", "middleground_texture_id")
    _rename_key(level_start_object, "kA26", "target_channel")
    _rename_key(level_start_object, "kA27", "allow_multi_rotation")
    _rename_key(level_start_object, "kA28", "mirror_mode")
    _rename_key(level_start_object, "kA29", "rotate_gameplay")
    # _rename_key(result, "kA30", "") # not documented
    _rename_key(level_start_object, "kA31", "enable_player_squeeze")
    _rename_key(level_start_object, "kA32", "fix_gravity_bug")
    _rename_key(level_start_object, "kA33", "fix_negative_scale")
    _rename_key(level_start_object, "kA34", "fix_robot_jump")
    _rename_key(level_start_object, "kA35", "reset_camera")
    _rename_key(level_start_object, "kA36", "spawn_group")
    _rename_key(level_start_object, "kA37", "dynamic_level_height")
    _rename_key(level_start_object, "kA38", "sort_groups")
    _rename_key(level_start_object, "kA39", "fix_radius_collision")
    _rename_key(level_start_object, "kA40", "enable_two_point_two_changes")
    _rename_key(level_start_object, "kA41", "allow_static_rotate")
    _rename_key(level_start_object, "kA42", "reverse_sync")
    _rename_key(level_start_object, "kA43", "no_time_penalty")
    # _rename_key(level_start_object, "kA44", "") # not documented
    _rename_key(level_start_object, "kA45", "decrease_boost_slide")

    _rename_key(level_start_object, "kS38", "colors")
    _rename_key(level_start_object, "kS39", "color_page")


def _format_level_start_object(data: str) -> dict:
    result = {}

    key = None

    for level_start_property in data.split(","):
        if key is None:
            key = level_start_property
        else:
            if key is None:
                raise Exception("Format is incorrect.")

            result[key] = level_start_property
            key = None

    _rename_level_start_object(result)

    result["colors"] = _format_colors(result["colors"])

    return result


def _format_level_data(data: str) -> dict:
    data = data.replace('-', '+').replace('_', '/')
    base64decoded = base64.b64decode(data.encode())
    decompressed = zlib.decompress(base64decoded[10:], -zlib.MAX_WBITS).decode()

    data_split = decompressed.split(";", 1)
    level_start: str = data_split[0]
    objects: str = data_split[1]

    result = {
        "level_start_object": _format_level_start_object(level_start),
        "objects": _format_objects(objects)
    }

    return result
