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

    def set_P_val(self, state, next_state, action):
        self.P[state][action].append(next_state)
        self.P[state][action].append(self.graph[state][1])
        if next_state == self.finish:
            self.P[state][action].append(True)
            self.P[state][action][1] = 10
        else:
            self.P[state][action].append(False)

    def init_P(self):
        for i in range(64): #state
            for j in self.adj[i]: #possible action
                if j == i + 8:
                    self.set_P_val(i,j,0)
                elif j == i - 8:
                    self.set_P_val(i,j,1)
                elif j == i + 1:
                    self.set_P_val(i,j,2)
                elif j == i - 1:
                    self.set_P_val(i,j,3)

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
            
