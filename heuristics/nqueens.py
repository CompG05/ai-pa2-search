from typing import Callable

from algorithms.search_algorithm import Node
from problems.nqueens import NQueensState
from constants import *


class NQueensHeuristic:
    def create(self, heuristic: str) -> Callable:
        from constants import N_CONFLICTS
        if heuristic.lower() == N_CONFLICTS:
            return self.n_conflicts
        if heuristic.lower() == INVERSE_N_CONFLICTS:
            return lambda n: -self.n_conflicts(n)
        if heuristic.lower() == INVERSE_N_CONFLICTS_FITNESS:
            return inverse_n_conflicts_fitness
        else:
            raise ValueError("Heuristic not found")

    @staticmethod
    def n_conflicts(node: Node):
        state: NQueensState = node.state
        return state.n_conflicts()


def inverse_n_conflicts_fitness(fst, solution=None, _=None) -> float:
    if solution is not None:
        state = NQueensState(tuple(solution))
        node = Node(state)
    else:
        node = fst
    return -NQueensHeuristic().n_conflicts(node)
