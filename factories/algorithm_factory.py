from typing import Optional
from constants import *


class AlgorithmFactory:
    @staticmethod
    def create(algorithm: str, heuristic: Optional[str] = None, **kwargs):
        if algorithm.lower() in algorithms:
            return algorithms[algorithm.lower()](heuristic, **kwargs)
        else:
            raise ValueError(f"Algorithm {algorithm} not found")

algorithm_factory = AlgorithmFactory()
