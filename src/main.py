import gen_maze
import cars.random_car as rc
import cars.q_uber as qu
import sys


if __name__ == "__main__":
    start = int(sys.argv[1])
    finish = int(sys.argv[2])
    arg = int(sys.argv[3])
    if arg == 0:
        load_maze = False
    else:
        load_maze = True

    print(load_maze)
    maze = gen_maze.Maze(start,finish, load_maze)
    rand_car = rc.Random_car(maze.adj,maze.graph,start,finish)
    q_uber = qu.Q_uber(maze.adj,maze.graph,start,finish)
    #rand_car.solve_maze()
    #print("Car went through maze in", len(rand_car.visited_vert),"moves")
    print(q_uber.Q)