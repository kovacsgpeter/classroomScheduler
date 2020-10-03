from typing import List

from .constraint import Constraint
from .individual import Individual
from .population import Population
from .source_type import SourceType


class Engine(object):

    population: Population
    constraints: List[Constraint]

    def create_constraint_list_from_json(self, constraint_json: str) -> List[Constraint]:
        pass

    def create_initial_population(self, pop_json: str, source_type: SourceType) -> List[Individual]:
        pass

    def do_generate_new_generation(self):
        # self.population.do_reproduction(constraints)
        pass

    # returns false if there is no fit for constraints else true
    def do_evaluate_against_constraints(self, constraints: List[Constraint]) -> bool:
        pass
