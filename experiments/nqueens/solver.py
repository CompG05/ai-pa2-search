from solver.solver import Solver
from constants import *


def main():
    solver = Solver(
        NQUEENS,
        HILL_CLIMBING_RANDOM_RESTART,
        INVERSE_N_CONFLICTS,
        problem_kwargs={"dimension": 32},
        algorithm_kwargs={"exhaustive": False, "max_iterations": 100})
    solution = solver.solve()
    print(solution)


if __name__ == '__main__':
    main()
