import numpy.random as rand
from collections import deque

size_of_wall = 8


class Maze:

    adj = [[]for i in range(size_of_wall**2)]
    graph = []

    def make_graph(self):
        for i in range(size_of_wall**2):
            j = i+1
            if j-size_of_wall > 0: #Check if is node below
                self.adj[i].append(i-size_of_wall)      

            if j%size_of_wall != 1:#Check if is node on left
                self.adj[i].append(i-1)   

            if j%size_of_wall != 0:#Check if is node on right
                self.adj[i].append(i+1)

            if j+size_of_wall < size_of_wall**2:#Check if is node above
                self.adj[i].append(i+size_of_wall)

    def add_obstacles(self):
        for i in range(size_of_wall**2):
            if i == self.start or i == self.finish:
                self.graph.append([i,1])
            elif rand.uniform(0, 1) < 0.35:
                self.graph.append([i, -5]) #obstacle
            else:
                self.graph.append([i,1]) #free space

    def load_maze(self):
        try:
            f= open("../data/maze.data", "r")
        except:
            print("Cannot open file with maze")
        else:
            print("Loading maze...")
            for line in f:
                num,val = line.partition(' ')[::2]
                self.graph.append([int(num),int(val)])

    def __init__(self,start,finish,gen_maze):
        
        self.start = start
        self.finish = finish

        self.make_graph()
        if not gen_maze:
           self.load_maze()
        else:
            print("Generating maze...")
            self.add_obstacles()
            if not self.isReachable(self.start, self.finish):
                while not self.isReachable(self.start, self.finish):
                    self.graph = []
                    self.add_obstacles()
        

    def isReachable(self,s, d):
     
        if (s == d):
            return True
    
        visited = [False for i in range(size_of_wall**2)]
        for i in range(len(self.graph)):
            pass
            if self.graph[i][1] < 0:
                visited[i] = True
    
        queue = deque()
    
        visited[s] = True
        queue.append(s)
    
        while (len(queue) > 0):
        
            s = queue.popleft()

            for i in self.adj[s]:

                if (i == d):
                    return True
    
                if (not visited[i]):
                    visited[i] = True
                    queue.append(i)
        return False        


def main():
    
    maze = Maze()
    