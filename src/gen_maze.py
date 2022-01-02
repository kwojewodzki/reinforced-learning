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

    def __init__(self,start,finish):
        
        self.start = start
        self.finish = finish

        print("Generating maze...")
        self.make_graph()

        self.add_obstacles()
        if not self.isReachable(self.start, self.finish):
            while not self.isReachable(self.start, self.finish):
                self.graph = []
                self.add_obstacles()
        

    def isReachable(self,s, d):
     
    # Base case
        if (s == d):
            return True
    
        # Mark all the vertices as not visited
        visited = [False for i in range(size_of_wall**2)]
        for i in range(len(self.graph)):
            pass
            if self.graph[i][1] < 0:
                visited[i] = True
    
        # Create a queue for BFS
        queue = deque()
    
        # Mark the current node as visited and enqueue it
        visited[s] = True
        queue.append(s)
    
        while (len(queue) > 0):
        
            # Dequeue a vertex from queue and print
            s = queue.popleft()
            # queue.pop_front()
    
            # Get all adjacent vertices of the dequeued vertex s
            # If a adjacent has not been visited, then mark it
            # visited  and enqueue it
            for i in self.adj[s]:
                # If this adjacent node is the destination node,
                # then return true
                if (i == d):
                    return True
    
                # Else, continue to do BFS
                if (not visited[i]):
                    visited[i] = True
                    queue.append(i)
        # If BFS is complete without visiting d
        return False        


def main():
    
    maze = Maze()
    