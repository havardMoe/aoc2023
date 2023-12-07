import re
from enum import Enum
from collections import defaultdict


class HandStrength(Enum):
    FIVE_OAK = 7
    FOUR_OAK = 6
    FULL_HOUSE = 5
    THREE_OAK = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1


CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}


def calculate_hand_strenght(hand: str):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1
    
    card_counts = [kv for kv in d.items()]
    # sort by number of card occurences (most occuring first)
    card_counts.sort(key=lambda kv: kv[1], reverse=True)

    strenght = HandStrength.HIGH_CARD

    # we dont care about which card it is
    _, occurences = card_counts[0]
    if occurences == 5:
        strenght = HandStrength.FIVE_OAK
    elif occurences == 4:
        strenght = HandStrength.FOUR_OAK
    elif occurences == 3:
        # if next most common occurence is 2
        if card_counts[1][1] == 2:
            strenght = HandStrength.FULL_HOUSE
        else:
            strenght = HandStrength.THREE_OAK
    elif occurences == 2:
        if card_counts[1][1] == 2:
            strenght = HandStrength.TWO_PAIR
        else:
            strenght = HandStrength.PAIR
    
    return strenght.value
    

def calculate_hand_values(hand: str):
    return [CARD_VALUES[c] for c in hand]


def total_winnings(hands):
    return sum(i*cnb[2] for i, cnb in enumerate(hands, 1))


if __name__ == '__main__':
    with open('7/input.txt') as f:
        inp = f.read()

    card_pattern = r'([AKQJT2-9]{5})\s+\d+'
    cards = re.findall(card_pattern, inp)

    bid_pattern = r'[AKQJT2-9]{5}\s+(\d+)'
    bids = [int(b) for b in re.findall(bid_pattern, inp)]

    # [HandStrength, [card value 1, ... card value 5], bid]
    cards_and_bets = [
        [calculate_hand_strenght(c), calculate_hand_values(c), b] 
        for (c, b) in zip(cards, bids)
    ]

    cards_and_bets.sort(key=lambda x: (x[0], [c for c in x[1]]))

    for v in cards_and_bets:
        print(v)

    result = total_winnings(cards_and_bets)
    print(result)

    #247889944