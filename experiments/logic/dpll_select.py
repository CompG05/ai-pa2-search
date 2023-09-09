import time
import signal
import sys

from aima.logic import dpll_select
from logic.graph_coloring import graph_to_expr
from logic.nqueens import to_expr
from structures.graph import UndirectedGraph

TIME_LIMIT = 5 * 60
errors = []


def handler(_, __):
    raise TimeoutError()


def main(e, filename, discard_timeouts, et, ps, uc):
    signal.signal(signal.SIGALRM, handler)

    if not discard_timeouts or (et, ps, uc) not in errors:
        signal.alarm(TIME_LIMIT)
        try:
            btime = time.time()
            model, partial_count, total_count = dpll_select(e, et, ps, uc)
            atime = time.time()
            with open(filename, "a") as f:
                f.write(
                    f"{et}\t\t{ps}\t\t{uc}\t\t{partial_count}\t\t{total_count}\t\t%.2f\t\t{model is not False}\n" % (
                            atime - btime))
        except TimeoutError:
            with open(filename, "a") as f:
                f.write(f"{et}\t\t{ps}\t\t{uc}\t\t \t\t \t\t{5 * 60}\t\tTIMEOUT\n")
            errors.append((et, ps, uc))
        except RecursionError:
            with open(filename, "a") as f:
                f.write(f"{et}\t\t{ps}\t\t{uc}\t\t \t\t \t\t{5 * 60}\t\tRECURSION EXCEEDED\n")
            errors.append((et, ps, uc))


def main_wrapper(e, title, filename, discard_timeouts):
    params = [
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (True, False, False),
        # (False, True, False),
        (False, False, True),
        # (False, False, False)
    ]

    with open(filename, "a") as f:
        f.write(title + "\n")
        f.write("et\t\tps\t\tuc\t\tpc\t\ttc\t\ttime\t\tfound\n")
    for param in params:
        main(e, filename, *param, discard_timeouts)
    with open(filename, "a") as f:
        f.write("\n")


if __name__ == "__main__":
    problem = sys.argv[1]
    nqueens_filename = "nqueens_dpll_select.txt"
    romania_filename = "romania_dpll_select.txt"
    argentina_filename = "argentina_dpll_select.txt"

    argentina_map = UndirectedGraph({
        "Buenos Aires": {
            "Rosario": 300,
            "Cordoba": 700,
            "Mendoza": 1000,
            "Mar del Plata": 400,
            "San Juan": 1100,
            "Salta": 1500,
            "Bahia Blanca": 650,
            "Neuquen": 1200,
            "La Plata": 60,
            "Tucuman": 1600,
            "Santa Rosa": 600,
        },
        "Rosario": {
            "Cordoba": 400,
            "Santa Fe": 150,
            "Parana": 380,
        },
        "Cordoba": {
            "Mendoza": 700,
            "San Juan": 900,
            "La Rioja": 800,
            "Santa Fe": 300,
        },
        "Mendoza": {
            "San Juan": 160,
            "La Rioja": 600,
            "San Luis": 350,
        },
        "Mar del Plata": {
            "Bahia Blanca": 400,
        },
        "Salta": {
            "Jujuy": 150,
        },
        "Bahia Blanca": {
            "Neuquen": 700,
        },
        "Neuquen": {
            "Bariloche": 400,
            "San Martin de los Andes": 400,
        },
        "Tucuman": {
            "Santiago del Estero": 200,
        },
        "Santa Rosa": {
            "La Pampa": 100,
        },
        "La Rioja": {
            "San Martin de los Andes": 400,
        },
        "Parana": {
            "Resistencia": 450,
        },
        "Santa Fe": {
            "Santiago del Estero": 500,
        },
        "San Martin de los Andes": {
            "Bariloche": 250,
        },
        "La Pampa": {
            "General Pico": 150,
        },
        "Resistencia": {
            "Corrientes": 300,
        },
        "Corrientes": {
            "Posadas": 350,
        },
    })

    romania_map = UndirectedGraph(
        dict(
            Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
            Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
            Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
            Drobeta=dict(Mehadia=75),
            Eforie=dict(Hirsova=86),
            Fagaras=dict(Sibiu=99),
            Hirsova=dict(Urziceni=98),
            Iasi=dict(Vaslui=92, Neamt=87),
            Lugoj=dict(Timisoara=111, Mehadia=70),
            Oradea=dict(Zerind=71, Sibiu=151),
            Pitesti=dict(Rimnicu=97),
            Rimnicu=dict(Sibiu=80),
            Urziceni=dict(Vaslui=142),
        )
    )

    if problem == "nqueens":
        open(nqueens_filename, "w").close()
        for i in [4, 6, 8, 12, 16, 24, 32]:
            nqueens_expr = to_expr(i)
            title = f"Dimension: {i}"
            main_wrapper(nqueens_expr, title, nqueens_filename, True)

    if problem == "romania":
        open(romania_filename, "w").close()
        for i in [2, 3, 4, 5]:
            expr = graph_to_expr(romania_map, i)
            title = f"Colors: {i}"
            main_wrapper(expr, title, romania_filename, False)

    if problem == "argentina":
        open(argentina_filename, "w").close()
        for i in [2, 3, 4, 5]:
            expr = graph_to_expr(argentina_map, i)
            title = f"Colors: {i}"
            main_wrapper(expr, title, argentina_filename, False)
