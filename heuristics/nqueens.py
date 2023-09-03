from typing import Callable

from algorithms.search_algorithm import Node
from problems.nqueens import NQueensState
from constants import *


class NQueensHeuristic:
    def create(self, heuristic: str) -> Callable:
        if heuristic.lower() == N_CONFLICTS:
            return self.n_conflicts
        if heuristic.lower() == INVERSE_N_CONFLICTS:
            return lambda n: -self.n_conflicts(n)
        else:
            raise ValueError("Heuristic not found")

    def create_fitness(self, heuristic_name: str, _) -> Callable:
        heuristic = self.create(heuristic_name)

        def fitness_func(fst, solution=None, _=None):
            if solution is not None:
                state = NQueensState(tuple(solution))
                node = Node(state)
            else:
                node = fst

            return heuristic(node) if node.state.is_valid() else 0

        return fitness_func

    @staticmethod
    def n_conflicts(node: Node):
        state: NQueensState = node.state
        return state.n_conflicts()
