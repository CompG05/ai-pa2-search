import sys
import time
import matplotlib.pyplot as plt

from constants import KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE
from solver.local_solver import LocalSolver


def main(filename, config, iterations):
    init_temp, cooling_rate, min_temp = config

    print(
        f"Configuracion = init_temp: {init_temp}, cooling_rate: {cooling_rate}, min_temp: {min_temp}"
    )

    with open(filename + "_op") as f:
        optimum = float(f.readline())

    print(f"Instance: {filename}")
    print("Optimum:", optimum)

    solver = LocalSolver(
        KNAPSACK,
        SIMULATED_ANNEALING,
        ACCUM_VALUE,
        problem_kwargs={"path": filename},
        algorithm_kwargs={
            "init_temp": init_temp,
            "cooling_rate": cooling_rate,
            "min_temp": min_temp,
            "time_limit": 90,
        },
    )
    solutions = 0
    times = []
    values = []
    last_it_values = []
    for i in range(iterations):
        print("Voy por:", i + 1, end="\r")

        bef_time = time.time()
        solution = solver.solve()
        aft_time = time.time()

        tolerance = 1
        solutions += optimum - tolerance <= solution.value <= optimum + tolerance
        times.append(aft_time - bef_time)
        values.append(solution.value)
        last_it_values = [s.sack_value for s in solution.path]
    print()
    plt.plot(last_it_values)
    plt.show()

    solution_rate = solutions / iterations
    mean_time = sum(times) / len(times)
    mean_value = sum(values) / len(values)
    print(
        f"it: {init_temp}, cr: {cooling_rate}, mt: {min_temp}, solution rate: {solution_rate}, mean "
        f"time: %.4f, mean value: {mean_value}" % mean_time
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python -m experiments.knapsack.simulated_annealing.py <filename> <config_idx> <iterations>"
        )
        exit(1)

    configs = [(100, 0.0001, 0.0001)]

    filename = sys.argv[1]
    config = configs[int(sys.argv[2])]
    iterations = int(sys.argv[3])

    main(filename, config, iterations)
