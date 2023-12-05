import re
from collections import defaultdict

def get_card_number(card_line) -> str:
    pattern = r'^Card\s+(\d+):'
    return re.search(pattern, card_line).group(1)

def get_winning_numbers(card_line) -> list[int]:
    pattern = r'Card\s+\d+: ([\d\s]*?) \|'
    numbers_string = re.search(pattern, card_line).group(1)
    return [int(n) for n in numbers_string.split(' ') if n != '']

def get_chosen_numbers(card_line) -> list[int]:
    pattern = r'\| ([\d\s]*?)$'
    numbers_string = re.search(pattern, card_line).group(1)
    return [int(n) for n in numbers_string.split(' ') if n != '']

def update_multiplier(current_card_num: str, num_correct: int, 
                      weight: int, multipler: dict) -> dict:
    
    for card in range(int(current_card_num)+1, int(current_card_num)+1+num_correct):
        multipler[str(card)] += weight
    return multipler

if __name__ == '__main__':
    with open('4\input.txt') as f:
        inp = [line.strip() for line in f.readlines()]
    
    card_multipliers = defaultdict(lambda: 1)
    score = 0

    for line in inp:
        card_number = get_card_number(line)
        winning_numbers = get_winning_numbers(line)
        chosen_numbers = get_chosen_numbers(line)

        # translates to how many copies you have of the current card
        weight = card_multipliers[card_number]
        num_correct = len(set(chosen_numbers).intersection(set(winning_numbers)))
        card_multipliers = update_multiplier(card_number, num_correct, weight, card_multipliers)

        score += weight
    print(score)
