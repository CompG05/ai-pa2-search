import pytest

from algorithms.local.hill_climbing import HillClimbingSideMovements, HillClimbing, RandomRestartHillClimbing
from constants import *
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


states = [(2, 5, 1, 6, 4, 1, 6, 3), (2, 5, 1, 6, 4, 0, 7, 3), (2, 6, 1, 6, 4, 1, 6, 3), (2, 3, 1, 6, 4, 1, 6, 3)]

h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
h2 = KnapsackHeuristic().create(ACCUM_VALUE)

hc_algorithms = [HillClimbing(h), HillClimbingSideMovements(h, 100), RandomRestartHillClimbing(h, exhaustive=True)]
nqueens_config = [(algorithm, state) for algorithm in hc_algorithms for state in states]


@pytest.mark.parametrize("algorithm, state", nqueens_config)
def test_random_restart_exhaustive_nqueens(algorithm, state):
    p = NQueensProblem(dimension=8, initial=state)
    solution = algorithm.search(p)
    assert solution.state.is_goal()
