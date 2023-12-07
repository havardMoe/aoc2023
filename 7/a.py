import re
from enum import Enum
from collections import defaultdict

class HandStrength(Enum):
    FIVE_OAK = 6
    FOUR_OAK = 5
    FULL_HOUSE = 4
    THREE_OAK = 3
    PAIR = 2
    HIGH_CARD = 1

def calculate_hand_strenght(hand: str):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1
    


if __name__ == '__main__':
    with open('7/input.txt') as f:
        inp = f.read()

    card_pattern = r'\n([AKQJT2-9]{5})'
    bid_pattern = r'\n[AKQJT2-9]{5}\s+(\d+)'

    cards = re.findall(card_pattern, inp)
    print(cards)

    bids = re.findall(bid_pattern, inp)
    print(bids)
