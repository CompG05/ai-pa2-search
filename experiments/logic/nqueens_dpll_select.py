import time

from aima.logic import dpll_select, dpll, dpll_satisfiable, dpll_satisfiable_with_count
from logic.nqueens import to_expr

DIM = 4

def main(et, ps, uc):
    e = to_expr(DIM)
    btime = time.time()
    model, partial_count, total_count = dpll_select(e, et, ps, uc)
    atime = time.time()
    print(f"early_termination: {et}, pure_symbol: {ps}, unit_clause: {uc}")
    print("Model found:", model is not False)
    print(f"Partial models reached:", {partial_count})
    print(f"Total models reached:", {total_count})
    print("time: %.2f" % (atime-btime))
    print()

if __name__ == "__main__":
    params = [
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, True),
        (False, False, False)
    ]

    e = to_expr(DIM)
    btime = time.time()
    model, count = dpll_satisfiable_with_count(e)
    atime = time.time()
    print(f"DPLL:")
    print("Model found:", model is not False)
    print(f"models tested:", {count})
    print("time: %.2f" % (atime-btime))
    print()

    for param in params:
        main(*param)
