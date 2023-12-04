import os

def get_total_points(input_array):
    total_sum = 0

    for i in range(len(input_array)):
        curr_card = input_array[i]
        winning_nums, our_nums = curr_card.split('|')
        winning_nums, our_nums = winning_nums.split(), our_nums.split()

        card_occurrences = sum(x in winning_nums for x in our_nums)

        if card_occurrences:
            total_sum += 1 * pow(2, card_occurrences - 1)

    return total_sum

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day4-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.strip()[line.index(':') + 2:] for line in input]

    result = get_total_points(input_array)
    print(result)


if __name__ == '__main__':
    main()