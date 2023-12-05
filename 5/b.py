import re
from collections import defaultdict

def check_overlap(t, m):
    # values inside the map
    overlap = None
    # before overlap
    outside1 = None
    # after overlap
    outside2 = None

# Check if start of t is before the map
#           #### MAP ####
#    S---------
    if t[0] < m[0]:

# Check if end is before the map
#           #### MAP ####
#    S---E
        if t[1] < m[0]:
            outside1 = t
# Check if end is inside the map
#           #### MAP ####
#    S--------E
        elif m[0] <= t[1] <= m[1]:
            overlap =  [m[0], t[1]]
            outside1 = [t[0], m[0] - 1]

# End is after the map
#           #### MAP ####
#    S-------------------------E
        else:
            overlap =  [m[0], m[1]]
            outside1 = [t[0], m[0] - 1]
            outside2 = [m[1] + 1, t[1]]



# Check if start of t is inside the map
#           #### MAP ####
#               S---------
    elif m[0] <= t[0] <= m[1]:

# Check if end is inside the map
#           #### MAP ####
#               S----E
        if m[0] <= t[1] <= m[1]:
            overlap = [t[0], t[1]]

# End has to be outside the map
#           #### MAP ####
#               S-----------E
        else:
            overlap =  [t[0], m[1]]
            outside2 = [m[0] + 1, t[1]]


    # start of t has to be after the map
    else: 
        outside2 = t

    return overlap, outside1, outside2

def solve(seed_tuples, mappings, order):
    min_dist = 9999999999999999
    for t in seed_tuples:
        start_seed, n = t
        ranges = [(start_seed, start_seed + n)]

        # Loop over a mapping, e.g. seed -> soil
        for source_dest in order:
            src_dest_map = mappings[source_dest]

            # Loop over a source range, e.g. source_range=(10, 20), delta=5
            for source_range, delta in src_dest_map.items():

                new_ranges = []
                # Loop over all tuples
                for r in ranges:
                    overlap, outside1, outside2 = check_overlap(r, source_range)
                    if overlap is not None:
                        print('overlap')
                        print(overlap)
                        overlap[0] += delta
                        overlap[1] += delta
                        new_ranges.append(overlap)
                    
                    if outside1 is not None:
                        new_ranges.append(outside1)
                    
                    if outside2 is not None:
                        new_ranges.append(outside2)
                
                ranges = new_ranges
    return ranges


def solve_old(seed_tuples, mappings, order):
    min_location = 99999999999999999
    for t in seed_tuples:
        start_seed, num_seeds = t
        for seed in range(start_seed, start_seed + num_seeds):
            val = seed
            for source_dest in order:
                src_dest_map = mappings[source_dest]
                for source_range, src_dest_map_func in src_dest_map.items():

                    if source_range[0] <= val <= source_range[1]:

                        val = src_dest_map_func(val)
                        break      
            
            if val < min_location:
                min_location = val

    return min_location

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

            delta = dest_start - source_start

            src_dest_mapping[(source_start, source_end)] = delta

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


    seed_tuples = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    total_seeds = sum(t[1] for t in seed_tuples)

    print(f'total seeds: {total_seeds}')
    print(solve(seed_tuples, mappings, order))
