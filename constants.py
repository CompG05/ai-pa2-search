from algorithms.local.hill_climbing import *
from problems.nqueens import NQueensProblem
from problems.knapsack import KnapsackProblem


NQUEENS = "nqueens"
KNAPSACK = "knapsack"

problems = {
    NQUEENS: NQueensProblem,
    KNAPSACK: KnapsackProblem,
}

HILL_CLIMBING = "hill_climbing"
HILL_CLIMBING_RANDOM_RESTART = "hill_climbing_random_restart"
HILL_CLIMBING_SIDEWAYS = "hill_climbing_sideways"

algorithms = {
    HILL_CLIMBING: HillClimbing,
    HILL_CLIMBING_RANDOM_RESTART: RandomRestartHillClimbing,
    HILL_CLIMBING_SIDEWAYS: HillClimbingSideMovements,
}

# nqueens heuristic
N_CONFLICTS = "n_conflicts"
INVERSE_N_CONFLICTS = "inverse_n_conflicts"

# knapsack heuristic
ACCUM_VALUE = "accumulated_value"

heuristics = {
    NQUEENS: [N_CONFLICTS],
    KNAPSACK: [ACCUM_VALUE],
}
