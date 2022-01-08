import random as rand

class Random_car:
    visited_vert = []

    def throw_dice(self,max):
        num = rand.randint(0,max)
        return num

    def __init__(self,adj,graph,start,finish):

        self.graph = graph
        self.adj = adj
        self.start = start
        self.finish = finish

    def random_move(self,curr_vert):

        dice_throw = self.throw_dice(len(self.adj[curr_vert])-1)

        if self.adj[curr_vert][dice_throw] != -1:
            next_vert = self.adj[curr_vert][dice_throw]
        else:
            next_vert=curr_vert

        self.visited_vert.append(next_vert)
        return next_vert

    def save_result(self,iterations, visited):
        try:
            f1= open("../data/results/rand_iterations.data", "a")
            f2= open("../data/results/rand_steps.data", "a")
        except:
            print("Cannot open file with maze")
        else:
            f1.write(str(iterations) + '\n')
            f2.write(str(visited) + '\n')

            f1.close()
            f2.close()
            
    def solve_maze(self):
        next_vert = 0
        iterations = 0
        curr_vert = self.start
        iterations = 0

        while curr_vert != self.finish:
            iterations += 1
            self.visited_vert = []
            self.visited_vert.append(self.start)
            curr_vert = self.start
            while curr_vert != self.finish:
                next_vert = self.random_move(curr_vert)
                if self.graph[next_vert][1] == -10:
                    break
                curr_vert = next_vert
        self.save_result(iterations,len(self.visited_vert))
                
