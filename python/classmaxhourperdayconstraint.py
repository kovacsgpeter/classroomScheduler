from typing import List

from python.constraint import Constraint
from python.week import Week, Slotv1


class ClassMaxHourPerDayConstraint(Constraint):
    max_hour: int

    def fill(self, params: List[object]):
        if params is not None:
            self.max_hour = params[0].max_hour

    # could return a percentage in the future for more flexible processing
    def evaluate(self, individual: Week) -> bool:
        slots: List[Slotv1] = individual.slots
        for slot in slots:
            if slot.slot_id.hour > self.max_hour:
                # TODO: log out day
                return False
        return True
