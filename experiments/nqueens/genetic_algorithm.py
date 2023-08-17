from algorithms.local.genetic import GeneticSearch
from constants import INVERSE_N_CONFLICTS_FITNESS
from heuristics.nqueens import NQueensHeuristic
from problems.nqueens import NQueensProblem


def main(dimension, num_generations_list, sol_per_pop_list, selection_method_list, elitism_list):
    iterations = 100
    dimension = 8
    problem = NQueensProblem(dimension=dimension)
    fitness = NQueensHeuristic().create(INVERSE_N_CONFLICTS_FITNESS)
    num_genes = dimension
    for num_generations in num_generations_list:
        for sol_per_pop in sol_per_pop_list:
            for selection_method in selection_method_list:
                for elitism in elitism_list:
                    solutions = 0

                    for _ in range(iterations):
                        algorithm = GeneticSearch(
                            num_generations=num_generations,
                            num_parents_mating=2,
                            fitness_func=fitness,
                            num_genes=num_genes,
                            sol_per_pop=sol_per_pop,
                            gene_type=int,
                            mutation_percent_genes=1 * 100 / num_genes,
                            gene_space=list(range(0, dimension)),
                            parent_selection_type=selection_method,
                            keep_elitism=elitism,
                        )
                        best_node = algorithm.search(problem)
                        # print(fitness[INVERSE_N_CONFLICTS](None, list(best_node.state.data), None))
                        if best_node.state.is_goal():
                            solutions += 1

                    print(f"ng: {num_generations}, spp: {sol_per_pop}, sm: {selection_method}, e: {elitism}\n"
                          f"\tsolution rate: {solutions / iterations}\n")


if __name__ == "__main__":
    eight_num_generations_list = [200]
    eight_sol_per_pop_list = [200]
    eight_selection_method_list = ["rank", "tournament"]
    eight_elitism_list = [30, 60]

    sixteen_num_generations_list = [300]
    sixteen_sol_per_pop_list = [300]
    sixteen_selection_method_list = ["rank", "tournament"]
    sixteen_elitism_list = [30, 60]

    #main(8, eight_num_generations_list, eight_sol_per_pop_list, eight_selection_method_list, eight_elitism_list)

    main(16, sixteen_num_generations_list, sixteen_sol_per_pop_list, sixteen_selection_method_list, sixteen_elitism_list)
