import numpy.random as rand

class Q_uber:
    visited_vert = []

    def __init__(self,adj,graph,start,finish):

        self.graph = graph
        self.adj = adj
        self.start = start
        self.finish = finish

    def solve_maze(self):
        pass