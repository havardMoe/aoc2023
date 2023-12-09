import re


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


    i = 0
    steps = 0
    n = len(direction)

    node = 'AAA'
    while node != 'ZZZ':
    
        steps += 1
        
        d = direction[i % n]
        node = go_left(maps, node) if d == 'L' else go_right(maps, node)

        i += 1

    print(steps)


    