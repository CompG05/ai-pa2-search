from typing import Optional
from constants import *


class AlgorithmFactory:
    @staticmethod
    def create(algorithm: str,
               heuristic: Optional[Callable[[Node], float]] = None,
               **kwargs):
        if algorithm.lower() == HILL_CLIMBING:
            return algorithms[algorithm](heuristic)

        elif algorithm.lower() == HILL_CLIMBING_SIDEWAYS:
            return algorithms[algorithm](heuristic, kwargs.get("max_sideways_moves"))

        elif algorithm.lower() == HILL_CLIMBING_RANDOM_RESTART:
            return algorithms[algorithm](heuristic, kwargs.get("exhaustive"),
                                         kwargs.get("time_limit"))

        elif algorithm.lower() == SIMULATED_ANNEALING:
            return algorithms[algorithm](heuristic, **kwargs)

        elif algorithm.lower() == GENETIC:
            return algorithms[algorithm](**kwargs)

        else:
            raise ValueError(f"Algorithm {algorithm} not found")


algorithm_factory = AlgorithmFactory()
