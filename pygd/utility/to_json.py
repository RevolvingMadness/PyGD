import xml.etree.ElementTree as ET
from typing import Any


def _to_json_integer(element: ET.Element) -> int:
    return int(element.text)


def _to_json_float(element: ET.Element) -> float:
    return float(element.text)


def _to_json_string(element: ET.Element) -> str:
    return str(element.text)


def _to_json_dict(element: ET.Element) -> dict:
    result = {}

    key = None

    for element_ in list(element):
        if element_.tag == "k":
            key = element_.text
        else:
            if key is None:
                raise Exception("File format is incorrect.")

            result[key] = _to_json_element(element_)
            key = None

    return result


def _to_json_element(element: ET.Element) -> Any:
    if element.tag == "plist":  # skip "plist"
        return _to_json_element(element[0])
    elif element.tag == "i":
        return _to_json_integer(element)
    elif element.tag == "r":
        return _to_json_float(element)
    elif element.tag == "s":
        return _to_json_string(element)
    elif element.tag in ["d", "dict"]:
        return _to_json_dict(element)
    elif element.tag == "t":
        return {}
    else:
        raise ValueError("Unknown tag '" + element.tag + "'")


def to_json(element: ET.Element) -> int | float | str | dict:
    return _to_json_element(element)
