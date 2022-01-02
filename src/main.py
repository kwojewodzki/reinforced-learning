import gen_maze
import cars.random_car as rc
import cars.q_uber as qu
import sys


if __name__ == "__main__":
    start = int(sys.argv[1]) - 1
    finish = int(sys.argv[2]) - 1

    maze = gen_maze.Maze(start,finish)