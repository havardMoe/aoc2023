import re

if __name__ == '__main__':
    # patterns
    seeds_p = r'^seeds:\s*([\s\d]+)$'

    # A-to-B map:
    maps_p = r'^([a-zA-Z]+)-to-([a-zA-Z]+) map:\n([\d \n]+)$'

    with open('5/input.txt') as f:
        inp = f.read()

    
    seeds = re.findall(seeds_p, inp)

    a = seeds
    print(a)
    