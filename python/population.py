from typing import List

from python.individual import Individual
from python.constraint import Constraint


class Population(object):
    size: int
    population: List[Individual]
    fit: Individual

    # Initializer / Instance Attributes
    def __init__(self, size, initial_population: List[Individual]):
        self.population = initial_population
        self.size = size

    def add(self, individual: Individual):
        self.population.append(individual)

    def do_selection(self, population: List[Individual]) -> List[Individual]:
        # create a mating pool y copyiing individuals x times
        pass

    def do_reproduction(self, constraints: List[Constraint]):
        # create mating pool

        # crossover - create child with combining parents
        # mutation - mutate childs dna base on a given probabiliy
        # add to new population
        pass

    def get_fit(self) -> Individual:
        pass
