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
