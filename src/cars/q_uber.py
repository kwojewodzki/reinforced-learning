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
    alpha = 0.1
    gamma = 0.6
    Q = [[[0],[0],[0],[0]]for i in range(64)]

    def set_P_val(self, state, next_state, action):
        if next_state == -1 or self.graph[next_state][1] < -1:
            self.P[state][action].append(state)
            self.P[state][action].append(-10)
            self.P[state][action].append(False)
        else:
            self.P[state][action].append(next_state)
            self.P[state][action].append(-1)
            self.P[state][action].append(False)

            if next_state == self.finish:
                self.P[state][action][1] = 10
                self.P[state][action][2] = True
            
    def init_P(self):
        for i in range(64): #state
            for j in range(len(self.adj[i])): #possible action
                self.set_P_val(i,self.adj[i][j], j) 

    def __init__(self,adj,graph,start,finish):

        self.graph = graph
        self.adj = adj
        self.start = start
        self.finish = finish
        self.init_P()

    def train(self):
        pass

    def reset_position(self):
        return self.start

    def solve_maze(self):
        curr_position = self.start

        while curr_position != self.finish:
            pass
            
