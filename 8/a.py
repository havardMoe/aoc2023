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

    steps = 0

    # start node
    node = nodes[0][0]

    i = 0
    n = len(direction)
    while True:
        if node == 'ZZZ':
            break
        else:
            steps += 1
        
        d = direction[i % n]

        if d == 'L':
            node = go_left(maps, node)
        elif d == 'R':
            node = go_right(maps, node)

    print(node)
    print(f'steps: {steps}')


    