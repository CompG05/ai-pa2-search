import sys
import time

from algorithms.local.genetic import GeneticSearch
from constants import ACCUM_VALUE
from heuristics.knapsack import KnapsackHeuristic
from problems.knapsack import KnapsackProblem


def main(filename, iterations, **algorithm_args):
    times = []
    optimum_solutions = 0
    values = []

    print(f"Instance: {filename}")
    with open(filename + "_op") as f:
        optimum = float(f.readline())
    print(f"Optimum: {optimum}")

    print(algorithm_args)

    for i in range(iterations):
        print(f"Iteration: {i+1} de {iterations}", end="\r")
        problem = KnapsackProblem.from_file(filename)
        algorithm_args.update(problem.default_genetic_args)
        fitness = KnapsackHeuristic().create_fitness(ACCUM_VALUE, problem)
        algorithm = GeneticSearch(fitness, **algorithm_args)

        bef = time.time()
        solution = algorithm.search(problem)
        aft = time.time()
        value = fitness(solution)

        times.append(aft - bef)
        values.append(value)
        optimum_solutions += value == optimum
    print()

    print(
        f"mean value: %.2f" % (sum(values) / len(values)),
        f"\nmean time: %.2f" % (sum(times) / len(times)),
        f"\nsolution rate: %.2f" % (optimum_solutions / iterations),
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python -m experiments.knapsack.genetic <file_name> <config_idx> <iterations>"
        )
        exit(1)

    filename = sys.argv[1]
    args_idx = int(sys.argv[2])
    iterations = int(sys.argv[3])

    args_list = [
        {  # solution rate: 0.80
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "rank",
            "num_parents_mating": 2,
            "keep_elitism": 30,
            "crossover_type": "single_point",
        },
        {  # solution rate: 1.0
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "tournament",
            "num_parents_mating": 2,
            "keep_elitism": 30,
            "crossover_type": "single_point",
        },
        {  # solution rate: 0.98
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "rank",
            "num_parents_mating": 10,
            "keep_elitism": 30,
            "crossover_type": "single_point",
        },
        {  # solution rate: 1.0
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "tournament",
            "num_parents_mating": 10,
            "keep_elitism": 30,
            "crossover_type": "single_point",
        },
    ]

    main(filename, iterations, **args_list[args_idx])
