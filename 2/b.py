from collections import defaultdict
from functools import reduce


def extract_draws(line: str):
    draws = (line
        .split(':')[1]  # part after Game XX: [here]
        .split(';')     # [' 1 blue', ' 2 green', ' 1 red'], [' 3 blue', ...], ...
    )
    return draws


def minimum_ball_quantity(draws: str):
    minimum = defaultdict(int)

    for draw in draws:
        for ball in draw.split(','):
            quantity, color = ball.strip().split(' ')
            if int(quantity) > minimum[color]:
                minimum[color] = int(quantity)

    return minimum


if __name__ == '__main__':
    with open('2\input.txt') as f:
        inp = f.readlines()
    
    s = 0
    for game in inp:
        draws = extract_draws(game)
        quantities = minimum_ball_quantity(draws)
        s += reduce(lambda x, y: x * y, quantities.values())

    print(s)