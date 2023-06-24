from typing import Callable

from algorithms.search_algorithm import Node
from constants import ACCUM_VALUE, ACCUM_RATING


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
