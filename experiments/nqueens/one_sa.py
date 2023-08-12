import argparse
import time
import matplotlib.pyplot as plt
from algorithms.local.simulated_annealing import SimulatedAnnealing
from constants import INVERSE_N_CONFLICTS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--dimension", "-d", type=int, default=8)
    argparser.add_argument("--initial_temperature", "-it", type=float, default=1)
    argparser.add_argument("--cooling_rate", "-cr", type=float, default=0.0005)
    argparser.add_argument("--min_temperature", "-mt", type=float, default=0.001)
    argparser.add_argument("--time_limit", "-tl", type=float)
    args = argparser.parse_args()

    h = NQueensHeuristic().create(INVERSE_N_CONFLICTS)
    a = SimulatedAnnealing(
        h,
        init_temp=args.initial_temperature,
        cooling_rate=args.cooling_rate,
        min_temp=args.min_temperature,
        time_limit=args.time_limit,
    )
    p = NQueensProblem(dimension=args.dimension)

    bef = time.time()
    node = a.search(p)
    aft = time.time()

    plt.plot(list(range(len(node.path()))), [h(n) for n in node.path()])
    plt.text(0, 0, "time: %.2f s" % (aft - bef))
    plt.text(0, -1, "final value: %.2f" % h(node))
    plt.show()


if __name__ == "__main__":
    main()
