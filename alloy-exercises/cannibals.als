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
  next: State+Null,
}

fact valid_state {
  all s: State | (
    0 <= s.l_missionaries and 0 <= s.l_cannibals and
    0 <= s.r_missionaries and 0 <= s.r_cannibals and
    (s.l_missionaries >= s.l_cannibals or s.l_missionaries = 0) and
    (s.r_missionaries >= s.r_cannibals or s.r_missionaries = 0) and
    (s.boat in Side)
  )
}

fun sum_left[s: State]: Int { add[s.l_missionaries, s.l_cannibals] }
fun sum_right[s: State]: Int { add[s.r_missionaries, s.r_cannibals] }
fun total_sum[s: State]: Int { add[sum_left[s], sum_right[s]] }

fun left_diff[s1, s2: State]: Int { sub[sum_left[s1], sum_left[s2]] }
fun left_missionaries_diff[s1, s2: State]: Int { sub[s1.l_missionaries, s2.l_missionaries] }
fun left_cannibals_diff[s1, s2: State]: Int { sub[s1.l_cannibals, s2.l_cannibals] }


 pred same_population[s1, s2: State] {
   add[s1.l_missionaries, s1.r_missionaries] = add[s2.l_missionaries, s2.r_missionaries] and
   add[s1.l_cannibals, s1.r_cannibals] = add[s2.l_cannibals, s2.r_cannibals]
 }

fact valid_transition {
  all s: State | (
    s.next in State implies (
      s.boat != s.next.boat and
      same_population[s, s.next] and
      (s.boat = Left implies (
        left_diff[s, s.next] in 1+2 and
        left_missionaries_diff[s, s.next] in 0+1+2 and
        left_cannibals_diff[s, s.next] in 0+1+2
      )) and
      (s.boat = Right implies (
        left_diff[s.next, s] in 1+2 and
        left_missionaries_diff[s.next, s] in 0+1+2 and
        left_cannibals_diff[s.next, s] in 0+1+2
      ))
    )
  )
}

one sig InitialState extends State {} {
  l_missionaries = 3
  l_cannibals = 3
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

run {} for 12 State
