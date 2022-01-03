import numpy.random as rand

#actions: 
# 0 - up
# 1 - down
# 2 - right
# 3 - left

class Q_uber:
    visited_vert = []
    states = [i for i in range(64)]
    P = [[[],[],[],[]]for i in range(64)]
    epsilon = 0.1

    def init_P(self):
        for i in len(self.adj):
            for j in range(4):
                if j == 0:
                    pass
                elif j == 1:
                    pass
                elif j == 2:
                    pass
                elif j == 3:
                    pass

    def __init__(self,adj,graph,start,finish):

        self.graph = graph
        self.adj = adj
        self.start = start
        self.finish = finish

    def reset_position(self):
        return self.start

    def solve_maze(self):
        curr_position = self.start

        while curr_position != self.finish:
            pass
            
