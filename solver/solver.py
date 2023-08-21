import time
import tracemalloc as tm
from typing import Optional

from solver.solution import Solution


class Solver:
    def __init__(
        self,
        problem: str,
        algorithm: str,
        heuristic: str,
        problem_kwargs: Optional[dict] = None,
        algorithm_kwargs: Optional[dict] = None,
    ):
        self.problem_kwargs = problem_kwargs or {}
        self.algorithm_kwargs = algorithm_kwargs or {}
        self.algorithm_name = algorithm
        self.problem_name = problem
        self.heuristic_name = heuristic

    def solve(self) -> Solution:
        bef_time = time.time()
        tm.start()
        node = self.algorithm.search(self.problem)
        tm.take_snapshot()
        memory_peak = tm.get_traced_memory()[1]
        aft_time = time.time()
        tm.stop()
        node_value = self.heuristic(node)

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
