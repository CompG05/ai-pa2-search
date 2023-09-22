import pytest

from algorithms.local.hill_climbing import HillClimbingSideMovements, HillClimbing, RandomRestartHillClimbing
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

# Algorithms
hc_algorithms_nqueens = [HillClimbing(h), HillClimbingSideMovements(h, 100), RandomRestartHillClimbing(h, exhaustive=True)]
hc_algorithms_knapsack = [HillClimbing(h2), HillClimbingSideMovements(h2, 100), RandomRestartHillClimbing(h2, exhaustive=False, time_limit=0.3)]

# Problems args
knapsack_values = [70, 20, 39, 37, 7, 5, 10]
knapsack_weights = [31, 10, 20, 19, 4, 3, 6]
sack_cap = 50
optimum = 107

nqueens_config = [(algorithm, state) for algorithm in hc_algorithms_nqueens for state in nqueens_states]


@pytest.mark.parametrize("algorithm, state", nqueens_config)
def test_hill_climbing_nqueens(algorithm, state):
    p = NQueensProblem(dimension=8, initial=state)
    solution = algorithm.search(p)
    assert solution.state.is_goal()


knapsack_config = [(algorithm, state) for algorithm in hc_algorithms_knapsack for state in knapsack_states]

@pytest.mark.parametrize("algorithm, state", knapsack_config)
def test_hill_climbing_knapsack(algorithm, state):
    p = KnapsackProblem(knapsack_weights, knapsack_values, sack_cap, state)
    solution = algorithm.search(p)
    assert h2(solution) == optimum





### USING SOLVER ###

hc_algorithms_nqueens_solver = [(HILL_CLIMBING, {}),
                                (HILL_CLIMBING_SIDEWAYS, {"max_side_movements": 100}),
                                (HILL_CLIMBING_RANDOM_RESTART, {"exhaustive": True})]
nqueens_solver_config = [(algorithm, algorithm_args, state) for (algorithm, algorithm_args) in hc_algorithms_nqueens_solver for state in nqueens_states]


@pytest.mark.parametrize("algorithm, algorithm_args, state", nqueens_solver_config)
def test_hill_climbing_nqueens_solver(algorithm, algorithm_args, state):
    solver = LocalSolver(NQUEENS, algorithm, INVERSE_N_CONFLICTS, {"initial_state": state}, algorithm_args)
    solution = solver.solve()
    assert solution.final_state.is_goal()


hc_algorithms_knapsack_solver = [(HILL_CLIMBING, {}),
                                (HILL_CLIMBING_SIDEWAYS, {"max_side_movements": 100}),
                                (HILL_CLIMBING_RANDOM_RESTART, {"exhaustive": False, "time_limit": 0.3})]
nqueens_solver_config = [(algorithm, algorithm_args, state) for (algorithm, algorithm_args) in hc_algorithms_knapsack_solver for state in knapsack_states]


@pytest.mark.parametrize("algorithm, algorithm_args, state", nqueens_solver_config)
def test_hill_climbing_knapsack_solver(algorithm, algorithm_args, state):
    solver = LocalSolver(KNAPSACK, algorithm, ACCUM_VALUE,
                         {"weights": knapsack_weights, "values": knapsack_values, "sack_cap": sack_cap, "initial_state": state},
                         algorithm_args)
    solution = solver.solve()
    assert h2(Node(solution.final_state)) == optimum
