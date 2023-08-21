import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main():
    p = NQueensProblem(dimension=8)

    initial_temperatures = [1]  # [1]
    cooling_rates = [0.001]  # [0.005, 0.001]
    min_temps = [0.00001]  # [0.000001]

    n_conflicts = NQueensHeuristic().create(INVERSE_N_CONFLICTS)

    iterations = 15
    _, ax = plt.subplots()

    for min_temp in min_temps:
        for init_temp in initial_temperatures:
            for cooling_rate in cooling_rates:
                sim_annealing = SimulatedAnnealing(n_conflicts, init_temp=init_temp, cooling_rate=cooling_rate, min_temp=min_temp)
                solutions = 0
                steps = []
                times = []
                values = []
                l = None
                for i in range(iterations):
                    print("Voy por:", i)
                    bef_time = time.time()
                    solution_node = sim_annealing.search(p)
                    solutions += solution_node.state.is_goal()
                    aft_time = time.time()
                    steps.append(len(solution_node.path()))
                    times.append(aft_time - bef_time)
                    values = [n_conflicts(n) for n in solution_node.path()]
                    l = len(solution_node.path())
                plt.plot(list(range(l)), values)
                plt.show()
                solution_rate = solutions / iterations
                mean_steps = sum(steps) / len(steps)
                mean_time = sum(times) / len(times)
                print(f"\nit: {init_temp}, cr: {cooling_rate}, mt: {min_temp}, solution rate: {solution_rate}, mean "
                      f"steps: {mean_steps}, mean time: %.4f" % mean_time)


if __name__ == "__main__":
    main()
