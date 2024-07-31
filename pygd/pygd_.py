import base64
import xml.etree.ElementTree as ET
import zlib
from xml.dom import minidom

import forbiddenfruit

from pygd.level.levels import Levels
from pygd.utility.builtinclass_encode import _int_encode_to_string, _float_encode_to_string, _str_encode_to_string
from pygd.utility.to_json import to_json


class PyGD:
    initialized = False

    def __init__(self, file_path: str) -> None:
        unformatted_file_contents = self._decode_dat_file(file_path)
        xml_dom = minidom.parseString(unformatted_file_contents)

        self.file_contents = xml_dom.toprettyxml(indent="    ", encoding="utf-8").decode()
        root_element = ET.fromstring(self.file_contents)
        llm = to_json(root_element)
        self.levels = Levels(llm["LLM_01"])
        self.binary_version = llm["LLM_02"]
        self.local_lists = llm["LLM_03"]

        del self.local_lists["_isArr"]
        self._initialize()

    @staticmethod
    def _decode_dat_file(file_path: str) -> str:
        with open(file_path, "rb") as f:
            file_contents_encrypted = f.read()

            decrypted_data = bytes(map(lambda x: x ^ 11, file_contents_encrypted))
            decoded_data = base64.b64decode(decrypted_data, altchars=b"-_")
            file_contents_decrypted = zlib.decompress(decoded_data[10:], -zlib.MAX_WBITS)

            return file_contents_decrypted.decode()

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as f:
            f.write(self.file_contents)

    def get_levels(self) -> Levels:
        return self.levels

    @staticmethod
    def _initialize() -> None:
        if PyGD.initialized:
            return

        forbiddenfruit.curse(int, "encode_to_string", _int_encode_to_string)
        forbiddenfruit.curse(float, "encode_to_string", _float_encode_to_string)
        forbiddenfruit.curse(str, "encode_to_string", _str_encode_to_string)
