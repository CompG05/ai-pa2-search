import argparse
import json

from constants import problems
from factories.problem_factory import problem_factory


def main():
    parser = argparse.ArgumentParser(description='generate states for a problem')
    parser.add_argument('problem', metavar='problem', help='problem to generate states for', choices=problems.keys())
    parser.add_argument('--output', '-o', help='output file')
    parser.add_argument('--problem-args', '-pa', help='problem arguments in json format')
    parser.add_argument('--number', '-n', help='number of states to generate', type=int, default=50)
    args = parser.parse_args()

    output = args.output or args.problem + '_states.csv'
    problem_args = json.loads(args.problem_args) if args.problem_args else {}

    problem, _ = problem_factory.create(args.problem, **problem_args)

    with open(output, 'w') as out:
        for i in range(args.number):
            state = problem.state_factory.random()
            out.write(state.to_csv() + '\n')


if __name__ == '__main__':
    main()