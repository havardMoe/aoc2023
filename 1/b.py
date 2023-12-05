TYPED_NUMBERS = [
    'one',
    'two', 
    'three', 
    'four', 
    'five', 
    'six', 
    'seven', 
    'eight', 
    'nine'
]

REVERSED_TYPED_NUMBERS = [
    'eno', 
    'owt', 
    'eerht', 
    'ruof', 
    'evif', 
    'xis', 
    'neves', 
    'thgie', 
    'enin'
]


def find_first_digit_modified(s: str, r:bool):
    if r:
        s = s[::-1]
    for i, c in enumerate(s):
        if c.isdigit():
            # check if there exists a number written in text before it
            wordlist = TYPED_NUMBERS if not r else REVERSED_TYPED_NUMBERS
            # look for matches and keep the index of the potential match for each number
            positions = [(s[:i].find(word), number) for number, word in enumerate(wordlist, 1)]
            # only count as a hit if the index is not -1
            hits = [(idx, number) for (idx, number) in positions if idx != -1]
            # find the first match if any      
            first_hit = None 
            if len(hits) > 0:
                first_hit = sorted(hits, key=lambda tuple: tuple[0])[0]
                if first_hit[0] < i:
                    return str(first_hit[1])
                
            # there is not a written number before it, return the int
            return c
    raise ValueError('please insert a string with a number or typed number included')


if __name__ == '__main__':
    with open('1\input.txt') as f:
        inp = f.readlines()
    
    numbers = []
    
    for line in inp:
        first = find_first_digit_modified(line, r=False)
        last = find_first_digit_modified(line, r=True)
        numbers.append(int(first + last))
    
    print(sum(numbers))