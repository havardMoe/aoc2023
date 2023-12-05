# find all numbers, and store it in a dict with coordinates as keys
# value should be on format
# {
#   number: XXX,
#   coordinates: [
#       (first coordinate), 
#       (coordinate for digit 2), ... 
#       (coordinate for digit n)
#   ]
# }
# each number can have multiple coordinates, one for each digit.

# for each valid symbol, for each neighbouring coordinate, look for numbers in the dict
# If you find one, then remove it, and all its coordinates from the dict 
# (can be found from the coordinates list)
# Else, go to next symbol

# Funcitons needed:
# a funciton to find digits and store them in a dict
def find_numbers(lines: list[str]):
    numbers = {}
    x_indexes = []
    current_number = ''

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c.isdigit():
                x_indexes.append(x)
                current_number += c  # append the current number string
            elif current_number:
                # c is not a digit, and there was a number from the previous character(s)
                numbers = _update_numbers_dict(numbers, y, x_indexes, current_number)
                # number is stored in the dict. Reset temp values:
                x_indexes = []
                current_number = ''
        # at the end of a line:
        if current_number:
            numbers = _update_numbers_dict(numbers, y, x_indexes, current_number)
            x_indexes = []
            current_number = ''

    return numbers


# function to update the numbers dict based on the temp variables
def _update_numbers_dict(numbers: dict, y: int, x_indexes: list[int], current_number: str):
    valid_coordinates = [f'{y},{x}' for x in x_indexes]
    for coordinate in valid_coordinates:
        numbers[coordinate] = {
            'number': int(current_number),
            'coordinates': valid_coordinates
        }
    return numbers


# function to return all neighbouring coordinates based on an input coordinate
def neighbouring_coordinates(y: int, x: int) -> list[str]:
    neighbours = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if not (dy == 0 and dx == 0):
                neighbours.append(f'{y + dy},{x + dx}')
    return neighbours

# a function to find all valid symbols and return a list of symbol coordinates
def find_valid_stars(lines: list[str]):
    symbol_coordinates = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c == '*':
                # character is a valid symbol
                symbol_coordinates.append((y, x))
    return symbol_coordinates

if __name__ == '__main__':
    with open('3\input.txt') as f:
        inp = f.readlines()


    numbers = find_numbers(inp)
    star_coordinates = find_valid_stars(inp)

    star_neighbour_coordinates = []
    for coord in star_coordinates:
        star_neighbour_coordinates.append(neighbouring_coordinates(*coord))
    
    s = 0
    # for each of the stars found
    for coords in star_neighbour_coordinates:
        temp_numbers = []
        temp_taken_coords = set()

        # for each of the neighboring coordinates
        for coord in coords:
            # see if there is a number present that is not already looked at
            if coord in numbers and coord not in temp_taken_coords:
                # there is a number, append it to the temp numbers list
                temp_numbers.append(numbers[coord]['number'])
                # also keep track of which coordinates belong to this number
                temp_taken_coords = temp_taken_coords.union(numbers[coord]['coordinates'])

        # check if there are exactly 2 numbers
        if len(temp_numbers) == 2:
            # add the product of these numbers to the total sum
            s += (temp_numbers[0] * temp_numbers[1])
        # else, do nothing about the sum and reset variables to the next iteration
        temp_numbers = []
        temp_taken_coords = set()
        
        
    print(s)