import copy
from random import random
from typing import List

from python.individual import Individual
from python.constraint import Constraint
from python.population import Population


class TimeTablePopulation(Population):

    def add(self, individual: Individual):
        super().add(individual)

    def do_selection(self, population: List[Individual]) -> List[Individual]:
        mating_pool = []
        for individual in population:
            for i in range(individual.fitness):
                mating_pool.append(copy.deepcopy(individual))

        return mating_pool

    def do_reproduction(self, constraints: List[Constraint]):

        mating_pool = self.do_selection(self.population)
        self.population.clear()

        while len(self.population) < self.size:
            individual = Individual().crossover(mating_pool.pop(random.randint(0, len(mating_pool))),
                                                mating_pool.pop(random.randint(0, len(mating_pool) - 1)))
            individual.mutate(None)
            self.population.append(individual)

    def get_fit(self) -> Individual:
        return super().get_fit()

