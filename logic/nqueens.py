from aima.logic import dpll_satisfiable
from aima.utils import expr, Expr


def deny_all_conflicts(dimension, x, y):
    """Return a conjunction of all conflicting cells, negated"""
    conflicts = []

    # Rows
    for j in range(y + 1, dimension):
        conflicts.append(f"~Q{x}{j}")

    # Columns
    for i in range(x + 1, dimension):
        conflicts.append(f"~Q{i}{y}")

    for i in range(x + 1, dimension):
        for j in range(dimension):
            if abs(i - x) == abs(j - y):
                conflicts.append(f"~Q{i}{j}")

    conflicts_str = " & ".join(conflicts)
    return f"({conflicts_str})"


def to_expr(dim: int) -> Expr:
    str_row = ""
    str_col = ""
    conflicts_str = ""

    for i in range(dim):
        str_row += "("
        str_col += "("
        for j in range(dim - 1):
            str_row += f"Q{i}{j} | "
            str_col += f"Q{j}{i} | "

        str_row += f"Q{i}{dim - 1}) & "
        str_col += f"Q{dim - 1}{i}) & "

    for i in range(dim):
        for j in range(dim):
            consecuente = deny_all_conflicts(dim, i, j)
            if len(consecuente) > 2:
                conflicts_str += f"(Q{i}{j} ==> {consecuente}) & "
    conflicts_str = conflicts_str[:-3]

    return expr(str_row + str_col + conflicts_str)


def get_nqueens_model(dim: int) -> tuple[int]:
    e = to_expr(dim)
    model = dpll_satisfiable(e)
    result = [-1] * dim

    for i in range(dim):
        for j in range(dim):
            if model[expr(f"Q{i}{j}")]:
                result[i] = j

    return tuple(result)
