from typing import List

from datapreprocessing.Individual import Individual


class Constraint(object):


    # Initializer / Instance Attributes
    def __init__(self):
        pass

    # could return a percentage in the future for more flexible processing
    def evaluate(self, individual: Individual) -> bool:
        pass