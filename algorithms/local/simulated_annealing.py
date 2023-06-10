from typing import Callable, Optional
import math
import random

import numpy as np

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], schedule: Optional[Callable[[float], float]] = None):
        super().__init__()
        self.heuristic = heuristic
        self.schedule = schedule
        self.limit = None

    def set_schedule(self, k, lam, limit):
        self.schedule = lambda t: k * np.exp(-lam * t)
        self.limit = limit

    def search(self, problem: Problem) -> Node:
        if self.schedule is None:
            raise Exception("Schedule not set")

        current = Node(problem.state_factory.random())
        t = 1
        while True:
            T = self.schedule(t)
            if t == self.limit:
                return current

            neighbors = current.expand(problem)

            if not neighbors:
                return current.state

            succ = random.choice(neighbors)
            delta_e = self.heuristic(current) - self.heuristic(succ)

            if delta_e > 0 or random.random() < math.e ** (delta_e/T):
                current = succ

            t += 1
