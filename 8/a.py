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

    directions_pattern = r'^([LR]+)'
    direction = re.search(directions_pattern, inp).group(1)

    node_pattern = r'\n'
    