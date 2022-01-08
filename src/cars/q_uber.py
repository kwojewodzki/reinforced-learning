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

    def save_result(self,penalties, steps,type):
        if type == "train":
            try:
                f1= open("../data/results/q_train_penalties.data", "a")
                f2= open("../data/results/q_train_steps.data", "a")
            except:
                print("Cannot open file with maze")
            else:
                f1.write(str(penalties) + '\n')
                f2.write(str(steps) + '\n')

                f1.close()
                f2.close()
        elif type == "solve":
            try:
                f1= open("../data/results/q_solve_penalties.data", "a")
                f2= open("../data/results/q_solve_steps.data", "a")
            except:
                print("Cannot open file with maze")
            else:
                f1.write(str(penalties) + '\n')
                f2.write(str(steps) + '\n')

                f1.close()
                f2.close()
        else:
            print("Something went wrong")

    def train(self):
        self.Q = [[0,0,0,0]for i in range(64)]
        penalties = 0
        steps_array = []
        for i in range(1,1001):
            state = self.reset_position()
            done = False
            steps = 0
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
                if reward == -10:
                    penalties += 1
                    steps += 10
                    break
                state = next_state
                steps += 1
            steps_array.append(steps)
        avg_steps = np.average(steps_array)
        self.save_result(penalties,avg_steps,"train")
            

    def reset_position(self):
        return self.start

    def solve_maze(self):
        
        penalties = 0
        steps = 0 
        state = self.reset_position()
        done = False
        path = []
        while not done:
            steps += 1
            path.append(state)
            action = np.argmax(self.Q[state])  

            next_state,reward,done = self.move(state,action)
            state = next_state
            if reward == -10:
                penalties += 1
                break
        self.save_result(penalties,steps,"solve")
        #print(path)
