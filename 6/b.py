import re
from functools import reduce

# mm/m2**2
ACCELERATION = 1

def calc_distance(speed, time):
    return speed * time

def calc_posibilities_beating_record(max_time, record) -> int:
    i = 0
    for t in range(max_time + 1):
        d = calc_distance(ACCELERATION * t, max_time - t)
        if record < d:
            i += 1
        if i > 0 and record >= d:
            break
    return i
    


if __name__ == '__main__':
    with open('6/input.txt') as f:
        inp = f.read()
    
    time_pattern = r'Time:([\d\s]+)'
    time = int(re.search(time_pattern, inp).group(1).strip().replace(' ', ''))

    distance_pattern = r'Distance:([\d\s]+)'
    distance = int(re.search(distance_pattern, inp).group(1).strip().replace(' ', ''))
    
        
    ways_of_winning_total = []

    possibilities = calc_posibilities_beating_record(time, distance)
   
    print(possibilities)
