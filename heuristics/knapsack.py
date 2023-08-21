from typing import Callable

from algorithms.search_algorithm import Node
from constants import ACCUM_VALUE, ACCUM_RATING
from problems.knapsack import KnapsackProblem, KnapsackState


class KnapsackHeuristic:
    def create(self, heuristic: str) -> Callable[[Node], float]:
        if heuristic.lower() == ACCUM_VALUE:
            return self.accumulated_value
        if heuristic.lower() == ACCUM_RATING:
            return self.accumulated_rating
        else:
            raise ValueError(f"Heuristic not found: {heuristic}")

    @staticmethod
    def accumulated_value(node: Node) -> float:
        return node.state.sack_value

    @staticmethod
    def accumulated_rating(node: Node) -> float:
        return node.state.sack_rating

    def create_fitness(self, heuristic_name: str, problem: KnapsackProblem) -> Callable:
        heuristic = self.create(heuristic_name)

        def fitness_func(fst, solution=None, _=None):
            if solution is not None:
                state = KnapsackState(solution, problem.weight, problem.value, problem.sack_cap)
                node = Node(state)
            else:
                node = fst

            return heuristic(node) if node.state.is_valid() else 0

        return fitness_func
