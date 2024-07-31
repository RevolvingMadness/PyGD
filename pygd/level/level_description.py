import base64


class LevelDescription:
    def __init__(self, encoded_description: str) -> None:
        self.description = base64.b64decode(encoded_description).decode()

    def pygd_encode(self) -> str:
        return base64.b64encode(self.description.encode()).decode()
