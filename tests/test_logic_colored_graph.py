import pytest

from aima.utils import expr, Expr
from logic.graph_coloring import graph_to_expr
from structures.graph import Graph, UndirectedGraph

g1 = UndirectedGraph({"A": {"B": 1}})
g2 = Graph({"A": {"B": 1, "C": 1}})


graph_to_expr_config = [
    (g1, 2, expr("((A0 | A1) & (B0 | B1)) & "
                 "((A0 ==> ~A1) & (B0 ==> ~B1)) & "
                 "((A0 ==> ~B0) & (A1 ==> ~B1) & (B0 ==> ~A0) & (B1 ==> ~A1))")),

    (g2, 2, expr("((A0 | A1) & (B0 | B1) & (C0 | C1)) & "
                 "((A0 ==> ~A1) & (B0 ==> ~B1) & (C0 ==> ~C1)) & "
                 "((A0 ==> (~B0 & ~C0)) & (A1 ==> (~B1 & ~C1)))"))
]


@pytest.mark.parametrize("g, k, expected", graph_to_expr_config)
def test_graph_to_expr(g: Graph, k: int, expected: Expr):
    result = graph_to_expr(g, k)
    assert result == expected
