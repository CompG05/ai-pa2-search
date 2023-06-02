NQUEENS = "nqueens"
KNAPSACK = "knapsack"

problems = [NQUEENS, KNAPSACK]


# nqueens heuristic
N_CONFLICTS = "n_conflicts"
INVERSE_N_CONFLICTS = "inverse_n_conflicts"

# knapsack heuristic
ACCUM_VALUE = "accumulated_value"

heuristics = {
    NQUEENS: [N_CONFLICTS],
    KNAPSACK: [ACCUM_VALUE],
}
