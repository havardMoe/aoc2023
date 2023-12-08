import re


if __name__ == '__main__':

    test_inp = '''LLR
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

    # with open('8/input.txt') as f:
    #     inp = f.read()
    
    inp = test_inp

    directions_p = r'^([LR]+)'
    direction = re.search(directions_p, inp).group(1)

    print(direction)

    