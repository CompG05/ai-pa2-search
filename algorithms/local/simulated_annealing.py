from typing import Callable, Optional
import math
import random

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], schedule: Optional[Callable[[float], float]] = None):
        super().__init__()
        self.heuristic = heuristic
        self.schedule = schedule

    def set_schedule(self, init_temp, decay, min_temp):
        self.schedule = lambda t: max(min_temp, init_temp * math.pow(math.e, -decay * t))

    def search(self, problem: Problem) -> Node:
        if self.schedule is None:
            raise Exception("Schedule not set")

        current = Node(problem.state_factory.random())
        t = 1
        while True:
            T = self.schedule(t)

            if T <= 0.05:   # with 0.01 it will iterate ~1520 times  (with 0.001 -> ~1980 times)
                return current

            succ = random.choice(current.expand(problem))
            delta_e = self.heuristic(current) - self.heuristic(succ)

            if delta_e > 0:
                current = succ
            else:
                print(delta_e)
                if random.random() < math.pow(math.e, delta_e/T):  # current <- next , with probability e^{-delta_e/T}
                    current = succ

            t += 1
