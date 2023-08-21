import sys

from constants import NQUEENS, INVERSE_N_CONFLICTS, hill_climbing_algorithms
from solver.local_solver import LocalSolver


def main():
    if len(sys.argv) != 3:
        print("Usage: python hill_climbing_solution_rate.py <dimension> <iterations>")
        exit(1)

    dimension = int(sys.argv[1])
    iterations = int(sys.argv[2])

    for algorithm in hill_climbing_algorithms:
        solver = LocalSolver(
            NQUEENS,
            algorithm,
            INVERSE_N_CONFLICTS,
            problem_kwargs={"dimension": dimension},
            algorithm_kwargs={"max_sideways_moves": 100, "exhaustive": True},
        )
        solved = 0

        for _ in range(iterations):
            solution = solver.solve()
            solved += solution.final_state.is_goal()

        solution_rate = solved / iterations
        print(f"\n{algorithm} solution rate: {solution_rate}")


if __name__ == "__main__":
    main()
