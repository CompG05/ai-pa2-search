from typing import Iterable


class State:
    def __init__(self, data):
        self.data = data

    def is_goal(self) -> bool:
        raise NotImplementedError

    def is_valid(self) -> bool:
        raise NotImplementedError

    def __eq__(self, other: 'State'):
        return self.data == other.data and isinstance(other, type(self))

    def __hash__(self):
        return hash(self.data)


class StateFactory:
    def random(self):
        raise NotImplementedError


class Action:
    def __init__(self, cost: float = 1):
        self.cost = cost

    def execute(self, state: State) -> State:
        raise NotImplementedError

    def is_enabled(self, state: State) -> bool:
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other: 'Action'):
        raise NotImplementedError


class Problem:
    """Abstract class for a formal representation of a search problem"""

    def __init__(self, initial_state=None):
        self.initial_state = initial_state
        self.state_factory = StateFactory()

    def restart_initial(self):
        self.initial_state = self.state_factory.random()

    def is_goal(self, state: State) -> bool:
        return state.is_goal()

    def result(self, state: State, action: Action) -> State:
        return action.execute(state)

    def enabled_actions(self, state: State) -> list[Action]:
        raise NotImplementedError

    @staticmethod
    def state_from_list(lst: list) -> State:
        raise NotImplementedError
