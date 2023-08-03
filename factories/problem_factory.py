from constants import *
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic


class ProblemFactory:
    def create(self, problem: str, **kwargs):
        if problem.lower() == NQUEENS:
            return NQueensProblem(kwargs.get("dimension"), kwargs.get("initial_state")), NQueensHeuristic()

        if problem.lower() == KNAPSACK:
            if "path" in kwargs:
                return KnapsackProblem.from_file(kwargs.get("path"), kwargs.get("content")), KnapsackHeuristic()
            return KnapsackProblem(kwargs.get("content"), kwargs.get("weights"),
                                   kwargs.get("values"), kwargs.get("sack_cap")), KnapsackHeuristic()

        else:
            raise ValueError("Problem not found")


problem_factory = ProblemFactory()
