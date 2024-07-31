import base64
import zlib

from .level_start_object import *
from .object import Object


class LevelData:
    def __init__(self, level_data_string: str) -> None:
        level_data_string = level_data_string.replace('-', '+').replace('_', '/')
        base64decoded = base64.b64decode(level_data_string.encode())
        decompressed = zlib.decompress(base64decoded[10:], -zlib.MAX_WBITS).decode()

        data_split = decompressed.split(";", 1)
        self.level_start_object = LevelStartObject(data_split[0])
        self.objects_string = data_split[1]
        self.objects = []

        object_string_list = self.objects_string.split(";")[:-1]

        for object_string in object_string_list:
            self.objects.append(Object(object_string))
