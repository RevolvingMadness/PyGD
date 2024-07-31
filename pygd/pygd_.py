import base64
import xml.etree.ElementTree as ET
import zlib
from xml.dom import minidom

from pygd.level.levels import Levels
from pygd.utility.to_json import to_json


class PyGD:
    def __init__(self) -> None:
        self.file_contents: str | None = None
        self.levels: Levels | None = None
        self.binary_version: int | None = None
        self.local_lists: dict | None = None

    @staticmethod
    def _decode_dat_file(file_path: str) -> str:
        with open(file_path, "rb") as f:
            file_contents_encrypted = f.read()

            decrypted_data = bytes(map(lambda x: x ^ 11, file_contents_encrypted))
            decoded_data = base64.b64decode(decrypted_data, altchars=b"-_")
            file_contents_decrypted = zlib.decompress(decoded_data[10:], -zlib.MAX_WBITS)

            return file_contents_decrypted.decode()

    def load_save(self, file_path: str) -> None:
        unformatted_file_contents = self._decode_dat_file(file_path)
        xml_dom = minidom.parseString(unformatted_file_contents)

        self.file_contents = xml_dom.toprettyxml(indent="    ", encoding="utf-8").decode()
        root_element = ET.fromstring(self.file_contents)
        llm = to_json(root_element)
        self.levels = Levels(llm["LLM_01"])
        self.binary_version = llm["LLM_02"]
        self.local_lists = llm["LLM_03"]

        del self.local_lists["_isArr"]

    def write_to_file(self, file_path: str) -> None:
        with open(file_path, "w") as f:
            f.write(self.file_contents)

    def get_levels(self) -> Levels:
        return self.levels
