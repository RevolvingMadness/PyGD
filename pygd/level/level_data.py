import base64
import zlib

from .level_objects import LevelObjects
from .level_start_object import LevelStartObject
from ..utility.string_helper import decode_level_start_object_string, decode_level_objects_string


class LevelData:
    def __init__(self, level_data_string: str) -> None:
        level_data_string = level_data_string.replace("-", "+").replace("_", "/")
        base64_decoded = base64.b64decode(level_data_string.encode())
        zlib_decompressed = zlib.decompress(base64_decoded[10:], -zlib.MAX_WBITS).decode()

        data_split = zlib_decompressed.split(";", 1)
        self.level_start_object = LevelStartObject(decode_level_start_object_string(data_split[0]))
        self.level_objects = LevelObjects(decode_level_objects_string(data_split[1]))

    def pygd_encode(self) -> str:
        # Should probably actually encode it
        # but it works so I might not
        return f"{self.level_start_object.pygd_encode()};{self.level_objects.pygd_encode()}"
