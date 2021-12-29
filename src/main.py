import gen_maze
import sys


if __name__ == "__main__":
    start = int(sys.argv[1]) - 1
    finish = int(sys.argv[2]) - 1

    maze = gen_maze.Maze(start,finish)
    print(maze.isReachable(start,finish))