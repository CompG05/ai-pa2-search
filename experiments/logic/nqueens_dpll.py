from aima.utils import Expr
from logic.nqueens import get_nqueens_model


def main():
    dimension = 8
    result = get_nqueens_model(dimension)
    print(result)
    print()
    for i in range(dimension):
        for j in range(dimension):
            if result[i] == j:
                print("* ", end='')
            else:
                print(". ", end='')
        print()


if __name__ == "__main__":
    main()
