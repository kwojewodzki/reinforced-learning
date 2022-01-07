import random as rand
import numpy as np

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
    Q = [[0,0,0,0]for i in range(64)]

    def set_P_val(self, state, next_state, action):
        if next_state == -1 or self.graph[next_state][1] < -1:
            self.P[state][action].append(state)
            self.P[state][action].append(-10)
            self.P[state][action].append(False)
        else:
            self.P[state][action].append(next_state)
            self.P[state][action].append(-1)
            self.P[state][action].append(False)

            if state == self.finish:
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

    def throw_dice(self):
        num = rand.randint(0,3)
        return num

    def move(self,state,action):
        next_action = self.P[state][action][0]
        reward = self.P[state][action][1]
        done = self.P[state][action][2]
        return next_action,reward,done

    def train(self):
        for i in range(1,1000):
            state = self.reset_position()
            done = False
            while not done:
                if rand.uniform(0,1) < 0.1:
                    action = self.throw_dice()
                else:
                    action = np.argmax(self.Q[state])  

                next_state,reward,done = self.move(state,action)

                old_val = self.Q[state][action]
                next_max = np.max(self.Q[next_state])

                new_val = ((1 - self.alpha) * old_val) + (self.alpha * (reward + (self.gamma * next_max)))
                self.Q[state][action] = new_val
                state = next_state
            
        print("Finished training")

    def reset_position(self):
        return self.start

    def solve_maze(self):
        state = self.reset_position()
        done = False
        path = []
        while not done:
            path.append(state)
            action = np.argmax(self.Q[state])  

            next_state,reward,done = self.move(state,action)
            state = next_state

        print("walked through maze")
        print(path)
            
