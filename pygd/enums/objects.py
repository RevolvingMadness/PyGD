class Objects:
    DEFAULT_BLOCK = 1
    SPIKE = 8
    HALF_SPIKE = 39
    START_POS = 31
    PLAYER_TRAIL_DISABLE = 33
    PLAYER_TRAIL_ENABLE = 32
    PULSING_STAR = 54
    PULSING_DIAMOND = 53
    PULSING_HEART = 52
    PULSING_CIRCLE_HOLLOW = 51
    PULSING_CIRCLE_FILLED = 50
    PULSING_MUSIC_NOTE = 60
    NORMAL_SAW = 89
    BIG_SAW = 88
    TINY_SAW = 98
    TINY_SPIKE = 103
    PULSING_EXCLAMATION_MARK = 133
    PULSING_ARROW = 132
    INVISIBLE_BLOCK = 1462
    INVISIBLE_TINY_SPIKE = 145
    INVISIBLE_SPIKE = 144
    BREAKABLE_BLOCK = 143
    PULSING_X = 150
    TINY_ELECTROMAN_SPIKE = 179
    HALF_ELECTROMAN_SPIKE = 178
    ELECTROMAN_SPIKE = 177
    SHADOW_TINY_SPIKE = 199
    HALF_SHADOW_SPIKE = 198
    PULSING_CIRCLE_FILLED_BIG = 397
    PULSING_SQUARE_HOLLOW = 496
    PULSING_SQUARE_BIG = 495
    PULSING_SQUARE = 148
    PULSING_RIGHT_ARROW = 494
    COIN = 1329
    LABEL = 1615
    COLLISION_BLOCK = 1816
    FORCE_BLOCK = 2069
    CHECKPOINT = 2063
    COLLISION_STATE_BLOCK = 3640
    OBJECT_CONTROL_BLOCK = 3655

    class LetterBlock:
        D = 1755
        J = 1813
        S = 1829
        H = 1859
        F = 2866

    class Trigger:
        COLOR = 221
        MOVE = 901
        PULSE = 1006
        ALPHA = 1007
        TOGGLE = 1049
        SPAWN = 1268
        FOLLOW = 1347
        ROTATE = 1346
        ANIMATE = 1585
        TOUCH = 1595
        STOP = 1616
        COUNT = 1611
        BACKGROUND_EFFECT_OFF = 18192
        BACKGROUND_EFFECT_ON = 1818
        PICKUP = 1817
        COLLISION = 1815
        FOLLOW_PLAYER_Y = 1814
        ON_DEATH = 1812
        INSTANT_COUNT = 1811
        REVERSE = 1917
        ENTER_EFFECT = 1915
        RANDOM = 1912
        TIME_WARP = 1935
        SONG = 1934
        PLAYER_CONTROL = 1932
        ADVANCED_RANDOM = 2068
        SCALE = 2067
        GRAVITY = 2066
        PARTICLE = 2065
        OPTIONS = 2899
        GRADIENT = 2903
        GAMEPLAY_OFFSET = 2901
        ARROW = 2900
        MIDDLEGROUND = 2999
        ENTER_SCALE = 3019
        ENTER_ROTATE = 3018
        ENTER_MOVE = 3017
        ADVANCED_FOLLOW = 3016
        CHANGE_BACKGROUND = 3029
        ENTER_STOP = 3023
        TELEPORT = 3022
        ENTER_TINT = 3021
        ENTER_FADE = 3020
        BASE_KEYFRAME = 3033
        KEYFRAME = 3032
        CHANGE_MIDDLEGROUND = 3031
        CHANGE_GROUND = 3030
        INSTANT_COLLISION = 3609
        SPAWN_PARTICLE = 3608
        SEQUENCE = 3607
        BACKGROUND_SPEED = 3606
        EDIT_SONG = 3605
        EVENT = 3604
        EDIT_SFX = 3603
        SFX = 3602
        END = 3600
        ITEM_EDIT = 3619
        RESET = 3618
        TIM_CONTROL = 3617
        TIM_EVENT = 3615
        TIME = 3614
        UI_SETTINGS = 3613
        MIDDLEGROUND_SPEED = 3612
        BPM = 3642
        PERSISTENT_ITEM_SETUP = 3641
        VISIBILITY_LINK = 3662
        RE_TARGET_ADVANCED_FOLLOW = 3661
        EDIT_ADVANCED_FOLLOW = 3660

        class EditArea:
            TINT = 3015
            FADE = 3014
            SCALE = 3013
            ROTATE = 3012
            MOVE = 3011

        class Area:
            MOVE = 3006
            ROTATE = 3007
            SCALE = 3008
            FADE = 3009
            TINT = 3010
            STOP = 3024

        class Camera:
            OFFSET = 1916
            STATIC = 1914
            ZOOM = 1913
            GUIDE = 2016
            ROTATE = 2015
            EDGE = 2062
            MODE = 2925

        class Shader:
            SHADER_GLITCH = 2909
            SHADER_SHOCK_LINE = 2907
            SHADER_SHOCK_WAVE = 2905
            SHADER = 2904
            SHADER_GRAY_SCALE = 2919
            SHADER_PINCH = 2917
            SHADER_BULGE = 2916
            SHADER_MOTION_BLUR = 2915
            SHADER_RADIAL_BLUR = 2914
            SHADER_LENS_CIRCLE = 2913
            SHADER_PIXELATE = 2912
            SHADER_CHROMATIC_GLITCH = 2911
            SHADER_CHROMATIC = 2910
            SHADER_SEPIA = 2920
            SHADER_INVERT_COLOR = 2921
            SHADER_HUE = 2922
            SHADER_EDIT_COLOR = 2923
            SHADER_SPLIT_SCREEN = 2924

    class Orb:
        YELLOW = 36
        BLUE = 84
        PINK = 141
        GREEN = 1022
        RED = 1333
        BLACK = 1330
        NORMAL_GRAVITY_DASH = 1704
        REVERSE_GRAVITY_DASH = 1751
        SPIDER = 3004
        TELEPORT = 3027

    class Pad:
        YELLOW = 35
        BLUE = 67
        PINK = 140
        RED = 1332
        SPIDER = 3005

    class Portal:
        class Dual:
            NORMAL = 287
            DUAL = 286

        class Gravity:
            NORMAL = 10
            FLIPPED = 11
            GREEN = 2926

        class Speed:
            HALF = 200
            NORMAL = 201
            DOUBLE = 202
            TRIPLE = 203
            QUADRUPLE = 1334

        class Size:
            NORMAL = 99
            MINI = 101

        class Mirror:
            NORMAL = 46
            FLIPPED = 45

        class Teleport:
            ENTRANCE = 747
            FAKE_ENTRANCE = 2902
            EXIT = 748  # maybe
            FAKE_EXIT = 2064

        class GameMode:
            CUBE = 12
            SHIP = 13
            BALL = 47
            UFO = 111
            WAVE = 660
            ROBOT = 745
            SPIDER = 1331
            SWINGCOPTER = 1933
