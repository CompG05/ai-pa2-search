import random
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

    problem = KnapsackProblem.from_file(file_name)
    algorithm_args.update(problem.default_genetic_args)
    algorithm_args.update(
        {"initial_population": [problem.state_factory.random().to_list() for _ in
                                range(algorithm_args["sol_per_pop"])]})
    algorithm_args.pop("sol_per_pop")
    fitness = KnapsackHeuristic().create_fitness(ACCUM_VALUE, problem)

    for i in range(iterations):
        print(f"Iteration: {i+1} de {iterations}", end='\r')
        algorithm = GeneticSearch(fitness, **algorithm_args)

        bef = time.time()
        solution = algorithm.search(problem)
        aft = time.time()
        value = fitness(solution)

        times.append(aft - bef)
        values.append(value)
        optimum_solutions += value == optimum
    print()

    print(f"\tmean value: %.2f\n" % (sum(values) / len(values)),
          f"\tmean time: %.2f\n" % (sum(times) / len(times)),
          f"\tsolution rate: %.2f\n" % (optimum_solutions / iterations))


if __name__ == '__main__':
    filename = sys.argv[1]
    iterations = int(sys.argv[2])
    args_idx = int(sys.argv[3])

    def custom_mutation(offspring, ga_instance):
        for chromosome_idx in range(offspring.shape[0]):
            if random.random() < 0.9:
                random_gene_idx = random.choice(range(offspring.shape[1]))
                offspring[chromosome_idx, random_gene_idx] = int(not offspring[chromosome_idx, random_gene_idx])
        return offspring

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
        {  # solution rate: 1.0
            "num_generations": 50,
            "sol_per_pop": 150,
            "parent_selection_type": "rank",
            "num_parents_mating": 10,
            "keep_elitism": 10,
            "crossover_type": "two_points"
        },
        {  # solution rate: 1.0
            "num_generations": 50,
            "sol_per_pop": 150,
            "parent_selection_type": "rank",
            "num_parents_mating": 10,
            "keep_elitism": 10,
            "crossover_type": "two_points"
        },

        {  #for hard ones
            "num_generations": 200,
            "sol_per_pop": 400,
            "parent_selection_type": "rank",
            "crossover_type": "two_points",
            #"mutation_probability": 0.2,
            #"mutation_type": "random",
            "keep_parents": 2,
            "keep_elitism": 50,
            "num_parents_mating": 2
        },
        {  # Idx: 7  No crossover
            "num_generations": 200,
            "sol_per_pop": 400,
            "crossover_probability": 0.0,
            "mutation_type": custom_mutation,
            "mutation_num_genes": 1,
            "keep_elitism": 100,
            "num_parents_mating": 2
        }
    ]

    main(filename, iterations, **args_list[args_idx])
