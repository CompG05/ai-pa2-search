from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory

from solution import Solution


class Solver:
    def __init__(self, problem: str, initial_state, algorithm: str, heuristic: str):
        self.problem, heuristic_factory = problem_factory.create(problem, initial_state)
        self.heuristic = heuristic and heuristic_factory.create(heuristic)
        self.algorithm = algorithm_factory.create(algorithm, self.heuristic)
        self.algorithm_name = algorithm
        self.heuristic_name = heuristic

    def solve(self) -> Solution:
        node = self.algorithm.search(self.problem)
        return Solution(node, self.algorithm_name, self.heuristic_name, self.problem.initial_state)
