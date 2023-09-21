import sys
import time
import matplotlib.pyplot as plt

from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main(dimension, config, iterations):
    init_temp, cooling_rate, min_temp = config

    p = NQueensProblem(dimension=dimension)
    n_conflicts = NQueensHeuristic().create(INVERSE_N_CONFLICTS)

    sim_annealing = SimulatedAnnealing(
        n_conflicts,
        init_temp=init_temp,
        cooling_rate=cooling_rate,
        min_temp=min_temp,
    )

    solutions = 0
    steps = []
    times = []
    values = []
    l = 0
    for i in range(iterations):
        print("Voy por:", i, end="\r")
        bef_time = time.time()
        solution_node = sim_annealing.search(p)
        aft_time = time.time()

        solutions += solution_node.state.is_goal()
        steps.append(len(solution_node.path()))
        times.append(aft_time - bef_time)
        values = [n_conflicts(n) for n in solution_node.path()]
        l = len(solution_node.path())
    print()
    plt.plot(list(range(l)), values)
    plt.show()
    solution_rate = solutions / iterations
    mean_steps = sum(steps) / len(steps)
    mean_time = sum(times) / len(times)
    print(
        f"\nit: {init_temp}, cr: {cooling_rate}, mt: {min_temp}, solution rate: {solution_rate}, mean "
        f"steps: {mean_steps}, mean time: %.4f" % mean_time
    )


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python -m experiments.nqueens.simulated_annealing.py <dimension> <config_idx> <iterations>"
        )
        exit(1)

    configs = [
        (1, 0.001, 0.00001),
        (1, 0.005, 0.00001),
        (1, 0.001, 0.000001),
    ]

    dimension = int(sys.argv[1])
    config = configs[int(sys.argv[2])]
    iterations = int(sys.argv[3])

    main(dimension, config, iterations)
