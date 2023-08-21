import sys

from algorithms.local.genetic import GeneticSearch
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main(dimension, iterations, **params):
    problem = NQueensProblem(dimension=dimension)
    fitness = NQueensHeuristic().create_fitness(INVERSE_N_CONFLICTS)
    solutions = 0

    for i in range(iterations):
        print(f"Voy por: {i+1} de {iterations}")
        algorithm = GeneticSearch(
            fitness_func=fitness,
            gene_type=int,
            num_genes=dimension,
            mutation_percent_genes=1/8,
            gene_space=list(range(0, dimension)),
            **params
        )
        best_node = algorithm.search(problem)
        # print(fitness[INVERSE_N_CONFLICTS](None, list(best_node.state.data), None))
        if best_node.state.is_goal():
            solutions += 1

    print(f"{params}\n"
          f"\tsolution rate: {solutions / iterations}\n")


if __name__ == "__main__":
    dimension = int(sys.argv[1])
    iterations = int(sys.argv[2])

    configs = {
        8: [
            {
                "num_generations": 200,
                "sol_per_pop": 200,
                "parent_selection_type": "rank",
                "num_parents_mating": 2,
                "keep_elitism": 30,
                "crossover_type": "single_point"
            }
        ],

        16: [
            {
                "num_generations": 200,
                "sol_per_pop": 200,
                "parent_selection_type": "rank",
                "num_parents_mating": 2,
                "keep_elitism": 30,
                # "crossover_type": "single_point"
            }
        ]
    }

    for config in configs[dimension]:
        main(dimension, iterations, **config)
