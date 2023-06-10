from logic.graph_coloring import get_graph_coloring_model, write_colored_graph_dot
from structures.graph import Graph


def main():
    graph = Graph(dict(
        A=dict(B=0, C=0, D=0),
        B=dict(E=0),
        C=dict(F=0),
        D=dict(F=0)))

    color_map = get_graph_coloring_model(graph, 2)
    if color_map != False:
        write_colored_graph_dot("gr.dot", graph, ["red", "blue"], color_map)

    print(color_map)


if __name__ == "__main__":
    main()
