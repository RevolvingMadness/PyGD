import base64

from pygd.level.level_data import LevelData
from pygd.utility.type_converter import to_bool, to_int


class Level:
    def __init__(self, level_json: dict) -> None:
        self._key: str | None = None

        description = level_json.get("k3")

        if description is not None:  # decode description from base64
            description = base64.b64decode(description).decode()

        data = level_json.get("k4")

        if data is not None:  # decode description from base64
            data = LevelData(data)

        self.properties = {
            "k1": level_json.get("k1"),  # id
            "k2": level_json.get("k2"),  # name
            "k3": description,  # look above
            "k4": data,  # data
            "k5": level_json.get("k5"),  # creator
            "k6": level_json.get("k6"),  # user_id
            "k7": level_json.get("k7"),  # level_difficulty
            "k8": level_json.get("k8"),  # official_song_id
            "k9": level_json.get("k9"),  # rating
            "k10": level_json.get("k10"),  # rating_sum
            "k11": level_json.get("k11"),  # downloads
            "k12": level_json.get("k12"),  # completions
            "k13": level_json.get("k13"),  # is_editable
            "k14": level_json.get("k14"),  # has_been_verified
            "k15": level_json.get("k15"),  # has_been_uploaded
            "k16": level_json.get("k16"),  # level_version
            "k17": level_json.get("k17"),  # game_version
            "k18": level_json.get("k18"),  # attempts
            "k19": level_json.get("k19"),  # normal_mode_percentage
            "k20": level_json.get("k20"),  # practice_mode_percentage
            "k21": level_json.get("k21"),  # level_type
            "k22": level_json.get("k22"),  # like_rating
            "k23": level_json.get("k23"),  # length
            "k24": level_json.get("k24"),  # dislikes
            "k25": level_json.get("k25"),  # is_demon
            "k26": level_json.get("k26"),  # stars
            "k27": level_json.get("k27"),  # feature_score
            # k28
            # k29
            # k30
            # k31
            # k32
            "k33": level_json.get("k33"),  # is_auto
            "k34": level_json.get("k34"),  # replay_data
            "k35": level_json.get("k35"),  # is_playable
            "k36": level_json.get("k36"),  # jumps
            "k37": level_json.get("k37"),  # required_coins
            "k38": level_json.get("k38"),  # is_unlocked
            "k39": level_json.get("k39"),  # level_size
            "k40": level_json.get("k40"),  # build_version
            "k41": level_json.get("k41"),  # password
            "k42": level_json.get("k42"),  # original_level_id
            "k43": level_json.get("k43"),  # is_two_player_mode
            # k44
            "k45": level_json.get("k45"),  # custom_song_id
            "k46": level_json.get("k46"),  # level_revision
            "k47": level_json.get("k47"),  # has_been_modified
            "k48": level_json.get("k48"),  # object_count
            # k49
            "k50": level_json.get("k50"),  # binary_version
            "k51": level_json.get("k51"),  # capacity_1
            "k52": level_json.get("k52"),  # capacity_2
            "k53": level_json.get("k53"),  # capacity_3
            "k54": level_json.get("k54"),  # capacity_4
            # k55
            # k56
            # k57
            # k58
            # k59
            "k60": level_json.get("k60"),  # account_id
            "k61": level_json.get("k61"),  # first_coin_has_been_acquired
            "k62": level_json.get("k62"),  # second_coin_has_been_acquired
            "k63": level_json.get("k63"),  # third_coin_has_been_acquired
            "k64": level_json.get("k64"),  # total_coins
            "k65": level_json.get("k65"),  # coins_are_verified
            "k66": level_json.get("k66"),  # requested_stars
            "k67": level_json.get("k67"),  # capacity_string
            "k68": level_json.get("k68"),  # anti_cheat_has_been_triggered
            "k69": level_json.get("k69"),  # has_high_object_count
            # k70
            "k71": level_json.get("k71"),  # mana_orb_percentage
            "k72": level_json.get("k72"),  # has_ldm
            "k73": level_json.get("k73"),  # ldm_is_enabled
            "k74": level_json.get("k74"),  # timely_id
            "k75": level_json.get("k75"),  # epic_rating
            "k76": level_json.get("k76"),  # demon_type
            "k77": level_json.get("k77"),  # is_gauntlet
            "k78": level_json.get("k78"),  # is_alt_game
            "k79": level_json.get("k79"),  # is_unlisted
            "k80": level_json.get("k80"),  # seconds_spent_editing
            "k81": level_json.get("k81"),  # seconds_spent_editing_total
            "k82": level_json.get("k82"),  # is_level_favorited
            "k83": level_json.get("k83"),  # level_order
            "k84": level_json.get("k84"),  # level_folder
            "k85": level_json.get("k85"),  # clicks
            "k86": level_json.get("k86"),  # player_time
            "k87": level_json.get("k87"),  # level_seed
            "k88": level_json.get("k88"),  # level_progress
            "k89": level_json.get("k89"),  # vfDChk
            "k90": level_json.get("k90"),  # leaderboard_percentage
            # k91
            # k92
            # k93 - unlimited Objects?
            # k94 - Platformer?
            "k95": level_json.get("k95"),  # verification_time
            # k96
            # k97
            # k98
            # k99
            # k100
            # k101 - seems to be 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0. Seems to also correlate with k47
            # k102
            # k103
            "k104": level_json.get("k104"),  # song_list
            "k105": level_json.get("k105"),  # sfx_list
            # k106 - corresponds to key 54 on the servers
            "k107": level_json.get("k107"),  # best_time
            "k108": level_json.get("k108"),  # best_points
            "k109": level_json.get("k109"),  # local_best_times
            "k110": level_json.get("k110"),  # local_best_points
            "k111": level_json.get("k111"),  # platformer_seed
            "k112": level_json.get("k112"),  # no_shake

            "kI1": level_json.get("kI1"),  # editor_camera_x_position
            "kI2": level_json.get("kI2"),  # editor_camera_y_position
            "kI3": level_json.get("kI3"),  # editor_camera_zoom
            "kI4": level_json.get("kI4"),  # build_tab_page
            "kI5": level_json.get("kI5"),  # build_tab
            "kI6": level_json.get("kI6"),  # build_tab_pages
            "kI7": level_json.get("kI7")  # editor_layer
        }

    @property
    def id(self) -> int:
        return to_int(self.properties["k1"])

    @property
    def name(self) -> str:
        return self.properties["k2"]

    @property
    def description(self) -> str:
        return self.properties["k3"]

    @property
    def data(self) -> LevelData:
        return self.properties["k4"]

    @property
    def creator(self) -> str:
        return self.properties["k5"]

    @property
    def user_id(self) -> int:
        return to_int(self.properties["k6"])

    @property
    def level_difficulty(self) -> int:
        return to_int(self.properties["k7"])

    @property
    def official_song_id(self) -> int:
        return to_int(self.properties["k8"])

    @property
    def rating(self) -> int:
        return to_int(self.properties["k9"])

    @property
    def rating_sum(self) -> int:
        return to_int(self.properties["k10"])

    @property
    def downloads(self) -> int:
        return to_int(self.properties["k11"])

    @property
    def completions(self) -> int:
        return to_int(self.properties["k12"])

    @property
    def is_editable(self) -> bool:
        return to_bool(self.properties["k13"])

    @property
    def has_been_verified(self) -> bool:
        return to_bool(self.properties["k14"])

    @property
    def has_been_uploaded(self) -> bool:
        return to_bool(self.properties["k15"])

    @property
    def level_version(self) -> int:
        return to_int(self.properties["k16"])

    @property
    def game_version(self) -> int:
        return to_int(self.properties["k17"])

    @property
    def attempts(self) -> int:
        return to_int(self.properties["k18"])

    @property
    def normal_mode_percentage(self) -> int:
        return to_int(self.properties["k19"])

    @property
    def practice_mode_percentage(self) -> int:
        return to_int(self.properties["k20"])

    @property
    def level_type(self) -> int:
        return to_int(self.properties["k21"])

    @property
    def like_rating(self) -> int:
        return to_int(self.properties["k22"])

    @property
    def length(self) -> int:
        return to_int(self.properties["k23"])

    @property
    def dislikes(self) -> int:
        return to_int(self.properties["k24"])

    @property
    def is_demon(self) -> bool:
        return to_bool(self.properties["k25"])

    @property
    def stars(self) -> int:
        return to_int(self.properties["k26"])

    @property
    def feature_score(self) -> int:
        return to_int(self.properties["k27"])

    @property
    def is_auto(self) -> bool:
        return to_bool(self.properties["k33"])

    @property
    def replay_data(self) -> str:  # I'm a little confused about this
        return self.properties["k34"]

    @property
    def is_playable(self) -> bool:
        return to_bool(self.properties["k35"])

    @property
    def jumps(self) -> int:
        return to_int(self.properties["k36"])

    @property
    def required_coins(self) -> int:
        return to_int(self.properties["k37"])

    @property
    def is_unlocked(self) -> bool:
        return to_bool(self.properties["k38"])

    @property
    def level_size(self) -> int:
        return to_int(self.properties["k39"])

    @property
    def build_version(self) -> int:
        return to_int(self.properties["k40"])

    @property
    def password(self) -> int:
        return to_int(self.properties["k41"])

    @property
    def original_level_id(self) -> int:
        return to_int(self.properties["k42"])

    @property
    def is_two_player_mode(self) -> bool:
        return to_bool(self.properties["k43"])

    @property
    def custom_song_id(self) -> int:
        return to_int(self.properties["k45"])

    @property
    def level_revision(self) -> int:
        return to_int(self.properties["k46"])

    @property
    def has_been_modified(self) -> bool:
        return to_bool(self.properties["k47"])

    @property
    def object_count(self) -> int:
        return to_int(self.properties["k48"])

    @property
    def binary_version(self) -> int:
        return to_int(self.properties["k50"])

    @property
    def capacity_1(self) -> int:  # I don't exactly know what this is for
        return to_int(self.properties["k51"])

    @property
    def capacity_2(self) -> int:  # I don't exactly know what this is for
        return to_int(self.properties["k52"])

    @property
    def capacity_3(self) -> int:  # I don't exactly know what this is for
        return to_int(self.properties["k53"])

    @property
    def capacity_4(self) -> int:  # I don't exactly know what this is for
        return to_int(self.properties["k54"])

    @property
    def account_id(self) -> int:
        return to_int(self.properties["k60"])

    @property
    def first_coin_has_been_acquired(self) -> bool:
        return to_bool(self.properties["k61"])

    @property
    def second_coin_has_been_acquired(self) -> bool:
        return to_bool(self.properties["k62"])

    @property
    def third_coin_has_been_acquired(self) -> bool:
        return to_bool(self.properties["k63"])

    @property
    def total_coins(self) -> int:
        return to_int(self.properties["k64"])

    @property
    def coins_are_verified(self) -> bool:
        return to_bool(self.properties["k65"])

    @property
    def requested_stars(self) -> int:
        return to_int(self.properties["k66"])

    @property
    def capacity_string(self) -> str:
        return self.properties["k67"]

    @property
    def anti_cheat_has_been_triggered(self) -> bool:
        return to_bool(self.properties["k68"])

    @property
    def has_high_object_count(self) -> bool:
        return to_bool(self.properties["k69"])

    @property
    def mana_orb_percentage(self) -> int:
        return to_int(self.properties["k71"])

    @property
    def has_ldm(self) -> bool:
        return to_bool(self.properties["k72"])

    @property
    def ldm_is_enabled(self) -> bool:
        return to_bool(self.properties["k73"])

    @property
    def timely_id(self) -> int:
        return to_int(self.properties["k74"])

    @property
    def epic_rating(self) -> int:
        return to_int(self.properties["k75"])

    @property
    def demon_type(self) -> int:
        return to_int(self.properties["k76"])

    @property
    def is_gauntlet(self) -> bool:
        return to_bool(self.properties["k77"])

    @property
    def is_alt_game(self) -> bool:
        return to_bool(self.properties["k78"])

    @property
    def is_unlisted(self) -> bool:
        return to_bool(self.properties["k79"])

    @property
    def seconds_spent_editing(self) -> int:
        return to_int(self.properties["k80"])

    @property
    def seconds_spent_editing_total(self) -> int:
        return to_int(self.properties["k81"])

    @property
    def is_level_favorited(self) -> bool:
        return to_bool(self.properties["k82"])

    @property
    def level_order(self) -> int:
        return to_int(self.properties["k83"])

    @property
    def level_folder(self) -> int:
        return to_int(self.properties["k84"])

    @property
    def clicks(self) -> int:
        return to_int(self.properties["k85"])

    @property
    def player_time(self) -> int:
        return to_int(self.properties["k86"])

    @property
    def level_seed(self) -> int:  # Not quite sure about the type
        return to_int(self.properties["k87"])

    @property
    def level_progress(self) -> str:
        return self.properties["k88"]

    @property
    def vfDChk(self) -> bool:
        return to_bool(self.properties["k89"])

    @property
    def leaderboard_percentage(self) -> int:
        return to_int(self.properties["k90"])

    @property
    def verification_time(self) -> int:
        return to_int(self.properties["k95"])

    @property
    def song_list(self) -> str:
        return self.properties["k104"]

    @property
    def sfx_list(self) -> str:
        return self.properties["k105"]

    @property
    def best_time(self) -> int:
        return to_int(self.properties["k107"])

    @property
    def best_points(self) -> int:
        return to_int(self.properties["k108"])

    @property
    def local_best_times(self) -> int:
        return to_int(self.properties["k109"])

    @property
    def local_best_points(self) -> int:
        return to_int(self.properties["k110"])

    @property
    def platformer_seed(self) -> int:
        return to_int(self.properties["k111"])

    @property
    def no_shake(self) -> bool:
        return to_bool(self.properties["k112"])

    @property
    def editor_camera_x_position(self) -> float:
        return self.properties["kI1"]

    @property
    def editor_camera_y_position(self) -> float:
        return self.properties["kI2"]

    @property
    def editor_camera_zoom(self) -> float:
        return self.properties["kI3"]

    @property
    def build_tab_page(self) -> int:
        return to_int(self.properties["kI4"])

    @property
    def build_tab(self) -> int:
        return to_int(self.properties["kI5"])

    @property
    def build_tab_pages(self) -> dict:  # May have to make a separate class for this
        return self.properties["kI6"]

    @property
    def editor_layer(self) -> float:
        return self.properties["kI7"]
