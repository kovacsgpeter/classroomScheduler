from typing import List


class Teacher(object):

    def __init__(self, name: str, subjects: List[str]):
        self.name = name
        self.subjects = subjects

    name: str
    subjects: List[str]