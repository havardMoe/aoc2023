import re
from collections import defaultdict

def find_min_tuple(tuples):
    return min(min(t) for t in tuples)

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
            outside2 = [m[1] + 1, t[1]]


    # start of t has to be after the map
    else: 
        outside2 = t

    return overlap, outside1, outside2

def solve(seed_tuples, mappings, order):
    current_min = 999999999999999999999

    for t in seed_tuples:
        start_seed, n = t
        ranges = [(start_seed, start_seed + n - 1)]
        
        # Loop over a mapping, e.g. seed -> soil
        for source_dest in order:
            src_dest_map = mappings[source_dest]
            
            ranges_after_filtering = []
            ranges_not_mapped = []

            # Loop over a source range, e.g. source_range=(10, 20), delta=5
            for source_range, delta in src_dest_map.items():
                

                # Loop over all tuples
                for r in ranges:
                    overlap, outside1, outside2 = check_overlap(r, source_range)
                    if overlap is not None:
                        overlap[0] += delta
                        overlap[1] += delta
                        ranges_after_filtering.append(overlap)

                        if outside1 is not None:
                            ranges_not_mapped.append(outside1)
                        
                        if outside2 is not None:
                            ranges_not_mapped.append(outside2)

                    else:
                        ranges_not_mapped.append(r)

                # Finished mapping a given range for a given source dest mapping
                # This list will be looped over for the next range for the same source dest
                ranges = ranges_not_mapped.copy()
                ranges_not_mapped = []

            # Finished source -> dest mapping
            # Preparing range list for next source, dest mapping
            ranges.extend(ranges_after_filtering.copy())
            ranges_after_filtering = []
            ranges_not_mapped = []
            # print(ranges)

        # Finished iterating over seed
        # finding min:
        min_seed = find_min_tuple(ranges)
        if min_seed < current_min:
            current_min = min_seed
    return current_min


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

    tuples = solve(seed_tuples, mappings, order)
    print(tuples)
    # print(tuples)
    # print(min([min(t) for t in tuples]))
