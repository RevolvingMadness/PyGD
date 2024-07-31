def to_bool(value: int | None) -> bool | None:
    return None if value is None else bool(value)


def to_int(value: str | None) -> int | None:
    return None if value is None else int(value)
