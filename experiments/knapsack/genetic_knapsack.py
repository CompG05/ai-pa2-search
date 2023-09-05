import sys
import time

from algorithms.local.genetic import GeneticSearch
from constants import ACCUM_VALUE
from heuristics.knapsack import KnapsackHeuristic
from problems.knapsack import KnapsackProblem


def main(file_name, iterations, **algorithm_args):
    times = []
    optimum_solutions = 0
    values = []

    print(f"Instance: {file_name}")
    optimum_file = file_name + "_op"
    with open(optimum_file) as f:
        optimum = float(f.readline())
    print(f"Optimum: {optimum}")

    for i in range(iterations):
        print(f"Iteration: {i+1} de {iterations}", end='\r')
        problem = KnapsackProblem.from_file(file_name)
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

    print(f"{algorithm_args}\n"
          f"\tmean value: %.2f\n" % (sum(values) / len(values)),
          f"\tmean time: %.2f\n" % (sum(times) / len(times)),
          f"\tsolution rate: %.2f\n" % (optimum_solutions / iterations))


if __name__ == '__main__':
    filename = sys.argv[1]
    iterations = int(sys.argv[2])
    args_idx = int(sys.argv[3])

    args_list = [
        {   # solution rate: 0.80
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "rank",
            "num_parents_mating": 2,
            "keep_elitism": 30,
            "crossover_type": "single_point"
        },
        {   # solution rate: 1.0
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "tournament",
            "num_parents_mating": 2,
            "keep_elitism": 30,
            "crossover_type": "single_point"
        },
        {   # solution rate: 0.98
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "rank",
            "num_parents_mating": 10,
            "keep_elitism": 30,
            "crossover_type": "single_point"
        },
        {   # solution rate: 1.0
            "num_generations": 200,
            "sol_per_pop": 200,
            "parent_selection_type": "tournament",
            "num_parents_mating": 10,
            "keep_elitism": 30,
            "crossover_type": "single_point"
        },
    ]

    main(filename, iterations, **args_list[args_idx])
