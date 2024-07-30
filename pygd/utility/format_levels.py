import base64

from .format_level_data import _format_level_data
from .rename_key import _rename_key


def _base64_decode(data: str) -> str:
    return base64.b64decode(data).decode()


def _rename_level(level: dict) -> None:
    _rename_key(level, "k1", "id")
    _rename_key(level, "k2", "name")
    _rename_key(level, "k3", "description")
    _rename_key(level, "k4", "data")
    _rename_key(level, "k5", "creator")
    _rename_key(level, "k6", "user_id")
    _rename_key(level, "k7", "level_difficulty")
    _rename_key(level, "k8", "official_song_id")
    _rename_key(level, "k9", "rating")
    _rename_key(level, "k10", "rating_sum")
    _rename_key(level, "k11", "downloads")
    _rename_key(level, "k12", "completions")
    _rename_key(level, "k13", "is_editable")
    _rename_key(level, "k14", "has_been_verified")
    _rename_key(level, "k15", "has_been_uploaded")
    _rename_key(level, "k16", "level_version")
    _rename_key(level, "k17", "game_version")
    _rename_key(level, "k18", "attempts")
    _rename_key(level, "k19", "normal_mode_percentage")
    _rename_key(level, "k20", "practice_mode_percentage")
    _rename_key(level, "k21", "level_type")
    _rename_key(level, "k22", "like_rating")
    _rename_key(level, "k23", "length")  # unknown what format it is in (for me)
    _rename_key(level, "k24", "dislikes")
    _rename_key(level, "k25", "is_demon")
    _rename_key(level, "k26", "stars")
    _rename_key(level, "k27", "feature_score")
    # _rename_key(level, "k28", "") # unknown
    # _rename_key(level, "k29", "") # unknown
    # _rename_key(level, "k30", "") # unknown
    # _rename_key(level, "k31", "") # unknown
    # _rename_key(level, "k32", "") # unknown
    _rename_key(level, "k33", "is_auto")
    _rename_key(level, "k34", "replay_data")  # unknown how to decode (for me)
    _rename_key(level, "k35", "is_playable")  # not well documented
    _rename_key(level, "k36", "jumps")
    _rename_key(level, "k37", "required_coins")
    _rename_key(level, "k38", "is_unlocked")
    _rename_key(level, "k39", "level_size")
    _rename_key(level, "k40", "build_version")
    _rename_key(level, "k41", "password")
    _rename_key(level, "k42", "original")
    _rename_key(level, "k43", "is_two_player_mode")
    # _rename_key(level, "k44", "") # unknown
    _rename_key(level, "k45", "custom_song_id")
    _rename_key(level, "k46", "level_revision")
    _rename_key(level, "k47", "has_been_modified")
    _rename_key(level, "k48", "object_count")
    # _rename_key(level, "k49", "") # unknown
    _rename_key(level, "k50", "binary_version")
    _rename_key(level, "k51", "capacity_1")
    _rename_key(level, "k52", "capacity_2")
    _rename_key(level, "k53", "capacity_3")
    _rename_key(level, "k54", "capacity_4")
    # _rename_key(level, "k55", "") # unknown
    # _rename_key(level, "k56", "") # unknown
    # _rename_key(level, "k57", "") # unknown
    # _rename_key(level, "k58", "") # unknown
    # _rename_key(level, "k59", "") # unknown
    _rename_key(level, "k60", "account_id")
    _rename_key(level, "k61", "first_coin_has_been_acquired")
    _rename_key(level, "k62", "second_coin_has_been_acquired")
    _rename_key(level, "k63", "third_coin_has_been_acquired")
    _rename_key(level, "k64", "total_coins")
    _rename_key(level, "k65", "coins_are_verified")
    _rename_key(level, "k66", "requested_stars")
    _rename_key(level, "k67", "capacity_string")
    _rename_key(level, "k68", "anti_cheat_has_been_triggered")
    _rename_key(level, "k69", "has_high_object_count")
    # _rename_key(level, "k70", "") # unknown
    _rename_key(level, "k71", "mana_orb_percentage")
    _rename_key(level, "k72", "has_ldm")
    _rename_key(level, "k73", "ldm_is_enabled")
    _rename_key(level, "k74", "timely_id")
    _rename_key(level, "k75", "epic_rating")
    _rename_key(level, "k76", "demon_type")
    _rename_key(level, "k77", "is_gauntlet")
    _rename_key(level, "k78", "is_alt_game")
    _rename_key(level, "k79", "is_unlisted")
    _rename_key(level, "k80", "seconds_spent_editing")
    _rename_key(level, "k81", "seconds_spent_editing_total")  # includes copies
    _rename_key(level, "k82", "level_is_favorited")
    _rename_key(level, "k83", "level_order")
    _rename_key(level, "k84", "level_folder")
    _rename_key(level, "k85", "clicks")
    _rename_key(level, "k86", "player_time")
    _rename_key(level, "k87", "level_seed")  # unknown how to decode (for me)
    _rename_key(level, "k88", "level_progress")
    _rename_key(level, "k89", "vfDChk")  # ??? used to check for level completion ???
    _rename_key(level, "k90", "leaderboard_percentage")
    # _rename_key(level, "k91", "") # unknown, unknown
    # _rename_key(level, "k92", "") # unknown, unknown
    # _rename_key(level, "k93", "") # unknown, unlimited objects?
    # _rename_key(level, "k94", "") # unknown, platformer?
    _rename_key(level, "k95", "verification_time")
    # _rename_key(level, "k96", "") # unknown
    # _rename_key(level, "k97", "") # unknown
    # _rename_key(level, "k98", "") # unknown
    # _rename_key(level, "k99", "") # unknown
    # _rename_key(level, "k100", "") # unknown
    # _rename_key(level, "k101", "") # unknown, seems to be 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0. Seems to also correlate with k47
    # _rename_key(level, "k102", "") # unknown
    # _rename_key(level, "k103", "") # unknown
    _rename_key(level, "k104", "song_list")
    _rename_key(level, "k105", "sfx_list")
    # _rename_key(level, "k106", "") # unknown, corresponds to key 54 on the servers
    _rename_key(level, "k107", "best_time")
    _rename_key(level, "k108", "best_points")
    _rename_key(level, "k109", "local_best_times")
    _rename_key(level, "k110", "local_best_points")
    _rename_key(level, "k111", "platformer_seed")
    _rename_key(level, "k112", "shake_is_disabled")

    _rename_key(level, "kI1", "editor_camera_x_position")
    _rename_key(level, "kI2", "editor_camera_y_position")
    _rename_key(level, "kI3", "editor_camera_zoom")
    _rename_key(level, "kI4", "build_tab_page")
    _rename_key(level, "kI5", "build_tab")
    _rename_key(level, "kI6", "build_tab_pages")
    _rename_key(level, "kI7", "editor_layer")


def format_levels(unformatted_levels: dict) -> list:
    del unformatted_levels["_isArr"]

    result = []

    for key, level_json in unformatted_levels.items():
        level_json["_key"] = key
        del level_json["kCEK"]  # always 4, so no need to keep it

        _rename_level(level_json)

        if "data" in level_json:
            level_json["data"] = _format_level_data(level_json["data"])

        if "description" in level_json:
            level_json["description"] = base64.b64decode(level_json["description"]).decode()

        result.append(level_json)

    return result
