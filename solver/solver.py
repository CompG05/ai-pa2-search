import time
import tracemalloc as tm
from typing import Optional

from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory

from solver.solution import Solution
from constants import *


class Solver:
    def __init__(
            self, problem: str, algorithm: str, heuristic: Optional[str], problem_kwargs=None, algorithm_kwargs=None
    ):
        self.problem_kwargs = problem_kwargs or {}
        self.algorithm_kwargs = algorithm_kwargs or {}
        self.problem, heuristic_factory = problem_factory.create(problem, **self.problem_kwargs)
        if algorithm == GENETIC:
            for key in self.problem.default_genetic_args.keys():
                self.algorithm_kwargs[key] = self.problem.default_genetic_args[key]
        self.heuristic = heuristic_factory.create(heuristic) if heuristic else None
        self.algorithm = algorithm_factory.create(algorithm, self.heuristic, **self.algorithm_kwargs)
        self.algorithm_name = algorithm
        self.heuristic_name = heuristic

    def solve(self) -> Solution:
        bef_time = time.time()
        tm.start()
        node = self.algorithm.search(self.problem)
        tm.take_snapshot()
        memory_peak = tm.get_traced_memory()[1]
        aft_time = time.time()
        tm.stop()
        node_value = self.heuristic(node) if self.heuristic else 0

        return Solution(
            node=node,
            value=node_value,
            algorithm_name=self.algorithm_name,
            heuristic_name=self.heuristic_name,
            problem_kwargs=self.problem_kwargs or {},
            algorithm_kwargs=self.algorithm_kwargs or {},
            dtime=aft_time - bef_time,
            memory_peak=memory_peak,
        )
