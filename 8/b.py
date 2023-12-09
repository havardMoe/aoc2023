import re
from functools import reduce
import math

def generate_maps(nodes):
    m = {}
    for node in nodes:
        start, left, right = node
        m[start] = (left, right)
    return m

def go_left(d, key):
    return d[key][0]


def go_right(d, key):
    return d[key][1]


if __name__ == '__main__':

    with open('8/input.txt') as f:
        inp = f.read()

    directions_pattern = r'^([LR]+)'
    direction = [c for c in re.search(directions_pattern, inp).group(1)]

    node_pattern = r'\n([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)'
    nodes = re.findall(node_pattern, inp)
    maps = generate_maps(nodes)

    start_node_pattern = r'\n([A-Z]{2}A) ='
    start_nodes = re.findall(start_node_pattern, inp)

    end_nodes_pattern = r'\n([A-Z]{2}Z) ='
    end_nodes = set(re.findall(end_nodes_pattern, inp))

    time_of_visit = []
    for node in start_nodes:
        i = 0
        steps = 0
        n = len(direction)

        visits = []
        while node not in end_nodes:  
            d = direction[i % n]
            node = go_left(maps, node) if d == 'L' else go_right(maps, node)
            
            steps += 1
            i += 1
            
        time_of_visit.append(steps)

    # lcm across the set of numbers
    lcmm = reduce(math.lcm, time_of_visit)
    print(lcmm)
    

    