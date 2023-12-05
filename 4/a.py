import re

def get_winning_numbers(card_line) -> list[int]:
    pattern = r'Card\s+\d+: ([\d\s]*?) \|'
    # Capture group 1 is the part marked with paranthesis in the pattern
    # use re.search instead of findall because there should be only one match
    numbers_string = re.search(pattern, card_line).group(1)
    return [int(n) for n in numbers_string.split(' ') if n != '']

def get_chosen_numbers(card_line) -> list[int]:
    pattern = r'\| ([\d\s]*?)$'
    numbers_string = re.search(pattern, card_line).group(1)
    return [int(n) for n in numbers_string.split(' ') if n != '']

def get_score(num_correct: int) -> int:
    if num_correct == 0:
        return 0
    return 2**(num_correct - 1)

if __name__ == '__main__':
    with open('4\input.txt') as f:
        inp = [line.strip() for line in f.readlines()]
    
    s = 0
    for line in inp:
        winning_numbers = get_winning_numbers(line)
        chosen_numbers = get_chosen_numbers(line)
        num_correct = len(set(chosen_numbers).intersection(set(winning_numbers)))
        s += get_score(num_correct)
    print(s)
