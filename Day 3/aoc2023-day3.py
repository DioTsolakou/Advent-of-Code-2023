import os
import re
from math import prod

def check_adjacent_symbols(curr_line, input_array, i, special_chars, total_sum):
    empty_line = '.' * len(curr_line)
    input_array_with_empy_lines = [empty_line] + input_array + [empty_line]

    for num in re.finditer(r'\d+', curr_line):
        num_start, num_end = num.span()
        num_start, num_end = max(num_start - 1, 0), min(num_end + 1, len(curr_line))
        adjacent_chars = []

        for row in input_array_with_empy_lines[i:i+3]:
            adjacent_chars.append(row[num_start:num_end])

        if re.search(special_chars, ''.join(adjacent_chars)):
            total_sum += int(num.group())

    return total_sum

    # failed and too complex attempt at recursion
    """ num = re.search(r'\d+', curr_line)
    if not num:
        return total_sum
    else:
        num_start, num_end = num.span()
        proper_start, proper_end = num_start + starting_index, num_end + starting_index
        adjacent_chars = []

        if num_start - 1 > 0:
            adjacent_chars.append(curr_line[num_start - 1])
        if num_end + 1 < len(curr_line):
            adjacent_chars.append(curr_line[num_end + 1])

        #adjacent_chars = [curr_line[num_start - 1], curr_line[num_end + 1]] # initialize with left and right

        for j in range(proper_start - 1, proper_end + 1):
            if i == 0 or (i > 0 and i < len(input_array) - 1) and (j < len(input_array[i])) and j > 0 :
                adjacent_chars.append(input_array[i + 1][j])
            if i == len(input_array) - 1 or (i > 0 and i < len(input_array) - 1) and j < len(input_array[i]) and j > 0:
                adjacent_chars.append(input_array[i - 1][j])    
        
        adjacent_chars_to_string = ''.join(adjacent_chars)

        if (re.search(special_chars, adjacent_chars_to_string)):
            total_sum += int(num.group())

        curr_line = curr_line[num_end:]
        starting_index += num_end
        return check_adjacent_symbols(curr_line, input_array, i, special_chars, total_sum, starting_index) """    


def sum_part_numbers(input_array, special_chars):
    total_sum = 0

    for i in range(len(input_array)):
        curr_line = input_array[i]
        total_sum = check_adjacent_symbols(curr_line, input_array, i, special_chars, total_sum)
        
    return total_sum

def check_gears(curr_line, input_array, i, gear_char, total_sum):
    empty_line = '.' * len(curr_line)
    input_array_with_empy_lines = [empty_line] + input_array + [empty_line]

    for gear in re.finditer(gear_char, curr_line):
        gear_start, gear_end = gear.span()

        # not sure why I copied this from part 1, cost me too much time trying to find why total_sum was wrong...
        #gear_start, gear_end = max(gear_start - 1, 0), min(gear_end + 1, len(curr_line))

        adjacent_nums = []

        for row in input_array_with_empy_lines[i:i+3]:
            for num in re.finditer(r'\d+', row):
                num_start, num_end = num.span()
                
                if gear_start in range(num_start - 1, num_end + 1):
                    adjacent_nums.append(int(num.group(0)))
        
        if len(adjacent_nums) == 2:
            total_sum += prod(adjacent_nums)

    return total_sum

def sum_gear_ratios(input_array, gear_char):
    total_sum = 0

    for i in range(len(input_array)):
        curr_line = input_array[i]
        total_sum = check_gears(curr_line, input_array, i, gear_char, total_sum)
    
    return total_sum

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day3-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.strip() for line in input]
    special_chars = re.compile(r'[^.0-9]')
    gear_char = re.compile(r'\*')

    result1 = sum_part_numbers(input_array, special_chars)
    result2 = sum_gear_ratios(input_array, gear_char)

    print(result1)
    print(result2)

if __name__ == '__main__':
    main()