import re

BALLS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def extract_game_id(line: str):
    pattern = r'Game (\d+):'
    match = re.search(pattern, line)
    if match:
        return match.group(1)
    raise ValueError('There are no id in the input string: ' + line)


def extract_draws(line: str):
    draws = (line
        .split(':')[1]  # part after Game XX: [here]
        .split(';')     # [' 1 blue', ' 2 green', ' 1 red'], [' 3 blue', ...], ...
    )
    return draws


def check_valid_game(draws: str, balls: dict):
    for draw in draws:
        for ball in draw.split(','):
            quantity, color = ball.strip().split(' ')
            if int(quantity) > balls[color]:
                return False
    return True


if __name__ == '__main__':
    with open('2\input.txt') as f:
        inp = f.readlines()
    
    s = 0

    for game in inp:
        game_id = extract_game_id(game)
        draws = extract_draws(game)
        valid = check_valid_game(draws, BALLS)
        if valid:
            s += int(game_id)

    print(s)