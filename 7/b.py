import re
from collections import defaultdict


CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,

    'J': 0,  # jokers are nerfed
}


def calculate_hand_strenght(hand: str):
    d = defaultdict(int)
    for c in hand:
        d[c] += 1
    
    card_counts = [kv for kv in d.items()]
    # sort by number of card occurences (most occuring first)
    card_counts.sort(key=lambda kv: kv[1], reverse=True)

    strenght = 1

    # we dont care about which card it is
    most_common_card, occurences = card_counts[0]
    most_common_is_joker = most_common_card == 'J'


    if len(card_counts) > 1:
        second_most_common_occurence = card_counts[1][1]
        second_most_common_is_joker = card_counts[1][0] == 'J'
    else:
        second_most_common_occurence = 0
        second_most_common_is_joker = False

    num_jokers = d['J']
    jokers = num_jokers > 0

    if occurences == 5:
        strenght = 5

    elif occurences == 4:
        if jokers:  # either 4 or 1 jokers, both sets a strenght of 5
            strenght = 5
        else:
            strenght = 4
        
    elif occurences == 3:
        if jokers and not most_common_is_joker:
            # there is either 1 or 2 jokers
            if num_jokers == 1:
                strenght = 4
            elif num_jokers == 2:
                strenght = 5
        elif jokers and most_common_is_joker:
            if second_most_common_occurence == 2:
                strenght = 5
            else:
                strenght = 4
        else:
            # there are no jokers but second card exists twice
            if second_most_common_occurence == 2:
                strenght = 3.5
            else:
                strenght = 3


    elif occurences == 2:
        if second_most_common_occurence == 2:
            if jokers:
                if most_common_is_joker or second_most_common_is_joker:
                    strenght = 4  # use two jokers to get 4oak
                else:
                    strenght = 3.5  # use 1 joker on either of the 2's to get a house
            else:
                # there are no jokers
                strenght = 2.5  # two pair
        else:
            if jokers:
                strenght = 3  # use a single joker to get 3oak
            else:
                strenght = 2

    
    elif occurences == 1:
        if jokers:
            strenght = 2
        else:
            strenght = 1

    return strenght
    

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

    result = total_winnings(cards_and_bets)
    print(result)
    # 250184965
    # 251116261
    # 251195607