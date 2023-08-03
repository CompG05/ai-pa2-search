import argparse
import csv
import json

from constants import *
from solver.solution import Solution
from solver.solver import Solver

N_STATES = 50


def main():
    parser = argparse.ArgumentParser(prog='solve.py', description='Solve a problem using some search algorithm.')
    parser.add_argument('problem', metavar='problem', choices=problems.keys(), help='problem to solve')
    parser.add_argument('algorithm', metavar='algorithm', choices=algorithms.keys(), help='search algorithm to use')
    parser.add_argument('--heuristic', help='heuristic to use')
    parser.add_argument('--problem-args', '-pa', help='problem arguments in json format')
    parser.add_argument('--algorithm-args', '-aa', help='algorithm arguments in json format')
    parser.add_argument('--input', '-i', help='input file containing states')
    parser.add_argument('--output', '-o', help='output file', default='report.csv')
    args = parser.parse_args()
    problem_args = json.loads(args.problem_args) if args.problem_args else {}
    algorithm_args = json.loads(args.algorithm_args) if args.algorithm_args else {}

    with open(args.input, 'r') as inp:
        initial_states = read_initial_states(args.problem, inp)
        with open(args.output, 'w') as out:
            out.write(Solution.csv_header() + '\n')

    for state in initial_states:
        problem_args['initial_state'] = state
        solver = Solver(args.problem, args.algorithm, args.heuristic, problem_args, algorithm_args)
        solution = solver.solve()
        write_solution(solution, args.output)


def read_initial_states(problem, input_file):
    reader = csv.reader(input_file, delimiter=',')
    initial_states = []
    for row in reader:
        if problem == NQUEENS:
            initial_states.append(tuple(map(int, row)))
        elif problem == KNAPSACK:
            initial_states.append(list(map(bool, row)))

    return initial_states


def write_solution(solution, output_file):
    with open(output_file, 'a') as csvfile:
        csvfile.write(solution.to_csv() + '\n')


if __name__ == '__main__':
    main()
