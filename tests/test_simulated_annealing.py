import pytest

from constants import *
from heuristics.knapsack import KnapsackHeuristic
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem
from solver.local_solver import LocalSolver


# Problems states
nqueens_states = [(2, 5, 1, 6, 4, 1, 6, 3), (2, 5, 1, 6, 4, 0, 7, 3), (2, 6, 1, 6, 4, 1, 6, 3), (2, 3, 1, 6, 4, 1, 6, 3)]
knapsack_states = [[True, False, False, False, False, False, False], [False, False, False, False, False, False, False]]

# Heuristics
h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
h2 = KnapsackHeuristic().create(ACCUM_VALUE)

# Problems args
knapsack_values = [70, 20, 39, 37, 7, 5, 10]
knapsack_weights = [31, 10, 20, 19, 4, 3, 6]
sack_cap = 50
optimum = 107

#Algorithm args
nqueens_algorithm_args = [(1, 0.0005, 0.1)]
knapsack_algorithm_args = [(100, 0.0001, 0.01)]


nqueens_config = [(SimulatedAnnealing(h, init_temp=it, cooling_rate=cr, min_temp=mt), state)
                  for (it, cr, mt) in nqueens_algorithm_args for state in nqueens_states]


@pytest.mark.parametrize("algorithm, state", nqueens_config)
def test_simulated_annealing_nqueens(algorithm, state):
    p = NQueensProblem(dimension=8, initial=state)
    solution = algorithm.search(p)
    assert solution.state.is_goal()


knapsack_config = [(SimulatedAnnealing(h2, init_temp=it, cooling_rate=cr, min_temp=mt, time_limit=0.3), state)
                  for (it, cr, mt) in knapsack_algorithm_args for state in knapsack_states]


@pytest.mark.parametrize("algorithm, state", knapsack_config)
def test_simulated_annealing_knapsack(algorithm, state):
    p = KnapsackProblem(knapsack_weights, knapsack_values, sack_cap, state)
    solution = algorithm.search(p)
    assert h2(solution) == optimum





### USING SOLVER ###

nqueens_solver_config = [({"init_temp": it, "cooling_rate": cr, "min_temp": mt}, state)
                         for (it, cr, mt) in nqueens_algorithm_args for state in nqueens_states]


@pytest.mark.parametrize("algorithm_args, state", nqueens_solver_config)
def test_simulated_annealing_nqueens_solver(algorithm_args, state):
    solver = LocalSolver(NQUEENS, SIMULATED_ANNEALING, INVERSE_N_CONFLICTS, {"initial_state": state}, algorithm_args)
    solution = solver.solve()
    assert solution.final_state.is_goal()


nqueens_solver_config = [({"init_temp": it, "cooling_rate": cr, "min_temp": mt, "time_limit": 0.3}, state)
                         for (it, cr, mt) in knapsack_algorithm_args for state in knapsack_states]


@pytest.mark.parametrize("algorithm_args, state", nqueens_solver_config)
def test_simulated_annealing_knapsack_solver(algorithm_args, state):
    solver = LocalSolver(KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE,
                         {"weights": knapsack_weights, "values": knapsack_values, "sack_cap": sack_cap, "initial_state": state},
                         algorithm_args)
    solution = solver.solve()
    assert h2(Node(solution.final_state)) == optimum
