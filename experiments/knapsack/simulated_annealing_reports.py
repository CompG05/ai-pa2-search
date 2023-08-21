import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import exp_schedule
from solver.solution import Solution
from constants import KNAPSACK, SIMULATED_ANNEALING, ACCUM_VALUE
from problems.nqueens import NQueensProblem
from solver.local_solver import LocalSolver
import os


def main():
    configs = [(100, 0.0001, 0.0001)]
    iterations = 10
    file_name_list = ["easy/" + file for file in os.listdir("instances/easy") if file[-1] != 'p']

    for init_temp, cooling_rate, min_temp in configs:
        print(
            f"Configuracion = init_temp: {init_temp}, cooling_rate: {cooling_rate}, min_temp: {min_temp}"
        )
        total_solutions = 0
        for file_name in file_name_list:
            if not os.path.exists("reports/" + file_name):
                write_header("reports/" + file_name)

            with open("instances/" + file_name + "_op") as f:
                optimum = float(f.readline())
            print(f"Instance: {file_name}")
            print("Optimum:", optimum)

            solver = LocalSolver(
                KNAPSACK,
                SIMULATED_ANNEALING,
                ACCUM_VALUE,
                problem_kwargs={"path": "instances/" + file_name},
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
                print("\tVoy por:", i + 1)
                bef_time = time.time()
                solution = solver.solve()
                write_solution(solution, "reports/" + file_name)
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
            print(
                f"\n\tit: {init_temp}, cr: {cooling_rate}, mt: {min_temp}, solution rate: {solution_rate}, mean "
                f"time: %.4f, mean value: {mean_value}\n\n" % mean_time
            )

            total_solutions += solutions

        print(
            f"Total solution rate: {total_solutions/(len(file_name_list)*iterations)}"
        )


def write_solution(solution, output_file):
    with open(output_file, "a") as csvfile:
        csvfile.write(solution.to_csv() + "\n")


def write_header(output_file):
    with open(output_file, "w") as csvfile:
        csvfile.write(Solution.csv_header() + "\n")


if __name__ == "__main__":
    main()
