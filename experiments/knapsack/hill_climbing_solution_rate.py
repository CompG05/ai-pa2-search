from constants import ACCUM_VALUE, hill_climbing_algorithms, KNAPSACK
from solver.local_solver import LocalSolver


def main():
    file_name = "easy/f1_l-d_kp_10_269"
    iterations = 10

    with open("instances/" + file_name + "_op", "r") as f:
        optimum = int(f.readline())

    print(f"Optimum: {optimum}")

    for algorithm in hill_climbing_algorithms:
        solver = LocalSolver(
            KNAPSACK,
            algorithm,
            ACCUM_VALUE,
            problem_kwargs={"path": "instances/" + file_name},
            algorithm_kwargs={"max_sideways_moves": 100, "exhaustive": False, "time_limit": 10})
        solved = 0

        values = []
        for i in range(iterations):
            print(f"Voy por: {i} de {algorithm}")
            solution = solver.solve()

            solved += solution.value == optimum
            values.append(solution.value)

        solution_rate = solved / iterations
        print(f"{algorithm} solution rate: {solution_rate}, mean value: {sum(values) / len(values)}")


if __name__ == '__main__':
    main()
