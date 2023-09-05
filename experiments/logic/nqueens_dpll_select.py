from aima.logic import dpll_select
from logic.nqueens import to_expr


def main(et, ps, uc):
    e = to_expr(8)
    model, count = dpll_select(e, et, ps, uc)
    print(f"early_termination: {et}, pure_symbol: {ps}, unit_clause: {uc}")
    if not model:
        print("Try again capo")
    else:
        print(f"Model: {model}")
    print(f"models tested:", {count})

if __name__ == "__main__":
    params = [
        (True, True, True),
        # (True, False, False),
        # (False, True, False),
        # (False, False, True),
        # (False, False, False)
        (True, True, False),
        (True, False, True),
        (False, True, True),
    ]
    for param in params:
        main(*param)
