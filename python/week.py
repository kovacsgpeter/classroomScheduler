from random import random
from typing import List

from python.constraint import Constraint
from python.dayenum import DayEnum
from python.individual import Individual
from python.schoolclass import SchoolClass
from python.slot import Slot
from python.subject import Subject
from python.teacher import Teacher


class SlotId(object):

    day: DayEnum
    hour: int
    pass


class Slotv1(Slot):

    teacher: Teacher
    school_class: SchoolClass
    subject: Subject
    slot_id: SlotId

    # Initializer / Instance Attributes
    def __init__(self):
        pass


class Week(Individual):

    # Initializer / Instance Attributes
    def __init__(self):
        pass

    def calculateFitness(self, constraints: List[Constraint]) -> int:
        fitness = 0
        for constraint in constraints:
            fitness += 1 if constraint.evaluate(self) else 0
        return fitness

    def crossover(self, parent_1: Individual, parent_2: Individual) -> Individual:
        # get some random slots from each
        slots_from_1 = []
        num_of_slots = parent_1.slots.__len__()
        while self.slots.__len__() < num_of_slots:
            if bool(random.getrandbits(1)):
                slots_from_1.append(parent_1.slots.pop(random.randint(0, num_of_slots)))
            else:
                slots_from_1.append(parent_2.slots.pop(random.randint(0, num_of_slots)))

    def mutate(self, individual: Individual) -> Individual:
        # create random slots using a school - data  - pool where all teacher/class/subject is stored
        pass
