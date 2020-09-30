from typing import List

from python.constraint import Constraint
from python.subject import Subject
from python.week import Week, Slotv1


class ClassMaxHourPerDayPerSubjectConstraint(Constraint):
    max_hour_of_subject: int
    subject: Subject


    def fill(self, params: List[object], *args):
        # self.subject = subject
        if params is not None:
            self.max_hour_of_subject = params[0].max_hour_of_subject
            self.subject = params[1].subject

    # could return a percentage in the future for more flexible processing
    def evaluate(self, individual: Week) -> bool:
        slots: List[Slotv1] = individual.slots
        for slot in slots:
            if slot.slot_id.hour > self.max_hour:
                return False
        return True