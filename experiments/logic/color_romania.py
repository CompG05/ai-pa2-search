from logic.graph_coloring import get_graph_coloring_model, write_colored_graph_dot
from structures.graph import Graph, UndirectedGraph


def main():
    romania_map = UndirectedGraph(
        dict(
            Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
            Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
            Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
            Drobeta=dict(Mehadia=75),
            Eforie=dict(Hirsova=86),
            Fagaras=dict(Sibiu=99),
            Hirsova=dict(Urziceni=98),
            Iasi=dict(Vaslui=92, Neamt=87),
            Lugoj=dict(Timisoara=111, Mehadia=70),
            Oradea=dict(Zerind=71, Sibiu=151),
            Pitesti=dict(Rimnicu=97),
            Rimnicu=dict(Sibiu=80),
            Urziceni=dict(Vaslui=142),
        )
    )

    color_map = get_graph_coloring_model(romania_map, 3)
    if color_map != False:
        write_colored_graph_dot("colored_romania.dot", romania_map, ["red", "blue", "green"], color_map)

    print(color_map)


if __name__ == "__main__":
    main()
