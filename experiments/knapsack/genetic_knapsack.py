import argparse
import json
import os
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
        print(f"Iteration: {i+1} de {iterations}")
        problem = KnapsackProblem.from_file(file_name)
        algorithm_args.update(problem.default_genetic_args)
        algorithm = GeneticSearch(**algorithm_args)
        heuristic = KnapsackHeuristic().create(ACCUM_VALUE)

        bef = time.time()
        solution = algorithm.search(problem)
        aft = time.time()
        value = heuristic(solution)

        times.append(aft - bef)
        values.append(value)
        optimum_solutions += value == optimum

    print(f"{algorithm_args}\n"
          f"\tmean value: %.2f\n" % (sum(values) / len(values)),
          f"\tmean time: %.2f\n" % (sum(times) / len(times)),
          f"\tsolution rate: %.2f\n" % (optimum_solutions / iterations))


if __name__ == '__main__':
    filename = sys.argv[1]
    iterations = int(sys.argv[2])

    args_list = [
        # {
        #     "num_generations": 200,
        #     "sol_per_pop": 200,
        #     "parent_selection_type": "rank",
        #     "num_parents_mating": 10,
        #     "keep_elitism": 30,
        #     "crossover_type": "single_point"
        # },
        # {
        #     "num_generations": 200,
        #     "sol_per_pop": 200,
        #     "parent_selection_type": "tournament",
        #     "num_parents_mating": 2,
        #     "keep_elitism": 30,
        #     "crossover_type": "single_point"
        # },
        # {
        #     "num_generations": 200,
        #     "sol_per_pop": 200,
        #     "parent_selection_type": "tournament",
        #     "num_parents_mating": 10,
        #     "keep_elitism": 30,
        #     "crossover_type": "single_point"
        # },
        {
            "num_generations": 200,
            "sol_per_pop": 700,
            "parent_selection_type": "tournament",
            "num_parents_mating": 20,
            "keep_elitism": 100,
            "crossover_type": "single_point"
        },
    ]

    for args in args_list:
        main(filename, iterations, **args)
