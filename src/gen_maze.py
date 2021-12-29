size_of_wall = 8



class Maze:
    start = 20
    finish = 72
    graph_vertex = []
    graph = []

    def __init__(self):
        for i in range(size_of_wall**2):
            i+=1
            if i%size_of_wall != 0: 
                self.graph_vertex.append([i,i+1])
            if i+size_of_wall <= size_of_wall**2:
                self.graph_vertex.append([i,i+size_of_wall])

        print(len(self.graph))

def main():
    
    maze = Maze() 