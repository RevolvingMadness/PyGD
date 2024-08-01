import base64
import gzip

from .level_objects import LevelObjects
from .level_start_object import LevelStartObject
from ..utility.string_helper import decode_level_start_object_string, decode_level_objects_string


# https://github.com/gd-programming/gd.docs/blob/main/docs/topics/levelstring_encoding_decoding.md
class LevelData:
    def __init__(self, level_data_string_encoded: str) -> None:
        urlsafe_base64_decoded = base64.urlsafe_b64decode(level_data_string_encoded.encode())
        decompressed = gzip.decompress(urlsafe_base64_decoded).decode()

        data_split = decompressed.split(";", 1)
        self.level_start_object = LevelStartObject(decode_level_start_object_string(data_split[0]))
        self.level_objects = LevelObjects(decode_level_objects_string(data_split[1]))

    def pygd_encode(self) -> str:
        level_data_string = f"{self.level_start_object.pygd_encode()};{self.level_objects.pygd_encode()}"

        compressed = gzip.compress(level_data_string.encode())
        urlsafe_base64_encoded = base64.urlsafe_b64encode(compressed)

        return urlsafe_base64_encoded.decode()
