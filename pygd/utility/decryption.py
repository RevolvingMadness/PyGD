import base64
import zlib


def decode_dat_file(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_contents_encrypted = f.read()

        decrypted_data = bytes(map(lambda x: x ^ 11, file_contents_encrypted))
        decoded_data = base64.b64decode(decrypted_data, altchars=b'-_')
        file_contents_decrypted = zlib.decompress(decoded_data[10:], -zlib.MAX_WBITS)

        return file_contents_decrypted.decode()
