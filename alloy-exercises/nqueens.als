open util/integer

sig Queen {
	row: one Int,
	col: one Int
}

one sig Board {
	dimension: one Int,
	queens: set Queen
}

fact valid_board {
	Board.dimension = #Board.queens
	all q: Queen | q in Board.queens and
	               0 <= q.row and q.row < Board.dimension and
		   		   0 <= q.col and q.col < Board.dimension and
	all disj q1, q2: Queen | !eq[q1.row, q2.row] or !eq[q1.col, q2.col]
	
}

pred same_row_or_col[q1, q2: Queen] {
	eq[q1.row, q2.row] or eq[q1.col, q2.col]
}

pred same_diagonal[q1, q2: Queen] {
	-- q1.row - q2.row = q1.col - q2.col or
	-- q1.row - q2.row = q2.col - q1.col
	eq[ minus[q1.row, q2.row], minus[q1.col, q2.col] ] or
	eq[ minus[q1.row, q2.row], minus[q2.col, q1.col] ]
}

pred no_conflicts[q1, q2: Queen] {
	!same_row_or_col[q1, q2] and !same_diagonal[q1, q2]
}

run {all disj q1, q2: Queen | no_conflicts[q1, q2]} for exactly 16 Queen, 6 Int
