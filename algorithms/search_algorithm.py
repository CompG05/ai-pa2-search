from problems.problem import Problem


class Node:
    def __init__(self,
                 state,
                 accum_nodes: int = 1,
                 parent: 'Node' = None):
        self.state = state
        self.accum_nodes = accum_nodes
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem: Problem) -> list['Node']:
        enabled_actions = problem.enabled_actions(self.state)
        total_nodes = self.accum_nodes + len(enabled_actions)

        return [Node(problem.result(self.state, action), accum_nodes=total_nodes, parent=self)
                for action in enabled_actions]

    def in_path(self, state) -> bool:
        node = self.parent
        while node:
            if node.state == state:
                return True
            node = node.parent
        return False

    def path(self) -> list['Node']:
        node = self
        reversed_path = []
        while node:
            reversed_path.append(node)
            node = node.parent
        return list(reversed(reversed_path))


null_node = Node(None, accum_nodes=-1)


class SearchAlgorithm:
    def search(self, problem: Problem) -> Node:
        raise NotImplementedError
