from typing import List

from datapreprocessing.Constraint import Constraint
from datapreprocessing.Individual import Individual
from datapreprocessing.Population import Population


class Engine(object):

    population: Population
    constraints: List[Constraint]

    # Initializer / Instance Attributes
    def __init__(self, pop_json: str, constraint_json: str):
        self.population = Population(Engine.create_initial_population(pop_json))
        self.constraints = self.create_constraint_list_from_json(constraint_json)
        pass

    def create_constraint_list_from_json(self, constraint_json: str) -> List[Constraint]:
        pass

    @classmethod
    def create_initial_population(self, pop_json: str) -> List[Individual]:
        pass

    def do_generate_new_generation(self):
        self.population.do_reproduction()
        pass

    # returns false if there is no fit for constraints else true
    def do_evaluate_against_constraints(self, constraints: List[Constraint]) -> bool:
        pass
