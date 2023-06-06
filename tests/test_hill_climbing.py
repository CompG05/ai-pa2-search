from algorithms.local.hill_climbing import HillClimbingSideMovements, HillClimbing, RandomRestartHillClimbing
from constants import *
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem

p = NQueensProblem(dimension=8)
h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
h2 = KnapsackHeuristic().create(ACCUM_VALUE)

hc_algorithms = [HillClimbing(h), HillClimbingSideMovements(h, 100), RandomRestartHillClimbing(h, exhaustive=True)]


def test_random_restart_exhaustive_nqueens():
    algorithm = RandomRestartHillClimbing(h)
    solution = algorithm.search(p)
    assert solution.state.is_goal()
