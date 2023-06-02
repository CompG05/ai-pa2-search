from typing import Optional

from algorithms.search_algorithm import Node, null_node


class Solution:
    def __init__(self, node: Node, value, algorithm_name, heuristic_name, dtime, memory_peak):
        self.final_state = node.state
        self.path = [node.state for node in node.path()]
        self.depth = node.depth
        self.algorithm_name = algorithm_name
        self.heuristic_name = heuristic_name
        self.time = dtime
        self.memory = memory_peak
        self.nodes = node.accum_nodes
        self.value = value

    @classmethod
    def not_found(cls, algorithm_name: str, heuristic_name: Optional[str]):
        return Solution(null_node, 0, algorithm_name, heuristic_name, 0, 0)

    def __str__(self):
        return f"""
algorithm: {self.algorithm_name}
final state: {self.final_state}
final state value: {self.value}
time: %.2f ms
generated nodes: {self.nodes}
max memory usage: {self.memory} bytes""" % self.time * 1000

    @classmethod
    def csv_header(cls):
        return "algorithm,heuristic,solution found,depth,final state,value,time,generated nodes,max memory usage"

    def to_csv(self):
        return f"{self.algorithm_name},{self.heuristic_name},{self.final_state is not None},{self.depth},\
        {self.final_state},{self.value},{self.time},{self.nodes},{self.memory}"
