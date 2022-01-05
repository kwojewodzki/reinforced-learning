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
        next_vert = self.adj[curr_vert][dice_throw]
        self.visited_vert.append(next_vert)
        return next_vert

    def solve_maze(self):
        self.visited_vert = []
        self.visited_vert.append(self.start)
        curr_vert = self.start
        next_vert = 0
        crashed = False
        iterations = 0

        while curr_vert != self.finish:
            iterations += 1
            next_vert = self.random_move(curr_vert)
            curr_vert = next_vert
                
