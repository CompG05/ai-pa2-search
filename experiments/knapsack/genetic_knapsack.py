import argparse
import json
import os
import time

from algorithms.local.genetic import GeneticSearch
from constants import ACCUM_VALUE
from heuristics.knapsack import KnapsackHeuristic
from problems.knapsack import KnapsackProblem


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", "-f", type=str)
    group.add_argument("--dir", "-d", type=str)
    parser.add_argument("--algorithm-args", "-a", type=str)
    args = parser.parse_args()
    algorithm_args = json.loads(args.algorithm_args)

    if args.file:
        file_name_list = [args.file]
    else:
        file_name_list = [args.dir + '/' + file for file in os.listdir(args.dir)]

    times = []
    # optimums = 0
    values = []

    for file_name in file_name_list:
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

    print(f"{args.algorithm_args}\n"
          f"\tmean value: %.2f\n" % (sum(values) / len(values)),
          f"\tmean time: %.2f\n" % (sum(times) / len(times)))


if __name__ == '__main__':
    main()
