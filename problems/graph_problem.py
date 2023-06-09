from problems.problem import Action, Problem, State
from structures.graph import Graph


class Vertex:
    def __init__(self, current, goal):
        self.current = current
        self.goal = goal

    def is_goal(self):
        return self.goal == self.current

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.current == other.current

    def __hash__(self):
        return hash(self.current)

    def __str__(self):
        return str(self.current)

    def __repr__(self):
        return self.current.__repr__()


class Edge(Action):
    """Represents a transition to another node in a graph"""

    def __init__(self, graph: Graph, source, dest):
        super().__init__()
        self.graph = graph
        self.source = source
        self.dest = dest
        self.cost = graph.get(source, dest)

    def execute(self, source: Vertex) -> Vertex:
        return Vertex(self.dest, source.goal)

    def is_enabled(self, source: Vertex) -> bool:
        return source.current == self.source and self.dest in self.graph.get(self.source)

    def __eq__(self, other):
        return isinstance(other, Edge) and \
            self.graph == other.graph \
            and self.source == other.source \
            and self.dest == other.dest \
            and self.cost == other.cost

    def __hash__(self) -> int:
        t = (self.source, self.dest, self.cost)
        return t.__hash__()

    def __repr__(self):
        return self.source.__str__() + " -> " + self.dest.__str__() + " (" + self.cost.__str__() + ")"


class GraphProblem(Problem):
    """Represents a single source-single destination graph problem"""

    def __init__(self, graph: Graph, initial, goal):
        super().__init__()
        self.initial_state = Vertex(initial, goal)
        self.goal_state = Vertex(goal, goal)
        self.graph = graph
        self.edges = [Edge(self.graph, source, dest)
                      for source in graph.nodes()
                      for dest in graph.get(source).keys()]

    def enabled_actions(self, source: Vertex) -> list[Edge]:
        return [edge for edge in self.edges if edge.source == source.current]
