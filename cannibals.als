open util/integer

abstract sig Side {}
one sig Left, Right extends Side {}
one sig Null {}

sig State {
  l_missionaries: Int,
  l_cannibals: Int,
  r_missionaries: Int,
  r_cannibals: Int,
  boat: Side,
  next: (State+Null),
}

fact valid_state {
  all s: State | (
    0 <= s.l_missionaries and 0 <= s.l_cannibals and
    0 <= s.r_missionaries and 0 <= s.r_cannibals
  )
}

fun sum_left[s: State]: Int {
  add[s.l_missionaries, s.l_cannibals]
}

fun sum_right[s: State]: Int {
  add[s.r_missionaries, s.r_cannibals]
}

fun total_sum[s: State]: Int {
  add[sum_left[s], sum_right[s]]
}

fact valid_transition {
  all s: State | (
    s.next in State implies (
      s.boat != s.next.boat and
      total_sum[s] = total_sum[s.next] and
      (s.boat = Left implies (
        ((sum_left[s] = add[sum_left[s.next], 2] and sum_right[s] = sub[sum_right[s.next], 2]) or
        (sum_left[s] = add[sum_left[s.next], 1] and sum_right[s] = sub[sum_right[s.next], 1])) and
        s.next.l_missionaries = sub[s.l_missionaries, sub[s.next.r_missionaries, s.r_missionaries]] and
        s.next.l_cannibals = sub[s.l_cannibals, sub[s.next.r_cannibals, s.r_cannibals]]
      ))
      -- (s.boat = Right implies (
      --   ((sum_left[s] = sub[sum_left[s.next], 2] and sum_right[s] = add[sum_right[s.next], 2]) or
      --   (sum_left[s] = sub[sum_left[s.next], 1] and sum_right[s] = add[sum_right[s.next], 1])) and
      --   s.next.r_missionaries = sub[s.r_missionaries, sub[s.next.l_missionaries, s.l_missionaries]] and
      --   s.next.r_cannibals = sub[s.r_cannibals, sub[s.next.l_cannibals, s.l_cannibals]]
      -- ))

    )
  )
}

one sig InitialState extends State {}{
  l_missionaries = 5
  l_cannibals = 2
  r_missionaries = 0
  r_cannibals = 0
  boat = Left
}

fact valid_initial {
  all s: State | s in InitialState.*next
}

one sig FinalState extends State {}

fact valid_final {
  FinalState.l_missionaries = 0 and
  FinalState.l_cannibals = 0 and
  FinalState.r_missionaries = add[InitialState.l_missionaries, InitialState.r_missionaries] and
  FinalState.r_cannibals = add[InitialState.l_cannibals, InitialState.r_cannibals] and
  FinalState.boat = Right and
  FinalState.next = Null
}

run {} for 10 but 4 State
