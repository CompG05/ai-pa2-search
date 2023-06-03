import time
from typing import Optional

from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory

from solver.solution import Solution


class Solver:
    def __init__(
        self, problem: str, algorithm: str, heuristic: Optional[str], problem_kwargs=None, algorithm_kwargs=None
    ):
        problem_kwargs = problem_kwargs or {}
        algorithm_kwargs = algorithm_kwargs or {}
        self.problem, heuristic_factory = problem_factory.create(problem, **problem_kwargs)
        self.heuristic = heuristic_factory.create(heuristic) if heuristic else None
        self.algorithm = algorithm_factory.create(algorithm, self.heuristic, **algorithm_kwargs)
        self.algorithm_name = algorithm
        self.heuristic_name = heuristic

    def solve(self) -> Solution:
        bef_time = time.time()
        node = self.algorithm.search(self.problem)
        aft_time = time.time()
        node_value = self.heuristic(node) if self.heuristic else 0

        return Solution(
            node=node,
            value=node_value,
            algorithm_name=self.algorithm_name,
            heuristic_name=self.heuristic_name,
            dtime=aft_time - bef_time,
            memory_peak=0,
        )
