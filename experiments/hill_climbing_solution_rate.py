import sys

from constants import algorithms, NQUEENS, INVERSE_N_CONFLICTS
from problems.nqueens import NQueensProblem
from solver.solver import Solver


def main():
    if len(sys.argv) != 2:
        print("Usage: python hill_climbing_solution_rate.py <iterations>")
        exit(1)

    iterations = int(sys.argv[1])
    p = NQueensProblem(dimension=8)

    for algorithm in algorithms:
        solver = Solver(
            NQUEENS,
            algorithm,
            INVERSE_N_CONFLICTS,
            problem_kwargs={"dimension": 8},
            algorithm_kwargs={"max_sideways_moves": 100})
        solved = 0

        for _ in range(iterations):
            solution = solver.solve()
            solved += p.is_goal(solution.final_state)

        solution_rate = solved / iterations
        print(f"\n{algorithm} solution rate: {solution_rate}")


if __name__ == "__main__":
    main()
