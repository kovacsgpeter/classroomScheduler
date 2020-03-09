from typing import List

from .constraint import Constraint


class Slot(object):
    pass


class Individual(object):

    slots: List[Slot]
    fitness: int

    # Initializer / Instance Attributes
    def __init__(self):
        pass

    def calculateFitness(self, constraints: List[Constraint]):
        pass

    def crossover(self, parent_1: 'Individual', parent_2: 'Individual') -> 'Individual':
        pass

    def mutate(self, individual: 'Individual') -> 'Individual':
        pass
