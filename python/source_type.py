from enum import Enum


class SourceType(Enum):
    file = "file"
    json = "json"

    def __init__(self, value):
        pass