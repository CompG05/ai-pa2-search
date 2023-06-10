from algorithms.local.hill_climbing import *
from algorithms.local.simulated_annealing import SimulatedAnnealing
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

SIMULATED_ANNEALING = "simulated_annealing"

hill_climbing_algorithms = {
    HILL_CLIMBING: HillClimbing,
    HILL_CLIMBING_RANDOM_RESTART: RandomRestartHillClimbing,
    HILL_CLIMBING_SIDEWAYS: HillClimbingSideMovements,
}

algorithms = {
    HILL_CLIMBING: HillClimbing,
    HILL_CLIMBING_RANDOM_RESTART: RandomRestartHillClimbing,
    HILL_CLIMBING_SIDEWAYS: HillClimbingSideMovements,
    SIMULATED_ANNEALING: SimulatedAnnealing,
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

from heuristics.nqueens import inverse_n_conflicts_fitness

fitness = {INVERSE_N_CONFLICTS: inverse_n_conflicts_fitness}
