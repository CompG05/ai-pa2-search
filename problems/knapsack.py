import random

from problems.problem import Problem, Action, State, StateFactory


class KnapsackState(State):
    def __init__(
        self,
        data: list[bool],
        weights: list[float],
        values: list[float],
        sack_cap: float,
    ):
        super().__init__(data)
        self.weight = weights
        self.value = values
        self.sack_cap = sack_cap

    def is_goal(self) -> bool:
        return False

    @property
    def sack_weight(self) -> float:
        w = 0.0
        for i in range(len(self.data)):
            w += self.weight[i] if self.data[i] else 0
        return w

    @property
    def sack_value(self) -> float:
        v = 0
        for i in range(len(self.data)):
            v += self.value[i] if self.data[i] else 0
        return v

    @property
    def sack_rating(self) -> float:
        r = 0
        for i in range(len(self.data)):
            r += (self.value[i] / self.weight[i]) if self.data[i] else 0
        return r

    @property
    def n_items(self) -> int:
        return len(self.data)

    def is_valid(self) -> bool:
        if len(self.weight) != len(self.value) or len(self.weight) != len(self.data):
            return False

        if self.sack_weight > self.sack_cap:
            return False

        return True

    def __str__(self):
        s = "{}"
        content = [
            (f"w: {self.weight[i]}", f"v: {self.value[i]}")
            for i in range(self.n_items)
            if self.data[i]
        ]
        if len(content) > 0:
            s = str(content)

        return f"Knapsack{s}"

    def to_list(self):
        return self.data

    def to_csv(self) -> str:
        return ','.join(map(str, map(int, self.data)))

    def __hash__(self):
        return hash((self.data, self.weight, self.value, self.sack_cap))


class KnapsackStateFactory(StateFactory):
    def __init__(self, weights: list[float], values: list[float], sack_cap: float):
        super().__init__()
        self.weights = weights
        self.values = values
        self.sack_cap = sack_cap

    @property
    def n_items(self) -> int:
        return len(self.weights)

    def random(self) -> KnapsackState:
        content = [False] * self.n_items
        cap = random.random() * (self.sack_cap + 1)  # random float in [0, sack_cap]
        items = list(range(self.n_items))
        random.shuffle(items)
        cum_weight = 0

        item = items.pop()
        while items:
            if cum_weight + self.weights[item] <= cap:
                content[item] = True
                cum_weight += self.weights[item]
            item = items.pop()

        return KnapsackState(content, self.weights, self.values, self.sack_cap)


class Switch(Action):
    """Put in the given item if it's not in the knapsack, take it out otherwise"""

    def __init__(self, item: int):
        super().__init__(1)
        self.item: int = item

    def execute(self, state: KnapsackState) -> KnapsackState:
        content: list[bool] = state.data.copy()

        content[self.item] = not content[self.item]
        return KnapsackState(content, state.weight, state.value, state.sack_cap)

    def is_enabled(self, state: KnapsackState) -> bool:
        content: list[bool] = state.data

        # All items in the backpack can be taken out ; only fitting items can be put in
        return 0 <= self.item < state.n_items and (
            content[self.item]
            or state.sack_weight + state.weight[self.item] <= state.sack_cap
        )

    def __str__(self):
        return f"I{self.item}"

    def __repr__(self):
        return f"I{self.item}"

    def __hash__(self):
        return hash(self.item)

    def __eq__(self, other):
        return isinstance(other, Switch) and self.item == other.item


class KnapsackProblem(Problem):
    def __init__(
        self,
        weights: list[float],
        values: list[float],
        sack_cap: float,
        content: list[bool] = None,
    ):

        state = KnapsackState(content, weights, values, sack_cap) if content else None

        if not content and len(weights) != len(values):
            raise ValueError("Lists sizes don't match")
        if content and not state.is_valid():
                raise ValueError("Content is not valid or lists sizes don't match")

        super().__init__(initial_state=state)

        self.weight = weights
        self.value = values
        self.sack_cap = sack_cap
        self.actions = [Switch(i) for i in range(len(values))]
        self.state_factory = KnapsackStateFactory(weights, values, sack_cap)

    @property
    def default_genetic_args(self):
        from heuristics.knapsack import KnapsackHeuristic
        return {'num_genes': len(self.value), 'gene_space': [0, 1], 'fitness_func': KnapsackHeuristic().create_fitness("accumulated_value", self)}

    def state_from_list(self, content: list[bool]) -> KnapsackState:
        return KnapsackState(content, self.weight, self.value, self.sack_cap)

    def is_goal(self, _) -> bool:
        return False

    def enabled_actions(self, s: KnapsackState) -> list[Switch]:
        return [action for action in self.actions if action.is_enabled(s)]

    @classmethod
    def from_file(cls, path: str, content=None) -> 'KnapsackProblem':
        with open(path, "r") as f:
            lines = f.readlines()

        n_items_s, cap_s = lines[0].split(' ')
        n_items = int(n_items_s)
        cap = float(cap_s)
        weights = []
        values = []

        for i in range(1, n_items + 1):
            value_s, weight_s = lines[i].split(' ')
            weight = float(weight_s)
            value = float(value_s)
            weights.append(weight)
            values.append(value)

        return KnapsackProblem(weights, values, cap, content)
