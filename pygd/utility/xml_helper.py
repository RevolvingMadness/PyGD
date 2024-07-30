from typing import Any


def to_xml(key: str, obj: Any) -> str:
    result = f",{key}"


def to_bool(value: int | None) -> bool | None:
    return None if value is None else bool(value)
