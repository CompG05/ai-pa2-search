import sys
from constants import ACCUM_VALUE, hill_climbing_algorithms, KNAPSACK
from solver.local_solver import LocalSolver


def main():
    if len(sys.argv) != 3:
        print("Usage: python hill_climbing.py <file> <iterations>")
        exit(1)

    filename = sys.argv[1]
    iterations = int(sys.argv[2])

    with open(filename + "_op", "r") as f:
        optimum = int(f.readline())

    print(f"Optimum: {optimum}\n")

    for algorithm in hill_climbing_algorithms:
        solver = LocalSolver(
            KNAPSACK,
            algorithm,
            ACCUM_VALUE,
            problem_kwargs={"path": filename},
            algorithm_kwargs={"max_sideways_moves": 100, "exhaustive": False, "time_limit": 10})
        solved = 0

        values = []
        for i in range(iterations):
            print(f"Voy por: {i+1} de {algorithm}", end='\r')
            solution = solver.solve()

            solved += solution.value == optimum
            values.append(solution.value)
        print()

        solution_rate = solved / iterations
        print(f"{algorithm} solution rate: {solution_rate}, mean value: {sum(values) / len(values)}")
        print()


if __name__ == '__main__':
    main()
