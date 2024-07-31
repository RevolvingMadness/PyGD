# https://wyliemaster.github.io/gddocs/#/resources/client/level-components/inner-level-string


def decode_level_start_object_string(level_start_object_string: str) -> dict:
    result = {}

    level_keys_and_values = level_start_object_string.split(",")

    key = None

    for level_key_or_value in level_keys_and_values:
        if key is None:
            key = level_key_or_value
        else:
            result[key] = level_key_or_value
            key = None

    return result


def decode_color_string(colors_string: str) -> list:
    split_colors_string = colors_string.split("|")[:-1]
    result = []

    key = None

    for color_string in split_colors_string:
        split_color_string = color_string.split("_")

        color_json = {}

        for color_key_or_value in split_color_string:
            if key is None:
                key = color_key_or_value
            else:
                color_json[key] = color_key_or_value
                key = None

        result.append(color_json)

    return result


# https://wyliemaster.github.io/gddocs/#/resources/client/level-components/level-object
def decode_object_string(object_string: str) -> dict:
    result = {}

    object_keys_and_values = object_string.split(",")

    key = None

    for object_key_or_value in object_keys_and_values:
        if key is None:
            key = object_key_or_value
        else:
            result[key] = object_key_or_value
            key = None

    return result


def encode_object_json(object_json: dict) -> str:
    result = ""

    for key, value in object_json.items():
        result += f"{key},{value},"

    return result[:-1]
