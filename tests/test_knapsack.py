import pytest

from problems.knapsack import Switch, KnapsackState, KnapsackProblem

#                       0   1   2   3   4   5   6
weights: list[float] = [5, 10, 30, 15, 40, 25, 50]
values: list[float] =  [1,  2,  7,  3,  9,  6, 12]
cap = 75.0


def s(content):
    c = [False] * len(weights)
    for i in content:
        c[i] = True
    return KnapsackState(c, weights, values, cap)


action_is_enabled_config = [
    (Switch(1), s([6, 3]), True),
    (Switch(2), s([1, 2, 3]), True),
    (Switch(-1), s([6, 3]), False),
    (Switch(7), s([6, 3]), False),
]


@pytest.mark.parametrize("action, state, expected", action_is_enabled_config)
def test_action_is_enabled(action, state, expected):
    assert action.is_enabled(state) == expected


execute_action_config = [
    (Switch(6), s([1, 3]), s([1, 3, 6])),
    (Switch(6), s([1, 3, 6]), s([1, 3])),
    (Switch(1), s([2, 4]), s([1, 2, 4])),
    (Switch(1), s([1, 2, 4]), s([2, 4])),
]


@pytest.mark.parametrize("action, state, expected", execute_action_config)
def test_action_execute(action, state, expected):
    assert action.execute(state) == expected


def test_enabled_actions():
    problem = KnapsackProblem(weights, values, cap, [False] * len(weights))

    assert problem.enabled_actions(s([1, 3])) == [Switch(i) for i in [0, 1, 2, 3, 4, 5, 6]]
