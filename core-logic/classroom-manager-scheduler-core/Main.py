from datapreprocessing.Engine import Engine
from datapreprocessing.Individual import Individual


# only for testing purposes
def read_json(file: str) -> str:
    pass


def main():
    pop_json: str = read_json("file")
    constr_json: str = read_json("file")
    engine = Engine(pop_json, constr_json)
    while engine.do_evaluate_against_constraints():
        engine.do_generate_new_generation()

    # TODO: get best individual
    fit: Individual = Engine.population.get_fit()


if __name__ == '__main__':
    main()




