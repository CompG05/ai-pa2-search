from aima.logic import *


def deny_all_conflicts(dimension, x, y):
    """Return a conjunction of all conflicting cells, negated"""
    conflicts = []

    # for i in range(dimension):
    #     if i != y:
    #         conflicts.append(f"~Q{x}{i}")
    #     if i != x:
    #         conflicts.append(f"~Q{i}{y}")

    # Rows
    for j in range(y+1, dimension):
        conflicts.append(f"~Q{x}{j}")

    # Columns
    for i in range(x + 1, dimension):
        conflicts.append(f"~Q{i}{y}")

    for i in range(x+1, dimension):
        for j in range(dimension):
            if abs(i - x) == abs(j - y):
                conflicts.append(f"~Q{i}{j}")

    conflicts_str = " & ".join(conflicts)
    return f"({conflicts_str})"

def n_queens_formula(dimension):
    str_row = ""
    str_col = ""
    conflicts_str = ""

    for i in range(dimension):
        str_row += "("
        str_col += "("
        for j in range(dimension - 1):
            str_row += f"Q{i}{j} | "
            str_col += f"Q{j}{i} | "

        str_row += f"Q{i}{dimension-1}) & "
        str_col += f"Q{dimension-1}{i}) & "

    for i in range(dimension):
        for j in range(dimension):
            consecuente = deny_all_conflicts(dimension, i, j)
            if len(consecuente) > 2:
                conflicts_str += f"(Q{i}{j} ==> {consecuente}) & "
    conflicts_str = conflicts_str[:-3]

    return str_row + str_col + conflicts_str

def test_dpll_nqueens():
    dimension = 4

    print()
    print(n_queens_formula(dimension))
    result: dict[Expr, bool] = dpll_satisfiable(expr(n_queens_formula(dimension)))
    print()
    print(result)
    print()
    print(len(result.keys()))
    queens = 0
    for v in result.values():
        if v:
            queens += 1
    print(queens)

    for i in range(dimension):
        for j in range(dimension):
            if result[expr(f"Q{i}{j}")]:
                print("* ", end='')
            else:
                print("0 ", end='')
        print()
