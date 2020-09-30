from typing import List

from python.engine import Engine
from python.individual import Individual
from python.constraint import Constraint
from python.population import Population


class EngineImplV1(Engine):

    population: Population
    constraints: List[Constraint]

    # Initializer / Instance Attributes
    def __init__(self, pop_json: str, constraint_json: str):
        self.population = Population(Engine.create_initial_population(pop_json))
        self.constraints = self.create_constraint_list_from_json(constraint_json)
        pass

    def create_constraint_list_from_json(self, constraint_json: str) -> List[Constraint]:
        return super().create_constraint_list_from_json(constraint_json)

    @classmethod
    def create_initial_population(self, pop_json: str) -> List[Individual]:
        return super().create_initial_population(pop_json)

    def do_generate_new_generation(self):
        super().do_generate_new_generation()

    def do_evaluate_against_constraints(self, constraints: List[Constraint]) -> bool:
        return super().do_evaluate_against_constraints(constraints)


