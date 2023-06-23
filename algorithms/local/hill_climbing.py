import random
import sys
from typing import Callable

import PIL.Image

from algorithms.search_algorithm import SearchAlgorithm, Node
from problems.problem import Problem, State


class HillClimbing(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], initial: State = None):
        self.initial = initial
        self.heuristic = heuristic
        super().__init__()

    def search(self, problem: Problem) -> Node:
        s = self.initial or problem.initial_state or problem.state_factory.random()
        current: Node = Node(s)

        while True:
            neighbors = current.expand(problem)
            if not neighbors:
                return current
            neighbor = max(neighbors, key=(lambda n: self.heuristic(n)))

            if self.heuristic(neighbor) <= self.heuristic(current):
                return current

            current = neighbor


class HillClimbingSideMovements(SearchAlgorithm):
    def __init__(self, heuristic: Callable[[Node], float], k: int):
        self.heuristic = heuristic
        self.k = k
        super().__init__()

    def search(self, problem: Problem) -> Node:
        s = problem.initial_state or problem.state_factory.random()
        current: Node = Node(s)

        current_value = self.heuristic(current)
        current_k = self.k

        while True:
            neighbors = []
            best_neighbor = None
            best_neighbor_value = -sys.float_info.max
            best_neighbors = []

            for child in current.expand(problem):
                neighbors.append(child)
                v = self.heuristic(child)
                if v > best_neighbor_value:
                    best_neighbor_value = v
                    best_neighbor = child
                    best_neighbors = [child]
                elif v == best_neighbor_value:
                    best_neighbors.append(child)

            if best_neighbor is None:  # current has no neighbors
                return current

            if best_neighbor_value < current_value or (
                best_neighbor_value == current_value and current_k == 0
            ):
                return current

            current = best_neighbor

            if best_neighbor_value == current_value:
                current_k -= 1
                current = random.choice(best_neighbors)
            else:
                current_k = self.k

            current_value = self.heuristic(current)


class RandomRestartHillClimbing(SearchAlgorithm):
    def __init__(
        self,
        heuristic: Callable[[Node], float],
        exhaustive: bool = True,
        max_iterations: int = 50,
    ):
        self.heuristic = heuristic
        self.exhaustive = exhaustive
        self.max_iterations = max_iterations
        super().__init__()

    def search(self, problem: Problem) -> Node:
        if self.exhaustive:
            return self.exhaustive_search(problem)
        else:
            return self.non_exhaustive_search(problem)

    def exhaustive_search(self, problem: Problem) -> Node:
        hc = HillClimbing(self.heuristic)
        solution = hc.search(problem)
        nodes = solution.accum_nodes

        while not solution.state.is_goal():
            hc = HillClimbing(self.heuristic, problem.state_factory.random())
            solution = hc.search(problem)
            nodes += solution.accum_nodes

        solution.accum_nodes = nodes
        return solution

    def non_exhaustive_search(self, problem: Problem) -> Node:
        hc = HillClimbing(self.heuristic)
        solutions = [hc.search(problem)]

        while (
            not solutions[-1].state.is_goal() and len(solutions) < self.max_iterations
        ):
            hc = HillClimbing(self.heuristic, problem.state_factory.random())
            solutions.append(hc.search(problem))

        solution = max(solutions, key=(lambda n: self.heuristic(n)))
        solution.accum_nodes = sum([s.accum_nodes for s in solutions])
        return solution
