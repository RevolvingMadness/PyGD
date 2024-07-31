import xml.etree.ElementTree as ET
from typing import Any


def _to_integer(element: ET.Element) -> int:
    return int(element.text)


def _from_integer(integer: int) -> ET.Element:
    element = ET.Element("i")
    element.text = str(integer)

    return element


def _to_float(element: ET.Element) -> float:
    return float(element.text)


def _from_float(float_: float) -> ET.Element:
    element = ET.Element("r")
    element.text = str(float_)

    return element


def _to_string(element: ET.Element) -> str:
    return str(element.text)


def _from_string(string: str) -> ET.Element:
    element = ET.Element("s")
    element.text = string

    return element


def _to_json(element: ET.Element) -> dict:
    result = {}

    key = None

    for element_ in list(element):
        if element_.tag == "k":
            key = element_.text
        else:
            if key is None:
                raise Exception("File format is incorrect.")

            result[key] = _to_object(element_)
            key = None

    return result


def _from_json(json: dict) -> ET.Element:
    result = ET.Element("d")

    for key, value in json.items():
        key_element = ET.Element("k")
        key_element.text = key
        result.append(key_element)

        result.append(_from_object(value))

    return result


def _to_object(element: ET.Element) -> Any:
    if element.tag == "plist":  # skip "plist"
        return _to_object(element[0])

    if element.tag == "i":
        return _to_integer(element)
    elif element.tag == "r":
        return _to_float(element)
    elif element.tag == "s":
        return _to_string(element)
    elif element.tag in ["d", "dict"]:
        return _to_json(element)
    elif element.tag == "t":
        return True
    else:
        raise ValueError("Unknown tag '" + element.tag + "'")


def _from_object(object_: Any) -> ET.Element:
    if type(object_) is int:
        return _from_integer(object_)
    elif type(object_) is float:
        return _from_float(object_)
    elif type(object_) is str:
        return _from_string(object_)
    elif type(object_) is dict:
        return _from_json(object_)
    elif type(object_) is bool:
        return ET.Element("t")
    else:
        raise ValueError(f"Unknown object '{type(object_)}'")


def to_json(element: ET.Element) -> int | float | str | dict:
    return _to_object(element)


def from_object(object_: int | float | str | dict) -> ET.Element:
    dict_element = _from_object(object_)
    dict_element.tag = "dict"  # change from "d" -> "dict"

    plist_element = ET.Element("plist", {
        "version": "1.0",
        "gjver": "2.0"
    })
    plist_element.append(dict_element)

    return plist_element
