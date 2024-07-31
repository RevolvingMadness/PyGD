import base64
import os
import shutil
import xml.etree.ElementTree as ET
import zlib
from datetime import datetime
from xml.dom import minidom

import forbiddenfruit

from pygd.level.levels import Levels
from pygd.utility.builtinclass_encode import _int_pygd_encode, _float_pygd_encode, _str_pygd_encode, _dict_pygd_encode
from pygd.utility.element_helper import to_json, from_object


class PyGD:
    initialized = False

    def __init__(self, gd_save_directory: str = None) -> None:
        self._gd_save_directory = gd_save_directory
        self._cc_local_levels_path = os.path.join(self._gd_save_directory, "CCLocalLevels.dat")

        with open(self._cc_local_levels_path, "rb") as f:
            file_contents_bytes = f.read()

        unformatted_file_contents = PyGD._decrypt_dat_file(file_contents_bytes)
        xml_dom = minidom.parseString(unformatted_file_contents)

        file_contents_string = xml_dom.toprettyxml(indent="    ", encoding="utf-8").decode()
        root_element = ET.fromstring(file_contents_string)
        llm = to_json(root_element)
        self.levels = Levels(llm["LLM_01"])
        self.binary_version = llm["LLM_02"]
        self.local_lists = llm["LLM_03"]

        del self.local_lists["_isArr"]
        self._initialize()

    @staticmethod
    def _decrypt_dat_file(file_contents: bytes) -> str:
        xor_shifted = bytes(map(lambda x: x ^ 11, file_contents))
        base64_decoded = base64.b64decode(xor_shifted, altchars=b"-_")
        zlib_decompressed = zlib.decompress(base64_decoded[10:], -zlib.MAX_WBITS)
        return zlib_decompressed.decode()

    @staticmethod
    def _encrypt_dat_file(file_contents: str) -> bytes:
        zlib_compressed = zlib.compress(file_contents.encode(), level=9)
        base64_encoded = base64.b64encode(zlib_compressed, altchars=b"-_")
        xor_shifted = bytes(map(lambda x: x ^ 11, base64_encoded))
        return xor_shifted

    def get_levels(self) -> Levels:
        return self.levels

    @staticmethod
    def _initialize() -> None:
        if PyGD.initialized:
            return

        forbiddenfruit.curse(int, "pygd_encode", _int_pygd_encode)
        forbiddenfruit.curse(float, "pygd_encode", _float_pygd_encode)
        forbiddenfruit.curse(str, "pygd_encode", _str_pygd_encode)
        forbiddenfruit.curse(dict, "pygd_encode", _dict_pygd_encode)

    def overwrite_gd_save(self, i_accept_the_risks: bool = False):
        if not i_accept_the_risks:
            raise Exception("You need to set \"i_accept_the_risks\" to \"True\"")

        if self._gd_save_directory is None:
            raise Exception("Cannot overwrite geometry dash save. No save folder was passed as an argument.")

        if not os.path.exists("backups/"):
            os.makedirs("backups/")

        date_time = datetime.now()
        formatted_date_time = date_time.strftime("%Y-%m-%d %I.%M.%S %p")
        new_cc_local_levels_path = os.path.join(self._gd_save_directory, f"CCLocalLevels ({formatted_date_time}).dat")

        if os.path.exists(self._cc_local_levels_path):
            os.rename(self._cc_local_levels_path, new_cc_local_levels_path)
            shutil.move(new_cc_local_levels_path, "backups/")

        contents_element = from_object({
            "LLM_01": self.levels.pygd_encode(),
            "LLM_02": self.binary_version.pygd_encode(),
            "LLM_03": self.local_lists.pygd_encode()
        })

        file_contents = ET.tostring(contents_element).decode()

        with open(self._cc_local_levels_path, "w") as f:
            f.write(file_contents)
