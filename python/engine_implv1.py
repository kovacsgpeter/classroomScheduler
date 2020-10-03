from enum import Enum
from random import randrange
from typing import List

from python.core_service import CoreService
from python.dayenum import DayEnum
from python.engine import Engine
from python.individual import Individual
from python.constraint import Constraint
from python.population import Population
from python.schooldata import SchoolData
from python.source_type import SourceType
from python.week import Week, Slotv1, SlotId



class EngineImplV1(Engine):

    def create_constraint_list_from_json(self, constraint_json: str) -> List[Constraint]:
        return super().create_constraint_list_from_json(constraint_json)

    def create_initial_population(self, pop: str, source_type: SourceType) -> Population:
        data: SchoolData = None
        if source_type == SourceType.file:
            data = CoreService.get_processed_json(CoreService.read_json(pop))
        elif source_type == SourceType.json:
            data = CoreService.get_processed_json(pop)

        slot1: Slotv1 = self.create_random_slot(data)
        slot2: Slotv1 = self.create_random_slot(data)

        week: Week = Week()
        return None

    def get_random_element(self, size: int) -> int:
        return randrange(0, size)

    def create_random_slot_id(self) -> SlotId:
        slot_id: SlotId = SlotId()
        slot_id.hour = self.get_random_element(7)
        slot_id.day = DayEnum.get_random_day()
        return slot_id

    def create_random_slot(self, data) -> Slotv1:
        print(randrange(10))
        teachers = data.teachers
        subjects = data.subjects
        classes = data.classes
        constraints = data.constraints

        slot_id: SlotId = self.create_random_slot_id()
        slot: Slotv1 = Slotv1()
        slot.teacher = teachers[self.get_random_element(len(teachers))]
        slot.subject = subjects[self.get_random_element(len(subjects))]
        slot.school_class = classes[self.get_random_element(len(classes))]
        return slot

    def do_generate_new_generation(self):
        super().do_generate_new_generation()

    def do_evaluate_against_constraints(self, constraints: List[Constraint]) -> bool:
        return super().do_evaluate_against_constraints(constraints)
