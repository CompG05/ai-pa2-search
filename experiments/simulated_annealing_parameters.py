import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main():
    p = NQueensProblem(dimension=8)

    initial_temperatures = [1]
    cooling_rates = [0.005, 0.001]
    min_temperatures = [0.00000000000000001]

    n_conflicts = NQueensHeuristic().create(N_CONFLICTS)
    sim_annealing = SimulatedAnnealing(n_conflicts)
    iterations = 75
    _, ax = plt.subplots()

    for min_temp in min_temperatures:
        for init_temp in initial_temperatures:
            for cooling_rate in cooling_rates:
                sim_annealing.set_schedule(init_temp, cooling_rate, min_temp)
                solutions = 0
                steps = []
                times = []
                for _ in range(iterations):
                    bef_time = time.time()
                    solution_node = sim_annealing.search(p)
                    solutions += solution_node.state.is_goal()
                    aft_time = time.time()
                    steps.append(len(solution_node.path()))
                    times.append(aft_time - bef_time)
                solution_rate = solutions / iterations
                mean_steps = sum(steps) / len(steps)
                mean_time = sum(times) / len(times)
                print(f"\nit: {init_temp}, cr: {cooling_rate}, mt: {min_temp}, solution rate: {solution_rate}, mean "
                      f"steps: {mean_steps}, mean time: %.4f" % mean_time)




if __name__ == "__main__":
    main()