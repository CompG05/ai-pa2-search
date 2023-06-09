from typing import Iterable

from aima.logic import dpll_satisfiable
from aima.utils import expr
from structures.graph import Graph


def test_logic_colored_graph():
    graph = Graph(dict(
        A=dict(B=0, C=0, D=0),
        B=dict(E=0),
        C=dict(F=0),
        D=dict(F=0)))

    logic_colored_graph(graph, 2)
    assert False
