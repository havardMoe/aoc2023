import re
import numpy as np

if __name__ == '__main__':
    with open('11/input.txt') as f:
        lines = np.array([l.strip() for l in f.readlines()])
    
    print(lines)
    m = np.where(lines == '#', 1, 0)
    print(m)