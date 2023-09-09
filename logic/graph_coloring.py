import pydot
from typing import Iterable, Literal

from aima.logic import dpll_satisfiable
from aima.utils import expr
from structures.graph import Graph


def graph_to_expr(g: Graph, k: int):
    """
    Converts a graph coloring problem with k colors into a propositional logic expression.
    - Every node can be of any color
    - Each node can only be of one color
    - If node A is of color C, then all its adjacents are not of color C
    """
    nodes = list(g.nodes())
    nodes.sort()  # To make it deterministic
    e = ""

    def negate_color_for_states(color: int, states: Iterable):
        states_with_color = [f"~{var(s, color)}" for s in states]
        return " & ".join(states_with_color)

    # All nodes must have at least one color

    all_nodes_with_all_colors_list = []
    for v in nodes:
        v_with_all_colors_l = []
        for c in range(0, k):
            v_with_all_colors_l.append(f"{var(v, c)}")
        v_with_all_colors = "(" + " | ".join(v_with_all_colors_l) + ")"

        all_nodes_with_all_colors_list.append(v_with_all_colors)
    all_nodes_with_all_colors = "(" + " & ".join(all_nodes_with_all_colors_list) + ")"

    # Each node can only be of one color

    each_node_only_one_color_l = []
    for v in nodes:
        if k == 1:  # If there is only one color, no need to check for other colors
            break
        v_only_one_color_l = []
        for c in range(0, k):
            v_only_c = f"({var(v, c)} ==> "
            other_colors_denied = []
            for other_c in range(c + 1, k):
                other_colors_denied.append(f"~{var(v, other_c)}")
            v_only_c += " & ".join(other_colors_denied) + ")"
            if len(other_colors_denied) != 0:
                v_only_one_color_l.append(v_only_c)
        v_only_one_color = " & ".join(v_only_one_color_l)
        each_node_only_one_color_l.append(v_only_one_color)

    if k == 1:
        e = all_nodes_with_all_colors
    else:
        each_node_only_one_color = "(" + " & ".join(each_node_only_one_color_l) + ")"
        e = (all_nodes_with_all_colors + " & " + each_node_only_one_color)

    # Adjacent nodes must have different colors

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
    if k > len(g.nodes()):
        raise ValueError(f"Cannot color graph with {k} colors: graph has only {len(g.nodes())} nodes")

    e = graph_to_expr(g, k)
    model = dpll_satisfiable(e)
    if model == False:
        return False

    result = {}

    for v in g.nodes():
        for c in range(0, k):
            if model[expr(var(v, c))]:
                result[v] = c

    return result


def write_colored_graph_dot(path: str, g: Graph, colors: list[str], color_map: dict[str, int]):
    """Write a colored graph to a dot file in graphviz format"""
    graph = pydot.Dot(graph_type="graph")

    for n in g.nodes():
        if color_map[n] not in range(len(colors)):
            raise ValueError(f"Not enough colors: index {color_map[n]} not in range {len(colors)}")

        graph.add_node(pydot.Node(n, color=colors[color_map[n]]))

    for n in g.nodes():
        for adj in g.get(n).keys():
            if n < adj:
                graph.add_edge(pydot.Edge(n, adj))
        if n in g.get(n).keys():
            graph.add_edge(pydot.Edge(n, n))

    graph.write(path)


def var(v: str, c: int):
    return f"{v.replace(' ', '_')}{c}"

