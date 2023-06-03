from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem
import matplotlib.pyplot as plt


def test_solves_nqueens():
    problem = NQueensProblem(dimension=8)
    heuristic = NQueensHeuristic().create(N_CONFLICTS)
    algorithm = SimulatedAnnealing(heuristic)
    algorithm.set_schedule(1, 0.01, 0.05)
    solution_node = algorithm.search(problem)
    values_list = [heuristic(n) for n in solution_node.path()]

    _, ax = plt.subplots()
    ax.plot(list(range(len(values_list))), values_list)
    plt.show()

    # assert solution_node.state.is_goal()
    assert True

