from algorithms.local.hill_climbing import *
from algorithms.local.simulated_annealing import SimulatedAnnealing
from algorithms.local.genetic import GeneticSearch
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

GENETIC = "genetic"

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
    GENETIC: GeneticSearch,
}

# nqueens heuristic
N_CONFLICTS = "n_conflicts"
INVERSE_N_CONFLICTS = "inverse_n_conflicts"
INVERSE_N_CONFLICTS_FITNESS = "inverse_n_conlicts_fitness"

# knapsack heuristic
ACCUM_VALUE = "accumulated_value"
ACCUM_RATING = "accumulated_rating"
ACCUM_VALUE_FITNESS = "accum_value_fitness"

heuristics = {
    NQUEENS: [INVERSE_N_CONFLICTS, N_CONFLICTS],
    KNAPSACK: [ACCUM_VALUE],
}

fitness = {
    NQUEENS: [INVERSE_N_CONFLICTS_FITNESS],
    KNAPSACK: [ACCUM_VALUE_FITNESS],
}
