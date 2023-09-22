import pytest

from problems.nqueens import NQueensState, NQueensProblem, NQueensAction

conflicted_config = [
    (4, 0, 7, 3, True),
    (7, 1, 1, 7, True),
    (1, 3, 1, 8, True),
    (1, 4, 5, 4, True),
    (0, 0, 2, 1, False),
]


@pytest.mark.parametrize("row1, col1, row2, col2, expected", conflicted_config)
def test_conflicted(row1, col1, row2, col2, expected):
    assert NQueensState.conflicted(row1, col1, row2, col2) == expected


n_conflicts_config = [
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 3)), 0),
    (NQueensState((4, 2, 1, 6, 1, 7, 5, 3)), 3),
    (NQueensState((4, 2, 1, 2, 1, 7, 5, 3)), 7),
    (NQueensState((4, 2, 1, 2, 1, 7, 5, 2)), 9),
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 1)), 1)
]


@pytest.mark.parametrize("state, expected", n_conflicts_config)
def test_n_conflicts(state, expected):
    assert state.n_conflicts() == expected


move_queen_config = [
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 5, 1, NQueensState((0, 1, 2, 3, 4, 1, 6, 7))),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 0, 1, NQueensState((1, 1, 2, 3, 4, 5, 6, 7))),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), 7, 1, NQueensState((0, 1, 2, 3, 4, 5, 6, 1))),
]


@pytest.mark.parametrize("state, column, delta, expected", move_queen_config)
def test_move_queen(state, column, delta, expected):
    assert state.move_queen(column, delta) == expected


is_goal_config = [
    (NQueensState((6, 4, 2, 0, 5, 7, 1, 3)), True),
    (NQueensState((4, 2, 0, 6, 1, 7, 5, 1)), False)
]


@pytest.mark.parametrize("state, expected", is_goal_config)
def test_is_goal(state, expected):
    assert state.is_goal() == expected


is_valid_config = [
    (NQueensState((0, 1, 2, 3, 4, 5, 6, -1)), False),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 8)), False),
    (NQueensState((0, 1, 2, 3, 4, 5, 6, 7)), True),
    (NQueensState((0, 0, 0, 0, 0, 0, 0, 0)), True)
]


@pytest.mark.parametrize("state, expected", is_valid_config)
def test_is_valid(state, expected):
    assert state.is_valid() == expected


enabled_actions_config = [
    (
        NQueensState((0, 1, 2, 3, 4, 5, 6, 7)),
        # [NQueensAction(i, j) for i in [0..7] for j in [0..i-1, i+1..7]
        [NQueensAction(i, j) for i in range(8) for j in list(range(i)) + list(range(i + 1, 8))]
    )
]


@pytest.mark.parametrize("state, expected", enabled_actions_config)
def test_enabled_actions(state, expected):
    assert NQueensProblem(8).enabled_actions(state) == expected
