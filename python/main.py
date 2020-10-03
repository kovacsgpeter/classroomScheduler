from python.core_service import CoreService
from python.engine import Engine
from python.engine_implv1 import EngineImplV1, SourceType
from python.individual import Individual
from python.population import Population
from python.schooldata import SchoolData


def min(list: [int]):
    counter = len(list)-1
    var_zero = list[counter]
    while counter > -1:
        if list[counter] < var_zero:
            var_zero = list[counter]
        counter = counter - 1
    return var_zero

def main():
    # print(min([2, 34, 2, 11, 4, 99, 1]))
    engine: EngineImplV1 = EngineImplV1()
    intiial_population: Population = engine.create_initial_population("resources/testclass.json", SourceType.file)
    print()


if __name__ == '__main__':
    main()




