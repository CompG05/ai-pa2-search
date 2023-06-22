import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import exp_schedule
from constants import KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE
from problems.nqueens import NQueensProblem
from solver.solver import Solver
import os


def main():
    configs = [(400, 0.00007, 90000)]
    iterations = 10
    file_name_list = ["easy/" + file for file in os.listdir("instances/easy")]


    for (init_temp, cooling_rate, limit) in configs:
        print(f"Configuracion = init_temp: {init_temp}, cooling_rate: {cooling_rate}, limit: {limit}")
        total_solutions = 0
        for file_name in file_name_list:
            with open("instances/optimum/" + file_name) as f:
                optimum = float(f.readline())
            print("Optimum:", optimum)

            solver = Solver(KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE,
                            problem_kwargs={"path": "instances/" + file_name},
                            algorithm_kwargs={"schedule": exp_schedule(init_temp, cooling_rate, limit)})
            solutions = 0
            times = []
            values = []
            last_it_values = []
            for i in range(iterations):
                print("\tVoy por:", i, " de ", file_name)
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
            print(f"\n\tit: {init_temp}, cr: {cooling_rate}, lt: {limit}, solution rate: {solution_rate}, mean "
                  f"time: %.4f, mean value: {mean_value}" % mean_time)

            total_solutions += solutions

        print(f"Total solution rate: {total_solutions/(len(file_name_list)*iterations)}")


if __name__ == "__main__":
    main()
