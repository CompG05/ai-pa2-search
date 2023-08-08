#/bin/sh

solve="python solve.py"

states_dir="reports/states"
solution_dir="reports/solutions"
eight_queens_solution_dir="${solution_dir}/eight_queens"
sixteen_queens_solution_dir="${solution_dir}/sixteen_queens"
thirty_two_queens_solution_dir="${solution_dir}/thirty_two_queens"

mkdir -p ${eight_queens_solution_dir}
mkdir -p ${sixteen_queens_solution_dir}
mkdir -p ${thirty_two_queens_solution_dir}

run_eightqueens=true

# Eight Queens

$solve nqueens hill_climbing \
-i ${states_dir}/eightqueens.csv -o ${eight_queens_solution_dir}/hill_climbing.csv \
-pa '{"dimension": 8}'

$solve nqueens hill_climbing_sideways \
-i ${states_dir}/eightqueens.csv -o ${eight_queens_solution_dir}/hill_climbing_sideways_100.csv \
-pa '{"dimension": 8}' \
-aa '{"max_sideways_moves": 100}'

$solve nqueens hill_climbing_random_restart \
-i ${states_dir}/eightqueens.csv -o ${eight_queens_solution_dir}/hill_climbing_random_restart_exhaustive.csv \
-pa '{"dimension": 8}' \
-aa '{"exhaustive": 1}'


# Sixteen Queens

$solve nqueens hill_climbing \
-i ${states_dir}/sixteenqueens.csv -o ${sixteen_queens_solution_dir}/hill_climbing.csv \
-pa '{"dimension": 16}'

$solve nqueens hill_climbing_sideways \
-i ${states_dir}/sixteenqueens.csv -o ${sixteen_queens_solution_dir}/hill_climbing_sideways_100.csv \
-pa '{"dimension": 16}' \
-aa '{"max_sideways_moves": 100}'

$solve nqueens hill_climbing_random_restart \
-i ${states_dir}/sixteenqueens.csv -o ${sixteen_queens_solution_dir}/hill_climbing_random_restart_exhaustive.csv \
-pa '{"dimension": 16}' \
-aa '{"exhaustive": 1}'

# Thirty-two Queens

$solve nqueens hill_climbing \
-i ${states_dir}/thirtytwoqueens.csv -o ${thirty_two_queens_solution_dir}/hill_climbing.csv \
-pa '{"dimension": 32}'

$solve nqueens hill_climbing_sideways \
-i ${states_dir}/thirtytwoqueens.csv -o ${thirty_two_queens_solution_dir}/hill_climbing_sideways_100.csv \
-pa '{"dimension": 32}' \
-aa '{"max_sideways_moves": 100}'

$solve nqueens hill_climbing_random_restart \
-i ${states_dir}/thirtytwoqueens.csv -o ${thirty_two_queens_solution_dir}/hill_climbing_random_restart_exhaustive.csv \
-pa '{"dimension": 32}' \
-aa '{"exhaustive": 0, "time_limit": 60}'


# Knapsack

knapsack_solution_dir="${solution_dir}/knapsack"
mkdir -p ${knapsack_solution_dir}/easy_10_269

$solve knapsack hill_climbing \
-i ${states_dir}/knapsack_easy_10_269.csv -o ${knapsack_solution_dir}/easy_10_269/hill_climbing.csv \
-pa '{"path": "experiments/knapskack/instances/easy/f1_l-d_kp_10_269"}'

$solve knapsack hill_climbing_sideways \
-i ${states_dir}/knapsack_easy_10_269.csv -o ${knapsack_solution_dir}/easy_10_269/hill_climbing_sideways_25.csv \
-pa '{"path": "experiments/knapskack/instances/easy/f1_l-d_kp_10_269"}' \
-aa '{"max_sideways_moves": 25}'

$solve knapsack hill_climbing_random_restart \
-i ${states_dir}/knapsack_easy_10_269.csv -o ${knapsack_solution_dir}/easy_10_269/hill_climbing_random_restart.csv \
-pa '{"path": "experiments/knapskack/instances/easy/f1_l-d_kp_10_269"}' \
-aa '{"exhaustive": 0, "time_limit": 2}'