from pygd.level.level_data import LevelData
from pygd.level.level_description import LevelDescription
from pygd.utility.type_converter import to_bool, to_int


class Level:
    def __init__(self, level_json: dict) -> None:
        self._key: str | None = None

        self._json = level_json

        description = self._json.get("k3")
        if description is not None:
            self._json["k3"] = LevelDescription(description)

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

    @id.setter
    def id(self, value: int) -> None:
        self._json["k1"] = value

    @name.setter
    def name(self, value: str) -> None:
        self._json["k2"] = value

    @description.setter
    def description(self, value: str) -> None:
        self._json["k3"] = value

    @data.setter
    def data(self, value: LevelData) -> None:
        self._json["k4"] = value

    @creator.setter
    def creator(self, value: str) -> None:
        self._json["k5"] = value

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._json["k6"] = value

    @level_difficulty.setter
    def level_difficulty(self, value: int) -> None:
        self._json["k7"] = value

    @official_song_id.setter
    def official_song_id(self, value: int) -> None:
        self._json["k8"] = value

    @rating.setter
    def rating(self, value: int) -> None:
        self._json["k9"] = value

    @rating_sum.setter
    def rating_sum(self, value: int) -> None:
        self._json["k10"] = value

    @downloads.setter
    def downloads(self, value: int) -> None:
        self._json["k11"] = value

    @completions.setter
    def completions(self, value: int) -> None:
        self._json["k12"] = value

    @is_editable.setter
    def is_editable(self, value: bool) -> None:
        self._json["k13"] = value

    @has_been_verified.setter
    def has_been_verified(self, value: bool) -> None:
        self._json["k14"] = value

    @has_been_uploaded.setter
    def has_been_uploaded(self, value: bool) -> None:
        self._json["k15"] = value

    @level_version.setter
    def level_version(self, value: int) -> None:
        self._json["k16"] = value

    @game_version.setter
    def game_version(self, value: int) -> None:
        self._json["k17"] = value

    @attempts.setter
    def attempts(self, value: int) -> None:
        self._json["k18"] = value

    @normal_mode_percentage.setter
    def normal_mode_percentage(self, value: int) -> None:
        self._json["k19"] = value

    @practice_mode_percentage.setter
    def practice_mode_percentage(self, value: int) -> None:
        self._json["k20"] = value

    @level_type.setter
    def level_type(self, value: int) -> None:
        self._json["k21"] = value

    @like_rating.setter
    def like_rating(self, value: int) -> None:
        self._json["k22"] = value

    @length.setter
    def length(self, value: int) -> None:
        self._json["k23"] = value

    @dislikes.setter
    def dislikes(self, value: int) -> None:
        self._json["k24"] = value

    @is_demon.setter
    def is_demon(self, value: bool) -> None:
        self._json["k25"] = value

    @stars.setter
    def stars(self, value: int) -> None:
        self._json["k26"] = value

    @feature_score.setter
    def feature_score(self, value: int) -> None:
        self._json["k27"] = value

    @is_auto.setter
    def is_auto(self, value: bool) -> None:
        self._json["k33"] = value

    @replay_data.setter
    def replay_data(self, value: str) -> None:
        self._json["k34"] = value

    @is_playable.setter
    def is_playable(self, value: bool) -> None:
        self._json["k35"] = value

    @jumps.setter
    def jumps(self, value: int) -> None:
        self._json["k36"] = value

    @required_coins.setter
    def required_coins(self, value: int) -> None:
        self._json["k37"] = value

    @is_unlocked.setter
    def is_unlocked(self, value: bool) -> None:
        self._json["k38"] = value

    @level_size.setter
    def level_size(self, value: int) -> None:
        self._json["k39"] = value

    @build_version.setter
    def build_version(self, value: int) -> None:
        self._json["k40"] = value

    @password.setter
    def password(self, value: int) -> None:
        self._json["k41"] = value

    @original_level_id.setter
    def original_level_id(self, value: int) -> None:
        self._json["k42"] = value

    @is_two_player_mode.setter
    def is_two_player_mode(self, value: bool) -> None:
        self._json["k43"] = value

    @custom_song_id.setter
    def custom_song_id(self, value: int) -> None:
        self._json["k45"] = value

    @level_revision.setter
    def level_revision(self, value: int) -> None:
        self._json["k46"] = value

    @has_been_modified.setter
    def has_been_modified(self, value: bool) -> None:
        self._json["k47"] = value

    @object_count.setter
    def object_count(self, value: int) -> None:
        self._json["k48"] = value

    @binary_version.setter
    def binary_version(self, value: int) -> None:
        self._json["k50"] = value

    @capacity_1.setter
    def capacity_1(self, value: int) -> None:
        self._json["k51"] = value

    @capacity_2.setter
    def capacity_2(self, value: int) -> None:
        self._json["k52"] = value

    @capacity_3.setter
    def capacity_3(self, value: int) -> None:
        self._json["k53"] = value

    @capacity_4.setter
    def capacity_4(self, value: int) -> None:
        self._json["k54"] = value

    @account_id.setter
    def account_id(self, value: int) -> None:
        self._json["k60"] = value

    @first_coin_has_been_acquired.setter
    def first_coin_has_been_acquired(self, value: bool) -> None:
        self._json["k61"] = value

    @second_coin_has_been_acquired.setter
    def second_coin_has_been_acquired(self, value: bool) -> None:
        self._json["k62"] = value

    @third_coin_has_been_acquired.setter
    def third_coin_has_been_acquired(self, value: bool) -> None:
        self._json["k63"] = value

    @total_coins.setter
    def total_coins(self, value: int) -> None:
        self._json["k64"] = value

    @coins_are_verified.setter
    def coins_are_verified(self, value: bool) -> None:
        self._json["k65"] = value

    @requested_stars.setter
    def requested_stars(self, value: int) -> None:
        self._json["k66"] = value

    @capacity_string.setter
    def capacity_string(self, value: str) -> None:
        self._json["k67"] = value

    @anti_cheat_has_been_triggered.setter
    def anti_cheat_has_been_triggered(self, value: bool) -> None:
        self._json["k68"] = value

    @has_high_object_count.setter
    def has_high_object_count(self, value: bool) -> None:
        self._json["k69"] = value

    @mana_orb_percentage.setter
    def mana_orb_percentage(self, value: int) -> None:
        self._json["k71"] = value

    @has_ldm.setter
    def has_ldm(self, value: bool) -> None:
        self._json["k72"] = value

    @ldm_is_enabled.setter
    def ldm_is_enabled(self, value: bool) -> None:
        self._json["k73"] = value

    @timely_id.setter
    def timely_id(self, value: int) -> None:
        self._json["k74"] = value

    @epic_rating.setter
    def epic_rating(self, value: int) -> None:
        self._json["k75"] = value

    @demon_type.setter
    def demon_type(self, value: int) -> None:
        self._json["k76"] = value

    @is_gauntlet.setter
    def is_gauntlet(self, value: bool) -> None:
        self._json["k77"] = value

    @is_alt_game.setter
    def is_alt_game(self, value: bool) -> None:
        self._json["k78"] = value

    @is_unlisted.setter
    def is_unlisted(self, value: bool) -> None:
        self._json["k79"] = value

    @seconds_spent_editing.setter
    def seconds_spent_editing(self, value: int) -> None:
        self._json["k80"] = value

    @seconds_spent_editing_total.setter
    def seconds_spent_editing_total(self, value: int) -> None:
        self._json["k81"] = value

    @is_level_favorited.setter
    def is_level_favorited(self, value: bool) -> None:
        self._json["k82"] = value

    @level_order.setter
    def level_order(self, value: int) -> None:
        self._json["k83"] = value

    @level_folder.setter
    def level_folder(self, value: int) -> None:
        self._json["k84"] = value

    @clicks.setter
    def clicks(self, value: int) -> None:
        self._json["k85"] = value

    @player_time.setter
    def player_time(self, value: int) -> None:
        self._json["k86"] = value

    @level_seed.setter
    def level_seed(self, value: int) -> None:
        self._json["k87"] = value

    @level_progress.setter
    def level_progress(self, value: str) -> None:
        self._json["k88"] = value

    @vfDChk.setter
    def vfDChk(self, value: bool) -> None:
        self._json["k89"] = value

    @leaderboard_percentage.setter
    def leaderboard_percentage(self, value: int) -> None:
        self._json["k90"] = value

    @verification_time.setter
    def verification_time(self, value: int) -> None:
        self._json["k95"] = value

    @song_list.setter
    def song_list(self, value: str) -> None:
        self._json["k104"] = value

    @sfx_list.setter
    def sfx_list(self, value: str) -> None:
        self._json["k105"] = value

    @best_time.setter
    def best_time(self, value: int) -> None:
        self._json["k107"] = value

    @best_points.setter
    def best_points(self, value: int) -> None:
        self._json["k108"] = value

    @local_best_times.setter
    def local_best_times(self, value: int) -> None:
        self._json["k109"] = value

    @local_best_points.setter
    def local_best_points(self, value: int) -> None:
        self._json["k110"] = value

    @platformer_seed.setter
    def platformer_seed(self, value: int) -> None:
        self._json["k111"] = value

    @no_shake.setter
    def no_shake(self, value: bool) -> None:
        self._json["k112"] = value

    @editor_camera_x_position.setter
    def editor_camera_x_position(self, value: float) -> None:
        self._json["kI1"] = value

    @editor_camera_y_position.setter
    def editor_camera_y_position(self, value: float) -> None:
        self._json["kI2"] = value

    @editor_camera_zoom.setter
    def editor_camera_zoom(self, value: float) -> None:
        self._json["kI3"] = value

    @build_tab_page.setter
    def build_tab_page(self, value: int) -> None:
        self._json["kI4"] = value

    @build_tab.setter
    def build_tab(self, value: int) -> None:
        self._json["kI5"] = value

    @build_tab_pages.setter
    def build_tab_pages(self, value: dict) -> None:
        self._json["kI6"] = value

    @editor_layer.setter
    def editor_layer(self, value: float) -> None:
        self._json["kI7"] = value

    def pygd_encode(self) -> dict:
        result = {}

        for key, value in self._json.items():
            result[key] = value.pygd_encode()

        return result
