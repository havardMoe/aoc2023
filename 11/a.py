import re
import numpy as np
from itertools import combinations

def fill_empty_space(space):
    for _ in range(2):
        new_space = []
        for i in range(space.shape[0]):
            if np.all(space[i] == 0):
                new_space.append(space[i])
            new_space.append(space[i])
        space = np.array(new_space).T
    return space
    

if __name__ == '__main__':
    with open('11/input.txt') as f:
        lines = np.array([[c for c in l.strip()] for l in f.readlines()])
    
    # 1s are gallaxies and 0s are empty space
    space = np.where(lines == '#', 1, 0)
    space = fill_empty_space(space)
    galaxy_coordinates = [(x, y) for x, y in zip(*np.nonzero(space))]
    coordinate_combinations = combinations(galaxy_coordinates, r=2)
    distances = [np.abs(np.array(pair[0]) - np.array(pair[1])).sum() for pair in coordinate_combinations]

    print(sum(distances))