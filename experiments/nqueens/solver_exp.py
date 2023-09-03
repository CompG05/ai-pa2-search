from solver.local_solver import LocalSolver
from constants import *


def main():
    solver = LocalSolver(
        NQUEENS,
        HILL_CLIMBING_RANDOM_RESTART,
        INVERSE_N_CONFLICTS,
        problem_kwargs={"dimension": 32},
        algorithm_kwargs={"exhaustive": False, "max_iterations": 100})
    solution = solver.solve()
    print(solution)


if __name__ == '__main__':
    main()
