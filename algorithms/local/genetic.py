from typing import Callable

import pygad

from algorithms.search_algorithm import Node, SearchAlgorithm
from problems.problem import Problem


class GeneticSearch(SearchAlgorithm):
    def __init__(self, fitness_func: Callable, **kwargs):
        """Required parameters:
            - num_generations +
            - num_parents_mating +
        Optional parameters:
            - fitness_func
            - sol_per_pop: number of solutions in the population  +
            - initial_population
            - num_genes: number of genes in the chromosome  +
            - gene_type
            - parent_selection_type: 'sss' | 'rws' | 'sus' | 'rank' | 'random' | 'tournament'   +
            - keep_parents
            - keep_elitism  +
            - K_tournament
            - crossover_type  +
            - crossover_probability
            - mutation_type: 'random' | 'swap' | 'scramble' | 'inversion' | 'adaptive'
            - mutation_probability
        """
        super().__init__()
        self.ga_instance = pygad.GA(fitness_func=fitness_func, **kwargs)

    def search(self, problem: Problem) -> Node:
        self.ga_instance.run()
        solution, solution_fitness, solution_idx = self.ga_instance.best_solution()
        node = Node(problem.state_from_list(solution))
        node.accum_nodes = self.ga_instance.generations_completed
        return node
