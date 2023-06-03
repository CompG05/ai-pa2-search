from constants import *
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic


class ProblemFactory:
    def create(self, problem: str, **kwargs):
        if problem.lower() == NQUEENS:
            return NQueensProblem(kwargs.get("dimension")), NQueensHeuristic()
        if problem.lower() == KNAPSACK:
            return KnapsackProblem(kwargs.get("content"), kwargs.get("weights"), kwargs.get("value")), KnapsackHeuristic()
        else:
            raise ValueError("Problem not found")


problem_factory = ProblemFactory()
