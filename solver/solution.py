from typing import Optional

from algorithms.search_algorithm import Node, null_node


class Solution:
    def __init__(self, node: Node, value, algorithm_name, heuristic_name, problem_kwargs, algorithm_kwargs, dtime, memory_peak):
        self.final_state = node.state
        self.path = [node.state for node in node.path()]
        self.depth = node.depth
        self.algorithm_name = algorithm_name
        self.heuristic_name = heuristic_name
        self.problem_kwargs = problem_kwargs
        self.algorithm_kwargs = algorithm_kwargs
        self.time = dtime
        self.memory = memory_peak
        self.nodes = node.accum_nodes
        self.value = value

    @classmethod
    def not_found(cls, algorithm_name: str, heuristic_name: Optional[str], problem_kwargs, algorithm_kwargs):
        return Solution(null_node, 0, algorithm_name, heuristic_name, problem_kwargs, algorithm_kwargs, 0, 0)

    def __str__(self):
        return f"""
algorithm: {self.algorithm_name}
heuristic: {self.heuristic_name}
algorithm arguments: {self.algorithm_kwargs}
final state: {self.final_state}
final state value: {self.value}
time: %.2f ms
generated nodes: {self.nodes}
max memory usage: {self.memory} bytes""" % (self.time * 1000)

    @classmethod
    def csv_header(cls):
        return "algorithm,heuristic,algorithm args,final state,value,time,generated nodes,max memory usage"

    def to_csv(self):
        return f"{self.algorithm_name},{self.heuristic_name},{self.algorithm_kwargs},{self.final_state},{self.value},{self.time},{self.nodes},{self.memory}"
