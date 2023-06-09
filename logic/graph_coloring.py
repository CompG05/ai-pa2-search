from typing import Iterable, Literal

from aima.logic import dpll_satisfiable
from aima.utils import expr
from structures.graph import Graph


def graph_to_expr(g: Graph, k: int):
    """Converts a graph coloring problem with k colors into a propositional logic expression"""
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
        if k == 1:  # If there is only one color, no need to check for other colors
            break
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

    if k == 1:
        e = all_nodes_with_all_colors
    else:
        each_node_only_one_color = "(" + " & ".join(each_node_only_one_color_l) + ")"
        e = (all_nodes_with_all_colors + " & " + each_node_only_one_color)

    adjacents_different_color_l = []
    for v in nodes:
        adjacents = [adj for adj in g.get(v).keys() if adj != v]
        for c in range(0, k):
            v_adj_diff_color = negate_color_for_states(c, adjacents)
            if v_adj_diff_color != "":
                adjacents_different_color_l.append(f"({var(v, c)} ==> {v_adj_diff_color})")
    if adjacents_different_color_l:
        adjacents_different_color = "(" + " & ".join(adjacents_different_color_l) + ")"
        e += " & " + adjacents_different_color

    return expr(e)


def get_graph_coloring_model(g: Graph, k: int) -> dict[str, int] | Literal[False]:
    """Returns a model for a graph coloring problem with k colors as a dict[vertex, color]"""
    e = graph_to_expr(g, k)
    model = dpll_satisfiable(e)
    if model == False:
        return False

    result = {}

    for v in g.nodes():
        for c in range(0, k):
            if model[expr(f"{v}{c}")]:
                result[v] = c

    return result
