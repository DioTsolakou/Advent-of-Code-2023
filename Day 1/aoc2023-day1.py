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

def part2(input_array):
    total_sum = 0
    num_spelling = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    num_words_regex = re.compile(r"(?=(\d|" + "|".join(num_spelling) + r"))")

    for j in range(len(input_array)):
        line = input_array[j]
        found = re.findall(num_words_regex, line)
        nums = [found[0], found[len(found) - 1]]

        for i in range(len(nums)):
            num = nums[i]
            if num.isdigit():
                nums[i] = num
            else:
                nums[i] = num_spelling.get(num)
        
        total_sum += int(''.join(nums))

    return total_sum

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day1-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.rstrip() for line in input]

    part1_answer = part1(input_array)
    part2_answer = part2(input_array)
    
    print(part1_answer)
    print(part2_answer)

if __name__ == '__main__':
    main()