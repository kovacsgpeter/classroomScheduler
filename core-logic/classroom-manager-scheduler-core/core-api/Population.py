from typing import List
from datapreprocessing.Individual import Individual


class Population(object):

    population: List[Individual]
    fit: Individual

    # Initializer / Instance Attributes
    def __init__(self, initial_population: List[Individual]):
        self.population = initial_population

    def add(self, individual: Individual):
        self.population.append(individual)

    def do_selection(self, population: List[Individual]) -> List[Individual]:
        pass

    def do_reproduction(self):
        # create mating pool
        mating_pool: List[Individual] = self.do_selection(self.population)
        # crossover - create child with combining parents
        # mutation - mutate childs dna base on a given probabiliy
        # add to new population
        pass

    def get_fit(self) -> Individual:
        pass
