import importlib
from types import SimpleNamespace
from typing import List

from python.classmaxhourperdayconstraint import ClassMaxHourPerDayConstraint
from python.classmaxhourperdaysubjectconstraint import ClassMaxHourPerDayPerSubjectConstraint
from python.constraint import Constraint
from python.schoolclass import SchoolClass
from python.subject import Subject
from python.teacher import Teacher


class SchoolData(object):

    def __init__(self, classes: List[SimpleNamespace], teachers: List[SimpleNamespace],
                 subjects: List[SimpleNamespace], constraints: List[SimpleNamespace]):
        t_classes: List[SchoolClass] = []
        for school_class in classes:
            t_classes.append(SchoolClass(school_class.class_id))
        self.classes = t_classes

        t_techers: List[Teacher] = []
        for teacher in teachers:
            t_techers.append(Teacher(teacher.name, teacher.subjects))
        self.teachers = t_techers

        t_subjects: List[Subject] = []
        for subject in subjects:
            t_subjects.append(Subject(subject.subject_name))
        self.subjects = t_subjects

        t_constraints = []
        for constraint in constraints:
            a = ClassMaxHourPerDayConstraint()
            b = ClassMaxHourPerDayPerSubjectConstraint()
            z = importlib.import_module('python')
            klass = globals()[constraint.constraint_name]
            instance = klass()
            instance.fill(constraint.variables)
            t_constraints.append(instance)

        self.constraints = t_constraints

    classes: List[SchoolClass]
    teachers: List[Teacher]
    subjects: List[Subject]
    constraints: List[Constraint]
