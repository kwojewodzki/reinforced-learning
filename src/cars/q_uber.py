import numpy.random as rand

#actions: 
# 0 - up
# 1 - down
# 2 - right
# 3 - left

class Q_uber:
    visited_vert = []
    P = [[[],[],[],[]]for i in range(64)]
    epsilon = 0.1

    def set_P_val(self, state, action):
        self.P[state][action].append(state)
        self.P[state][action].append(self.graph[state][1])
        if state == self.finish:
            self.P[state][action].append(True)
            self.P[state][action][1] = 10

    def init_P(self):
        for i in range(64): #state
            for j in range(4): #possible action
                if j == 0:
                    for k in self.adj[i]:
                        if k == i + 8:
                            self.set_P_val(i,j)

    def __init__(self,adj,graph,start,finish):

        self.graph = graph
        self.adj = adj
        self.start = start
        self.finish = finish
        self.init_P()

    def reset_position(self):
        return self.start

    def solve_maze(self):
        curr_position = self.start

        while curr_position != self.finish:
            pass
            
