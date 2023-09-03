import sys

from algorithms.local.genetic import GeneticSearch
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main(dimension, iterations, **params):
    problem = NQueensProblem(dimension=dimension)
    fitness = NQueensHeuristic().create_fitness(INVERSE_N_CONFLICTS, problem)
    solutions = 0
    values = []

    for i in range(iterations):
        print(f"Voy por: {i+1} de {iterations}", end='\r')
        algorithm = GeneticSearch(
            fitness_func=fitness,
            gene_type=int,
            num_genes=dimension,
            gene_space=list(range(0, dimension)),
            **params
        )
        best_node = algorithm.search(problem)
        if best_node.state.is_goal():
            solutions += 1
        values.append(fitness(best_node))
    print()

    print(f"{params}\n"
          f"\tsolution rate: {solutions / iterations}\n"
          f"\taverage value: {sum(values) / len(values)}\n")


if __name__ == "__main__":
    dimension = int(sys.argv[1])
    iterations = int(sys.argv[2])

    configs = {
        8: [
            {
                "num_generations": 200,
                "sol_per_pop": 200,
                "parent_selection_type": "rank",
                "num_parents_mating": 10,
                "keep_elitism": 30,
                "crossover_type": "single_point"
            },
        ],

        16: [
            # {
            #     "num_generations": 200,
            #     "sol_per_pop": 200,
            #     "parent_selection_type": "rank",
            #     "num_parents_mating": 10,
            #     "keep_elitism": 30,
            #     "crossover_type": "single_point"
            # },
            # {
            #     "num_generations": 400,
            #     "sol_per_pop": 200,
            #     "parent_selection_type": "rank",
            #     "num_parents_mating": 10,
            #     "keep_elitism": 30,
            #     "crossover_type": "single_point"
            # },
            {
                "num_generations": 600,
                "sol_per_pop": 250,
                "parent_selection_type": "rank",
                "num_parents_mating": 10,
                "keep_elitism": 35,
                "crossover_type": "single_point"
            },
        ],

        32: [
            # {
            #     "num_generations": 600,
            #     "sol_per_pop": 400,
            #     "parent_selection_type": "rank",
            #     "num_parents_mating": 10,
            #     "keep_elitism": 50,
            #     "crossover_type": "single_point"
            # },

            # {
            #     "num_generations": 1000,
            #     "sol_per_pop": 200,
            #     "parent_selection_type": "rank",
            #     "num_parents_mating": 5,
            #     "keep_parents": 5,
            #     "keep_elitism": 30,
            #     "crossover_probability": 0.7,
            # },
            # solution rate: 0.0
            # average value: -2.3

            # {
            #     "num_generations": 1000,
            #     "sol_per_pop": 200,
            #     "parent_selection_type": "tournament",
            #     "K_tournament": 3,
            #     "num_parents_mating": 5,
            #     "keep_parents": 5,
            #     "keep_elitism": 30,
            #     "crossover_probability": 0.7,
            # },
            # solution rate: 0.0
            # average value: -3.6

            {
                "num_generations": 1000,
                "sol_per_pop": 400,
                "parent_selection_type": "tournament",
                "K_tournament": 3,
                "num_parents_mating": 10,
                "keep_parents": 5,
                "keep_elitism": 50,
                "crossover_probability": 0.7,
            },
        ]
    }

    for config in configs[dimension]:
        main(dimension, iterations, **config)
