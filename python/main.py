from python.core_service import CoreService
from python.engine import Engine
from python.engine_implv1 import EngineImplV1, SourceType
from python.individual import Individual
from python.population import Population
from python.schooldata import SchoolData


def main():
    engine: EngineImplV1 = EngineImplV1()
    intiial_population: Population = engine.create_initial_population("resources/testclass.json", SourceType.file)
    print()


if __name__ == '__main__':
    main()




