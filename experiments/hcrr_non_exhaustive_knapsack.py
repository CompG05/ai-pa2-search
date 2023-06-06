from algorithms.local.hill_climbing import RandomRestartHillClimbing
from constants import ACCUM_VALUE
from heuristics.knapsack import KnapsackHeuristic
from problems.knapsack import KnapsackProblem


def test_random_restart_non_exhaustive_knapsack():
    weights: list[float] = [5, 10, 30, 15, 40, 25, 65]
    values: list[float] = [1, 2, 7, 3, 9, 6, 10]
    cap = 75.0
    algorithm = RandomRestartHillClimbing(KnapsackHeuristic().create(ACCUM_VALUE), False, 10)
    problem = KnapsackProblem([False] * len(weights), weights, values, cap)
    print(algorithm.search(problem).state)


if __name__ == '__main__':
    test_random_restart_non_exhaustive_knapsack()
