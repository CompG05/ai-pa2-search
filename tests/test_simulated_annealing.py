from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def test_solves_nqueens():
    problem = NQueensProblem(dimension=6)
    heuristic = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
    algorithm = SimulatedAnnealing(heuristic, init_temp=1, cooling_rate=0.0005, min_temp=0.01)
    solution_node = algorithm.search(problem)

    assert solution_node.state.is_goal()

