import enum
from random import randrange
from typing import List


class DayEnum(enum.Enum):

    def __init__(self, value):
        pass

    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"

    @classmethod
    def get_random_day(cls) -> str:
        return cls._member_names_[randrange(0, len(cls._member_names_))]

    @classmethod
    def get_days(cls) -> List[str]:
        return cls._member_names_
