import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import exp_schedule
from constants import KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE
from problems.nqueens import NQueensProblem
from solver.solver import Solver


def main():
    p = NQueensProblem(dimension=8)

    initial_temperatures = [200]  # [1]
    cooling_rates = [0.1]  # [0.005, 0.001]
    limits = [10000]  # [0.000001]

    iterations = 100
    file_name = "easy/f2_l-d_kp_20_878"

    with open("instances/optimum/" + file_name) as f:
        optimum = int(f.readline())
    print("Optimum:", optimum)

    for limit in limits:
        for init_temp in initial_temperatures:
            for cooling_rate in cooling_rates:
                solver = Solver(KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE,
                                problem_kwargs={"path": "instances/" + file_name},
                                algorithm_kwargs={"schedule": exp_schedule(init_temp, cooling_rate, limit)})
                solutions = 0
                times = []
                values = []
                last_it_values = []
                for i in range(iterations):
                    print("Voy por:", i)
                    bef_time = time.time()
                    solution = solver.solve()
                    solutions += solution.value == optimum
                    aft_time = time.time()
                    times.append(aft_time - bef_time)
                    values.append(solution.value)
                    last_it_values = [s.sack_value for s in solution.path]
                plt.plot(last_it_values)
                plt.show()
                solution_rate = solutions / iterations
                mean_time = sum(times) / len(times)
                mean_value = sum(values) / len(values)
                print(f"\nit: {init_temp}, cr: {cooling_rate}, mt: {limit}, solution rate: {solution_rate}, mean "
                      f"time: %.4f, mean value: {mean_value}" % mean_time)


if __name__ == "__main__":
    main()
