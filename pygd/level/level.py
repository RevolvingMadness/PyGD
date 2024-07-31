import base64

from pygd.level.level_data import LevelData
from pygd.utility.type_converter import to_bool, to_int


class Level:
    def __init__(self, level_json: dict) -> None:
        self._key: str | None = None

        self._json = level_json

        description = self._json.get("k3")
        if description is not None:
            description = base64.b64decode(description).decode()
            self._json["k3"] = description

        data = self._json.get("k4")
        if data is not None:
            self._json["k4"] = LevelData(data)

    @property
    def id(self) -> int:
        return to_int(self._json.get("k1"))

    @property
    def name(self) -> str:
        return self._json.get("k2")

    @property
    def description(self) -> str:
        return self._json.get("k3")

    @property
    def data(self) -> LevelData:
        return self._json.get("k4")

    @property
    def creator(self) -> str:
        return self._json.get("k5")

    @property
    def user_id(self) -> int:
        return to_int(self._json.get("k6"))

    @property
    def level_difficulty(self) -> int:
        return to_int(self._json.get("k7"))

    @property
    def official_song_id(self) -> int:
        return to_int(self._json.get("k8"))

    @property
    def rating(self) -> int:
        return to_int(self._json.get("k9"))

    @property
    def rating_sum(self) -> int:
        return to_int(self._json.get("k10"))

    @property
    def downloads(self) -> int:
        return to_int(self._json.get("k11"))

    @property
    def completions(self) -> int:
        return to_int(self._json.get("k12"))

    @property
    def is_editable(self) -> bool:
        return to_bool(self._json.get("k13"))

    @property
    def has_been_verified(self) -> bool:
        return to_bool(self._json.get("k14"))

    @property
    def has_been_uploaded(self) -> bool:
        return to_bool(self._json.get("k15"))

    @property
    def level_version(self) -> int:
        return to_int(self._json.get("k16"))

    @property
    def game_version(self) -> int:
        return to_int(self._json.get("k17"))

    @property
    def attempts(self) -> int:
        return to_int(self._json.get("k18"))

    @property
    def normal_mode_percentage(self) -> int:
        return to_int(self._json.get("k19"))

    @property
    def practice_mode_percentage(self) -> int:
        return to_int(self._json.get("k20"))

    @property
    def level_type(self) -> int:
        return to_int(self._json.get("k21"))

    @property
    def like_rating(self) -> int:
        return to_int(self._json.get("k22"))

    @property
    def length(self) -> int:
        return to_int(self._json.get("k23"))

    @property
    def dislikes(self) -> int:
        return to_int(self._json.get("k24"))

    @property
    def is_demon(self) -> bool:
        return to_bool(self._json.get("k25"))

    @property
    def stars(self) -> int:
        return to_int(self._json.get("k26"))

    @property
    def feature_score(self) -> int:
        return to_int(self._json.get("k27"))

    @property
    def is_auto(self) -> bool:
        return to_bool(self._json.get("k33"))

    @property
    def replay_data(self) -> str:  # I'm a little confused about this
        return self._json.get("k34")

    @property
    def is_playable(self) -> bool:
        return to_bool(self._json.get("k35"))

    @property
    def jumps(self) -> int:
        return to_int(self._json.get("k36"))

    @property
    def required_coins(self) -> int:
        return to_int(self._json.get("k37"))

    @property
    def is_unlocked(self) -> bool:
        return to_bool(self._json.get("k38"))

    @property
    def level_size(self) -> int:
        return to_int(self._json.get("k39"))

    @property
    def build_version(self) -> int:
        return to_int(self._json.get("k40"))

    @property
    def password(self) -> int:
        return to_int(self._json.get("k41"))

    @property
    def original_level_id(self) -> int:
        return to_int(self._json.get("k42"))

    @property
    def is_two_player_mode(self) -> bool:
        return to_bool(self._json.get("k43"))

    @property
    def custom_song_id(self) -> int:
        return to_int(self._json.get("k45"))

    @property
    def level_revision(self) -> int:
        return to_int(self._json.get("k46"))

    @property
    def has_been_modified(self) -> bool:
        return to_bool(self._json.get("k47"))

    @property
    def object_count(self) -> int:
        return to_int(self._json.get("k48"))

    @property
    def binary_version(self) -> int:
        return to_int(self._json.get("k50"))

    @property
    def capacity_1(self) -> int:  # I don't exactly know what this is for
        return to_int(self._json.get("k51"))

    @property
    def capacity_2(self) -> int:  # I don't exactly know what this is for
        return to_int(self._json.get("k52"))

    @property
    def capacity_3(self) -> int:  # I don't exactly know what this is for
        return to_int(self._json.get("k53"))

    @property
    def capacity_4(self) -> int:  # I don't exactly know what this is for
        return to_int(self._json.get("k54"))

    @property
    def account_id(self) -> int:
        return to_int(self._json.get("k60"))

    @property
    def first_coin_has_been_acquired(self) -> bool:
        return to_bool(self._json.get("k61"))

    @property
    def second_coin_has_been_acquired(self) -> bool:
        return to_bool(self._json.get("k62"))

    @property
    def third_coin_has_been_acquired(self) -> bool:
        return to_bool(self._json.get("k63"))

    @property
    def total_coins(self) -> int:
        return to_int(self._json.get("k64"))

    @property
    def coins_are_verified(self) -> bool:
        return to_bool(self._json.get("k65"))

    @property
    def requested_stars(self) -> int:
        return to_int(self._json.get("k66"))

    @property
    def capacity_string(self) -> str:
        return self._json.get("k67")

    @property
    def anti_cheat_has_been_triggered(self) -> bool:
        return to_bool(self._json.get("k68"))

    @property
    def has_high_object_count(self) -> bool:
        return to_bool(self._json.get("k69"))

    @property
    def mana_orb_percentage(self) -> int:
        return to_int(self._json.get("k71"))

    @property
    def has_ldm(self) -> bool:
        return to_bool(self._json.get("k72"))

    @property
    def ldm_is_enabled(self) -> bool:
        return to_bool(self._json.get("k73"))

    @property
    def timely_id(self) -> int:
        return to_int(self._json.get("k74"))

    @property
    def epic_rating(self) -> int:
        return to_int(self._json.get("k75"))

    @property
    def demon_type(self) -> int:
        return to_int(self._json.get("k76"))

    @property
    def is_gauntlet(self) -> bool:
        return to_bool(self._json.get("k77"))

    @property
    def is_alt_game(self) -> bool:
        return to_bool(self._json.get("k78"))

    @property
    def is_unlisted(self) -> bool:
        return to_bool(self._json.get("k79"))

    @property
    def seconds_spent_editing(self) -> int:
        return to_int(self._json.get("k80"))

    @property
    def seconds_spent_editing_total(self) -> int:
        return to_int(self._json.get("k81"))

    @property
    def is_level_favorited(self) -> bool:
        return to_bool(self._json.get("k82"))

    @property
    def level_order(self) -> int:
        return to_int(self._json.get("k83"))

    @property
    def level_folder(self) -> int:
        return to_int(self._json.get("k84"))

    @property
    def clicks(self) -> int:
        return to_int(self._json.get("k85"))

    @property
    def player_time(self) -> int:
        return to_int(self._json.get("k86"))

    @property
    def level_seed(self) -> int:  # Not quite sure about the type
        return to_int(self._json.get("k87"))

    @property
    def level_progress(self) -> str:
        return self._json.get("k88")

    # noinspection PyPep8Naming
    @property
    def vfDChk(self) -> bool:
        return to_bool(self._json.get("k89"))

    @property
    def leaderboard_percentage(self) -> int:
        return to_int(self._json.get("k90"))

    @property
    def verification_time(self) -> int:
        return to_int(self._json.get("k95"))

    @property
    def song_list(self) -> str:
        return self._json.get("k104")

    @property
    def sfx_list(self) -> str:
        return self._json.get("k105")

    @property
    def best_time(self) -> int:
        return to_int(self._json.get("k107"))

    @property
    def best_points(self) -> int:
        return to_int(self._json.get("k108"))

    @property
    def local_best_times(self) -> int:
        return to_int(self._json.get("k109"))

    @property
    def local_best_points(self) -> int:
        return to_int(self._json.get("k110"))

    @property
    def platformer_seed(self) -> int:
        return to_int(self._json.get("k111"))

    @property
    def no_shake(self) -> bool:
        return to_bool(self._json.get("k112"))

    @property
    def editor_camera_x_position(self) -> float:
        return self._json.get("kI1")

    @property
    def editor_camera_y_position(self) -> float:
        return self._json.get("kI2")

    @property
    def editor_camera_zoom(self) -> float:
        return self._json.get("kI3")

    @property
    def build_tab_page(self) -> int:
        return to_int(self._json.get("kI4"))

    @property
    def build_tab(self) -> int:
        return to_int(self._json.get("kI5"))

    @property
    def build_tab_pages(self) -> dict:  # May have to make a separate class for this
        return self._json.get("kI6")

    @property
    def editor_layer(self) -> float:
        return self._json.get("kI7")
