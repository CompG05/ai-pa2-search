import time
import signal

from aima.logic import dpll_select
from logic.nqueens import to_expr

TIME_LIMIT = 5 * 60
filename = "nqueens_dpll_select_report.txt"
errors = []


def main(dimension, et, ps, uc):
    e = to_expr(dimension)

    def handler(_, __):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, handler)

    if (et, ps, uc) not in errors:
        signal.alarm(TIME_LIMIT)
        try:
            btime = time.time()
            model, partial_count, total_count = dpll_select(e, et, ps, uc)
            atime = time.time()
            with open(filename, "a") as f:
                f.write(f"{et}\t\t{ps}\t\t{uc}\t\t{partial_count}\t\t{total_count}\t\t%.2f\t\t{model is not False}\n" % (
                    atime - btime))
        except TimeoutError:
            with open(filename, "a") as f:
                f.write(f"{et}\t\t{ps}\t\t{uc}\t\t \t\t \t\t{5 * 60}\t\tTIMEOUT\n")
            errors.append((et, ps, uc))
        except RecursionError:
            with open(filename, "a") as f:
                f.write(f"{et}\t\t{ps}\t\t{uc}\t\t \t\t \t\t{5 * 60}\t\tRECURSION EXCEEDED\n")
            errors.append((et, ps, uc))



if __name__ == "__main__":
    params = [
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, True),
        (False, False, False)
    ]

    open(filename, "w").close()
    for i in [4, 6, 8, 12, 16, 24, 32]:
        with open(filename, "a") as f:
            f.write(f"Dimension: {i}\n")
            f.write("et\t\tps\t\tuc\t\tpc\t\ttc\t\ttime\t\tfound\n")
        for param in params:
            main(i, *param)
        with open(filename, "a") as f:
            f.write("\n")
