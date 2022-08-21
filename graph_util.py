import random

# Initializes a graph represented with an adjacency matrix.
class Graph():
    def __init__(self, size):
        self.size = size
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        
    def add_edge(self, n1, n2):
        """
        Instead of a binary edge|!edge representation,
        the relationship between the two nodes is assigned
        a random weight.

        args: n1 & n2 as pair of different nodes
        """
        if n1 != n2:
            weight = random.randint(1, 9)
            self.adjMatrix[n1][n2] = weight
            self.adjMatrix[n2][n1] = weight

    # Prints the adjacency matrix with formatting and labels
    def print_graph(self):
        s = " "
        for i in range(self.size):
            s = s + "  " + str(i)
        print(s)
        for i in range(self.size):
            print(i, self.adjMatrix[i])