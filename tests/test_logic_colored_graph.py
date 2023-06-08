from typing import Iterable

from aima.logic import dpll_satisfiable
from aima.utils import expr
from structures.graph import Graph


def logic_colored_graph(g: Graph, k: int):
    nodes = list(g.nodes())
    e = ""

    def negate_color_for_states(color: int, states: Iterable):
        states_with_color = [f"~{var(s, color)}" for s in states]
        return " & ".join(states_with_color)
    
    def var(v: str, c: int):
        return f"{v}{c}"

    all_nodes_with_all_colors_list = []
    for v in nodes:
        v_with_all_colors_l = []
        for c in range(0, k):
            v_with_all_colors_l.append(f"{var(v, c)}")
        v_with_all_colors = "(" + " | ".join(v_with_all_colors_l) + ")"

        all_nodes_with_all_colors_list.append(v_with_all_colors)
    all_nodes_with_all_colors = "(" + " & ".join(all_nodes_with_all_colors_list) + ")"

    each_node_only_one_color_l = []
    for v in nodes:
        v_only_one_color_l = []
        for c in range(0, k):
            v_only_c = f"({var(v, c)} ==> "
            other_colors_denied = []
            for other_c in range(0, k):
                if c == other_c:
                    continue
                other_colors_denied.append(f"~{var(v, other_c)}")
            v_only_c += " & ".join(other_colors_denied) + ")"
            v_only_one_color_l.append(v_only_c)
        v_only_one_color = " & ".join(v_only_one_color_l)
        each_node_only_one_color_l.append(v_only_one_color)
    each_node_only_one_color = "(" + " & ".join(each_node_only_one_color_l) + ")"

    e = (
            all_nodes_with_all_colors
            + " & "
            + each_node_only_one_color
    )

    adjacents_different_color_l = []
    for v in nodes:
        adjacents = [adj for adj in g.get(v).keys() if adj != v]
        for c in range(0, k):
            v_adj_diff_color = negate_color_for_states(c, adjacents)
            print(v_adj_diff_color)
            if v_adj_diff_color != "":
                adjacents_different_color_l.append(f"({var(v, c)} ==> {v_adj_diff_color})")
    if adjacents_different_color_l:
        adjacents_different_color = "(" + " & ".join(adjacents_different_color_l) + ")"
        e += " & " + adjacents_different_color

    exp = expr(e)
    result = dpll_satisfiable(exp)
    print(result)


def test_logic_colored_graph():
    graph = Graph(dict(
        A=dict(B=0, C=0, D=0),
        B=dict(E=0),
        C=dict(F=0),
        D=dict(F=0)))

    logic_colored_graph(graph, 2)
    assert False
