import re
from functools import reduce

# mm/m2**2
ACCELERATION = 1

def calc_distance(speed, time):
    return speed * time

def calc_posibilities(max_time) -> [int]:  # returns a list of distances where index is the amount of ms the button is held
    return [calc_distance(ACCELERATION * t, max_time - t) for t in range(max_time + 1)]

def calc_ways_to_beat_record(possibilities, record):
    return len(list(filter(lambda d: d > record, possibilities)))

if __name__ == '__main__':
    with open('6/input.txt') as f:
        inp = f.read()
    
    time_pattern = r'Time:([\d\s]+)'
    time = [int(n) for n in  re.search(time_pattern, inp).group(1).strip().split(' ') if n != '']

    distance_pattern = r'Distance:([\d\s]+)'
    distance = [int(n) for n in  re.search(distance_pattern, inp).group(1).strip().split(' ') if n != '']
    
    ways_of_winning_total = []

    for t, d in zip(time, distance):
        possibilities = calc_posibilities(t)
        ways_to_beat_record = calc_ways_to_beat_record(possibilities, d)
        ways_of_winning_total.append(ways_to_beat_record)
    
    product = reduce(lambda x, y: x * y, ways_of_winning_total)

    print(ways_of_winning_total)
    print(product)
