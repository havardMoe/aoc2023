from enum import Enum
import numpy as np
from copy import deepcopy
import sys

sys.setrecursionlimit(20000) 

class DIRECTION(Enum):
    UP = 1
    DOWN = -1
    RIGHT = 2
    LEFT = -2

# Symbols valid when looking for an neighbour in the different directions
VALID_UPWARD_SYMBOLS = {'7', 'F', '|'}
VALID_DOWNWARD_SYMBOLS = {'J', 'L', '|'}

VALID_RIGHT_SYMBOLS = {'7', 'J', '-'}
VALID_LEFT_SYMBOLS = {'F', 'L', '-'}

def find_start(maze):
    for i, row in enumerate(maze):
        j = row.find('S')
        if j != -1:
            return (i, j)
    raise ValueError('No start in maze')

def get_valid_neighbours(maze, visits, idx):
    valid_neighbours = []
    for d in DIRECTION:
        valid, coord = get_valid_neighbour(maze, visits, idx, d)
        if valid:
            valid_neighbours.append(coord)

    return valid_neighbours

def char_allows_direction(char, d):
    if char == 'S':
        return True
    elif char == '7':
        if d in {DIRECTION.LEFT, DIRECTION.DOWN}:
            return True
    elif char == 'F':
        if d in {DIRECTION.DOWN, DIRECTION.RIGHT}:
            return True
    elif char == '|':
        if d in {DIRECTION.UP, DIRECTION.DOWN}:
            return True
    elif char == 'J':
        if d in {DIRECTION.LEFT, DIRECTION.UP}:
            return True
    elif char == 'L':
        if d in {DIRECTION.UP, DIRECTION.RIGHT}:
            return True
    elif char == '-':
        if d in {DIRECTION.LEFT, DIRECTION.RIGHT}:
            return True
    else:
        raise ValueError('wrong char')
    return False

def get_valid_neighbour(maze: list[str], visits: list[bool], idx: list[int], d):
    i, j = idx
    char = maze[idx[0]][idx[1]]
    valid_direction = char_allows_direction(char, d)
    if d == DIRECTION.UP:
        # Check if we are not at the top of the maze
        valid = (i > 0)
        c = (i-1, j)
        valid_symbols = VALID_UPWARD_SYMBOLS
    elif d == DIRECTION.DOWN:
        # Check if we are not at the bottom of the maze
        valid = (i < len(maze)-1)
        c = (i+1, j)
        valid_symbols = VALID_DOWNWARD_SYMBOLS
    elif d == DIRECTION.RIGHT:
        # Check if we are not at the rightmost edge of the maze
        valid = (j < len(maze[0])-1)
        c = (i, j+1)
        valid_symbols = VALID_RIGHT_SYMBOLS
    elif d == DIRECTION.LEFT:
        # Check if we are not at the leftmost edge of the maze
        valid = (j > 0)
        c = (i, j-1)
        valid_symbols = VALID_LEFT_SYMBOLS
    else:
        raise ValueError('Wrong direction input')
    if c == (2, 5) and d == DIRECTION.LEFT:
        1 == 1
    # coordinate is not out of bounds
    # is a valid neighbouring symbol
    # is not visited before
    if (valid and maze[c[0]][c[1]] in valid_symbols 
              and valid_direction and not visits[c[0]][c[1]]): 
        return True, c

    return False, None


def traverse_maze(loc, maze, visits, distances, steps=-1, root=False):
    steps += 1

    # set distance if it is lower than prev distance at location
    if distances[loc[0]][loc[1]] > steps:
        distances[loc[0]][loc[1]] = steps
    # Update visits matrix
    visits[loc[0]][loc[1]] = True
    # check for valid neighbours
    neighbours = get_valid_neighbours(maze, visits, loc)

    if loc == (78, 75):
        1 == 1

    if root:
        # there should be 2 neighbours
        neigh1 = neighbours[0]
        neigh2 = neighbours[1]
        visits1 = deepcopy(visits)
        visits2 = deepcopy(visits)
        distances1 = deepcopy(distances)
        distances2 = deepcopy(distances)
        traverse_maze(neigh1, maze, visits1, distances1, steps)
        traverse_maze(neigh2, maze, visits2, distances2, steps)
        return distances1, distances2

    # for each valid neighbour, call funciton recursively
    elif len(neighbours) == 0:
        return
    # is 1 neighbours when starting at the start location
    elif len(neighbours) == 1:
        neigh = neighbours[0]
        traverse_maze(neigh, maze, visits, distances, steps)
    else:
        print(len(neighbours))
        raise ValueError(' there are too many neighbours ')

def draw_pipes(inp):
    s = find_start(inp)
    
    visits = [[False for c in r] for r in inp]
    distances = [[np.inf for c in r] for r in inp]
    distances1, distances2 = traverse_maze(
        loc=s,
        maze=inp,
        visits=visits,
        distances=distances,
        root=True
    )

    pipes = []
    for r1, r2 in zip(distances1, distances2):
        pipe_row = ['X' if (d1 * d2 < np.inf) else '.' for (d1, d2) in zip(r1, r2)]
        pipes.append(pipe_row)
    
    return pipes

def fill_outward(loc, pipes):
    valid_neighbours = []
def fill_pipes(pipes, c):
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == '.':
                fill_outward((i, j), pipes, c)



if __name__ == '__main__':
    with open('10/input.txt') as f:
        inp = [line.strip() for line in f]

    pipes = draw_pipes(inp)

    for r in pipes:
        print(r)