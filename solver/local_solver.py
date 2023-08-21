import time
import tracemalloc as tm
from typing import Optional

from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory

from solver.solution import Solution
from constants import *
from solver.solver import Solver


class LocalSolver(Solver):
    def __init__(
        self,
        problem: str,
        algorithm: str,
        heuristic: Optional[str],
        problem_kwargs=None,
        algorithm_kwargs=None,
    ):
        super().__init__(problem, algorithm, heuristic, problem_kwargs, algorithm_kwargs)
        self.problem, heuristic_factory = problem_factory.create(problem, **self.problem_kwargs)
        self.heuristic = heuristic_factory.create(heuristic) if heuristic else None
        self.algorithm = algorithm_factory.create(
            algorithm, self.heuristic, **self.algorithm_kwargs
        )
