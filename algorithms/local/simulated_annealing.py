from typing import Callable
import math
import random

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], schedule: Callable[[float], float] = None):
        super().__init__()
        self.heuristic = heuristic
        self.schedule = schedule
        if schedule is None:
            self.set_schedule(1, 0.005, 0.05)

    def set_schedule(self, init_temp, decay, min_temp):
        self.schedule = lambda t: max(min_temp, init_temp * math.pow(math.e, -decay * t))

    def search(self, problem: Problem) -> Node:
        current = Node(problem.initial_state)
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
