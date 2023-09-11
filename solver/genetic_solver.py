import time
import tracemalloc as tm

from constants import GENETIC
from problems.problem import Problem
from solver.solution import Solution
from solver.solver import Solver

from factories.algorithm_factory import algorithm_factory
from factories.problem_factory import problem_factory


class GeneticSolver(Solver):
    def __init__(
            self,
            problem: str,
            heuristic: str,
            problem_kwargs=None,
            algorithm_kwargs=None,
    ):
        super().__init__(problem, GENETIC, heuristic, problem_kwargs, algorithm_kwargs)
        self.problem, heuristic_factory = problem_factory.create(problem, **self.problem_kwargs)
        self.heuristic = heuristic_factory.create_fitness(heuristic, self.problem)
        self.algorithm_kwargs.update({"initial_population": init_population(self.problem, self.algorithm_kwargs["sol_per_pop"])})
        self.algorithm_kwargs.update(self.problem.default_genetic_args)
        self.algorithm_kwargs.pop("sol_per_pop")
        self.algorithm = algorithm_factory.create(
            GENETIC, self.heuristic, **self.algorithm_kwargs
        )


def init_population(problem: Problem, sol_per_pop: int):
    return [problem.state_factory.random().to_list() for _ in range(sol_per_pop)]
