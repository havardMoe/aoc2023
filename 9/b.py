def generate_derivative(pattern):
    return [pattern[i] - pattern[i-1] for i in range(1, len(pattern))]
    
def generate_derivative_pyramid(pattern):
    pyramid = [pattern]
    
    while not (all(n == 0 for n in pyramid[-1]) or len(pattern) < 2):
        pattern = generate_derivative(pattern)
        pyramid.append(pattern)
    
    if not all(n == 0 for n in pyramid[-1]):
        raise Exception('Never reached zero')

    return pyramid

def fill_pyramid_reverse(pyramid):
    # start at the bottom of the pyramid (zeros)
    for i in range(len(pyramid) - 1, -1, -1):
        pattern = pyramid[i]

        # check if row is bottom
        if all(n == 0 for n in pattern):
            pattern.append(0)
        
        else:
            # get the change from the row below
            derivate = pyramid[i + 1][0]
            first_value = pattern[0]
            pattern.insert(0, first_value - derivate)


if __name__ == '__main__':
    with open('9/input.txt') as f:
        patterns = [[int(n) for n in line.strip().split(' ')] for line in f.readlines()]

    next_numbers = []

    for pattern in patterns:
        pyramid = generate_derivative_pyramid(pattern)
        fill_pyramid_reverse(pyramid)
        next_numbers.append(pyramid[0][0])
    
        # print(pyramid)

    print(sum(next_numbers))