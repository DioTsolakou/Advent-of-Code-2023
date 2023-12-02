import re
import os

def part1(input_array):
    total_sum = 0

    for line in input_array:
        extracted_nums = "".join(re.findall(r'([0-9])', line))

        if len(extracted_nums) == 1:
            extracted_nums += extracted_nums
        elif len(extracted_nums) > 2:
            extracted_nums = extracted_nums[0] + extracted_nums[len(extracted_nums) - 1]
        
        total_sum += int(extracted_nums)

    return total_sum

""" def part2(input_array):
    return input_array """

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day1-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.rstrip() for line in input]

    part1_answer = part1(input_array)
    """ part1_answer = part2(input_array) """
    
    
    print(part1_answer)

if __name__ == '__main__':
    main()