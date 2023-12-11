import re
import numpy as np
from itertools import combinations

def expand_coordinates(space, coordinates, n=999_999):
    y, x = coordinates

    # modify the rows
    dy = np.zeros(len(x))
    for i in range(space.shape[0]):
        if np.all(space[i] == 0):
            dy = np.where(y > i, dy + n, dy)
    
    # modify the columns
    dx = np.zeros(len(y))
    for i in range(space.shape[1]):
        if np.all(space[:,i] == 0):
            dx = np.where(x > i, dx + n, dx)
    
    
    coordinates = [(a, b) for a, b in zip(y + dy, x + dx)]
    return coordinates


if __name__ == '__main__':
    with open('11/input.txt') as f:
        lines = np.array([[c for c in l.strip()] for l in f.readlines()])
    
    # 1s are gallaxies and 0s are empty space
    space = np.where(lines == '#', 1, 0)

    galaxy_coordinates = np.nonzero(space)
    expanded_coordinates = expand_coordinates(space, galaxy_coordinates, n=999_999)
    coordinate_combinations = combinations(expanded_coordinates, r=2)
    distances = [np.abs(np.array(pair[0]) - np.array(pair[1])).sum() for pair in coordinate_combinations]

    print(int(sum(distances)))