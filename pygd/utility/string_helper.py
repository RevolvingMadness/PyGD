# https://wyliemaster.github.io/gddocs/#/resources/client/level-components/inner-level-string


def decode_level_start_object_string(level_start_object_string: str) -> dict:
    result = {}

    properties = level_start_object_string.split(",")

    key = None

    for property in properties:
        if key is None:
            key = property
        else:
            result[key] = property
            key = None

    return result


# https://wyliemaster.github.io/gddocs/#/resources/client/level-components/level-object
def decode_object_string(object_string: str) -> dict:
    result = {}

    properties = object_string.split(",")

    key = None

    for property in properties:
        if key is None:
            key = property
        else:
            result[key] = property
            key = None

    return result
