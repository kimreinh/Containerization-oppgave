from graph_util import *
from hill_climber import *

# Generates a complete undirected weighted graph
# with n nodes
n = 8
graph = Graph(n)
for i in range(graph.size):
    for j in range(graph.size):
        graph.add_edge(i, j)

# Treats a given graph with respect to the Traveling Salesman Problem.
def TSP(graph):
    print("Generated complete weighted graph with", n, "nodes")
    print("Adjacency matrix:")
    graph.print_graph()
    print()
    print("Traveling salesman problem naive solution:")
    print("Circuit:", list(range(graph.size)))
    print("Distance:", compute_distance(graph, range(graph.size)))
    print()
    print("Traveling salesman problem solution after optimization with hill climber algorithm:")
    solution = hill_climber(graph)
    print("Circuit:", solution[0])
    print("Distance:", solution[1])

TSP(graph)