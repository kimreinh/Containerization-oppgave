import random

def hill_climber(graph):
    """
    Starts with a naive Hamiltonian circuit,
    then optimizes the summed weight of the circuit
    with a hill climber algorithm. Two nodes in
    a circuit are swapped to generate a neighboring
    solution that is stored if it is a better solution.
    After a number of iterations the solution will
    improve as it approaches a local optima that may
    or may not be the global optimum.

    args: graph in the format given in graph_util.py

    return: list with two items
            list[0]: list representation of circuit
            list[1]: summed weights of circuit
    """
    best_path = list(range(graph.size))
    best_distance = compute_distance(graph, best_path)

    iterations = 50
    while iterations > 0:
        new_path = best_path.copy()
        random_swap(new_path)
        new_distance = compute_distance(graph, new_path)
        if new_distance < best_distance:
            best_distance = new_distance
            best_path = new_path
        iterations += -1
    
    return best_path, best_distance

# Swaps a pair of elements in a given list at random.
# Used by the hill climber algorithm.
def random_swap(list):
    idx = range(len(list))
    i1, i2 = random.sample(idx, 2)
    list[i1], list[i2] = list[i2], list[i1]

# Returns summed weights of given circuit in a graph.
# Used by hill climber algorithm.
def compute_distance(graph, path):
    distance = 0
    for i in range(len(path) -1):
        distance += graph.adjMatrix[path[i]][path[i+1]]
    distance += graph.adjMatrix[path[-1]][path[0]]
    return distance
