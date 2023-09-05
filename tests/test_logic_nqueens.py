import pytest
from aima.logic import *
from logic.nqueens import to_expr, get_nqueens_model
from problems.nqueens import NQueensState

nqueens_expr_config = [
    (2, expr("(((((((Q00 | Q01) & (Q10 | Q11)) & "
             "(Q00 | Q10)) & (Q01 | Q11)) & "
             "(Q00 ==> ((~Q01 & ~Q10) & ~Q11))) & (Q01 ==> (~Q11 & ~Q10))) & (Q10 ==> ~Q11))")),
    (3, expr("(Q00 | Q01 | Q02) & (Q10 | Q11 | Q12) & (Q20 | Q21 | Q22) & "
             "(Q00 | Q10 | Q20) & (Q01 | Q11 | Q21) & (Q02 | Q12 | Q22) & "
             "(Q00 ==> (~Q01 & ~Q02 & ~Q10 & ~Q20 & ~Q11 & ~Q22)) & "
             "(Q01 ==> (~Q02 & ~Q11 & ~Q21 & ~Q10 & ~Q12)) & "
             "(Q02 ==> (~Q12 & ~Q22 & ~Q11 & ~Q20)) & "
             "(Q10 ==> (~Q11 & ~Q12 & ~Q20 & ~Q21)) & "
             "(Q11 ==> (~Q12 & ~Q21 & ~Q20 & ~Q22)) & "
             "(Q12 ==> (~Q22 & ~Q21)) & "
             "(Q20 ==> (~Q21 & ~Q22)) & "
             "(Q21 ==> (~Q22))"))
]


@pytest.mark.parametrize("dimension, expected", nqueens_expr_config)
def test_nqueens_to_expr(dimension: int, expected: Expr):
    nqueens_expr = to_expr(dimension)
    assert nqueens_expr == expected


dimensions_config = [4, 8, 12]


@pytest.mark.parametrize("dimension", dimensions_config)
def test_nqueens_dpll(dimension: int):
    solution = get_nqueens_model(dimension)
    solution_state = NQueensState(solution)
    assert solution_state.is_goal()