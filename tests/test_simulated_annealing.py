from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem
import matplotlib.pyplot as plt


def test_solves_nqueens():
    problem = NQueensProblem((0, 1, 2, 3, 4, 5, 6, 7, 8))
    problem.initial_state = problem.state_factory.random()
    heuristic = NQueensHeuristic().create(N_CONFLICTS)
    algorithm = SimulatedAnnealing(heuristic)
    solution_node = algorithm.search(problem)
    values_list = [heuristic(n) for n in solution_node.path()]

    fig, ax = plt.subplots()
    ax.plot(list(range(len(values_list))), values_list)
    plt.show()

    assert solution_node.state.is_goal()

