import re
from collections import defaultdict

def calc_mapping(i, source_start, dest_start):
    return dest_start + (i - source_start)

def solve(seeds, mappings, order):
    for seed in seeds:

        val = seed

        for source_dest in order:
            src_dest_map = mappings[source_dest]
            print(f'mapping {source_dest[0]} -> {source_dest[1]}')
            for source_range, src_dest_map_func in src_dest_map.items():

                if source_range[0] <= val <= source_range[1]:
                    print(f'value: {val} is in range: {source_range}')

                    val = src_dest_map_func(val)
                    print(val)
                    continue                    
        break

if __name__ == '__main__':
    with open('5/input.txt') as f:
        inp = f.read()

    maps_p = r'([a-zA-Z]+)-to-([a-zA-Z]+) map:\n([\d \n]+)'
    maps = re.findall(maps_p, inp)

    mappings = {}
    for m in maps:
        src, dest, numbers = m

        src_dest_mapping = {}

        for row in numbers.strip().split('\n'):
            dest_start, src_start, n = row.strip().split(' ')

            dest_start = int(dest_start)
            source_start = int(src_start)
            source_end = source_start + int(n) - 1

            range_function = lambda i: calc_mapping(i, source_start, source_end)

            src_dest_mapping[(source_start, source_end)] = range_function

        mappings[(src, dest)] = src_dest_mapping

    order = [
        ('seed', 'soil'),
        ('soil', 'fertilizer'),
        ('fertilizer', 'water'),
        ('water', 'light'),
        ('light', 'temperature'),
        ('temperature', 'humidity'),
        ('humidity', 'location'),
    ]

    # Seeds to to start with
    seeds_p = r'^seeds:\s*([\s\d]+)'
    seeds = [int(n) for n in re.search(seeds_p, inp).group(1).strip().split(' ')]

    solve(seeds, mappings, order)

    # print(mappings[('seed', 'soil')][(50, 97)](50))