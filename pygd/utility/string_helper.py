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


def decode_color_string(color_string: str) -> dict:
    result = {}
    color_keys_and_values = color_string.split("_")
    key = None

    for color_key_or_value in color_keys_and_values:
        if key is None:
            key = color_key_or_value
        else:
            result[key] = color_key_or_value
            key = None

    return result


def decode_colors_string(colors_string: str) -> list:
    result = []
    color_strings = colors_string.split("|")[:-1]

    for color_string in color_strings:
        result.append(decode_color_string(color_string))

    return result


def decode_level_object_string(level_object_string: str) -> dict:
    result = {}
    level_object_keys_and_values = level_object_string.split(",")
    key = None

    for level_object_key_or_value in level_object_keys_and_values:
        if key is None:
            key = level_object_key_or_value
        else:
            result[key] = level_object_key_or_value
            key = None

    return result


def decode_level_objects_string(level_objects_string: str) -> list:
    result = []
    level_object_strings = level_objects_string.split(";")[:-1]

    for level_object_string in level_object_strings:
        result.append(decode_level_object_string(level_object_string))

    return result
