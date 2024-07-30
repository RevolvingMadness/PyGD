def _rename_key(json: dict, old_key: str, new_key: str) -> bool:
    if old_key not in json:
        return False

    json[new_key] = json[old_key]
    del json[old_key]

    return True
