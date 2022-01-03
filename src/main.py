import gen_maze
import cars.random_car as rc
import cars.q_uber as qu
import sys


if __name__ == "__main__":
    start = int(sys.argv[1])
    finish = int(sys.argv[2])
    load_maze = not bool(sys.argv[3])

    maze = gen_maze.Maze(start,finish, load_maze)
    rand_car = rc.Random_car(maze.adj,maze.graph,start,finish)
    crashed = True
    i = 0
    while crashed:
        crashed = rand_car.solve_maze()
        i+=1
    print("Solved in", i, "iterations")
    print("Car went through maze in", len(rand_car.visited_vert),"moves")
