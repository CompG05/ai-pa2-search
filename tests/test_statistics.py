import pytest

from algorithms.local.hill_climbing import HillClimbing
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem

config_accum_nodes = [
    ((2, 5, 1, 6, 4, 0, 7, 3), 57),
    ((2, 5, 1, 6, 5, 0, 7, 3), 113),
    ((2, 5, 1, 6, 5, 0, 7, 5), 169),
]


@pytest.mark.parametrize("initial, expected_accum_nodes", config_accum_nodes)
def test_accum_nodes(initial, expected_accum_nodes):
    p = NQueensProblem(dimension=8, initial=initial)
    h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
    sol_node = HillClimbing(h).search(p)
    assert sol_node.accum_nodes == expected_accum_nodes
