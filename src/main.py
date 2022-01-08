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

    maze = gen_maze.Maze(start,finish, load_maze)
    rand_car = rc.Random_car(maze.adj,maze.graph,start,finish)
    q_uber = qu.Q_uber(maze.adj,maze.graph,start,finish)

    #for i in range(100):
    #    rand_car.solve_maze()
    for i in range(100):
        q_uber.train()
        q_uber.solve_maze()