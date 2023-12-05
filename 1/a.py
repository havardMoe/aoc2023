
def find_first_digit(s: str):
    for c in s:
        if c.isdigit():
            return c
    raise ValueError('please insert a string with a number included')


if __name__ == '__main__':
    with open('1\input.txt') as f:
        inp = f.readlines()
    
    numbers = []
    
    for line in inp:
        first = find_first_digit(line)
        last = find_first_digit(line[::-1])
        numbers.append(int(first + last))
    
    print(sum(numbers))
