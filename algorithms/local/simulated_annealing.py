from typing import Callable
import math
import random
import time

import numpy as np

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self,
                 heuristic: Callable[[Node], float],
                 **kwargs):
        super().__init__()
        self.heuristic = heuristic
        self.schedule = exp_schedule(kwargs["init_temp"], kwargs["cooling_rate"], kwargs["min_temp"])
        self.time_limit = kwargs.get("time_limit") or float("inf")

    def search(self, problem: Problem) -> Node:
        s = problem.initial_state or problem.state_factory.random()
        current: Node = Node(s)
        best = current
        t = 1
        t0 = time.time()
        while True:
            T = self.schedule(t)
            if T == 0 or time.time() - t0 > self.time_limit or current.state.is_goal():
                return best

            neighbors = current.expand(problem)

            if not neighbors:
                return best

            succ = random.choice(neighbors)
            delta_e = self.heuristic(succ) - self.heuristic(current)

            if delta_e > 0 or random.random() < math.e ** (delta_e / T):
                current = succ
                if self.heuristic(succ) > self.heuristic(best):
                    best = succ

            t += 1


def exp_schedule(init_temp, cooling_rate, min_temp):
    def f(t):
        T = init_temp * np.exp(-cooling_rate * t)
        return T if T > min_temp else 0

    return f

