from random import randrange
from typing import List

from python.core_service import CoreService
from python.dayenum import DayEnum
from python.engine import Engine
from python.constraint import Constraint
from python.population import Population
from python.schooldata import SchoolData
from python.source_type import SourceType
from python.week import Week, Slotv1, SlotId





class EngineImplV1(Engine):
    primarch_slots: List[Slotv1] = []

    def create_constraint_list_from_json(self, constraint_json: str) -> List[Constraint]:
        return super().create_constraint_list_from_json(constraint_json)

    def create_initial_population(self, pop: str, source_type: SourceType) -> Population:
        data: SchoolData = None
        if source_type == SourceType.file:
            data = CoreService.get_processed_json(CoreService.read_json(pop))
        elif source_type == SourceType.json:
            data = CoreService.get_processed_json(pop)

        population: List[Week] = self.create_primarchs(data)


        initial_population: Population = Population(len(population), population)
        return initial_population

    def create_primarchs(self, data) -> List[Week]:

        teachers = data.teachers
        subjects = data.subjects
        classes = data.classes
        primarch_slot_ids: List[SlotId] = self.create_primarch_ids()
        weeks: List[Week] = []

        for id in primarch_slot_ids:
            counter = 0
            for teacher in teachers:
                for subject in subjects:
                    for sclass in classes:
                        if len(weeks) < counter + 1:
                            slots: list() = []
                            week: Week = Week()
                            week.slots = slots
                            weeks.append(week)
                        slot: Slotv1 = Slotv1()
                        slot.slot_id = id
                        slot.teacher = teacher
                        slot.subject = subject
                        slot.school_class = sclass
                        self.primarch_slots.append(slot)
                        weeks[counter].slots.append(slot)
                        counter = counter + 1

        return weeks

    def create_primarch_ids(self) -> List[SlotId]:
        primarch_slot_ids: List[SlotId] = []
        for day in DayEnum.get_days():
            for hour in range(8):
                slot_id: SlotId = SlotId()
                slot_id.day = day
                slot_id.hour = hour
                primarch_slot_ids.append(slot_id)
        return primarch_slot_ids

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


