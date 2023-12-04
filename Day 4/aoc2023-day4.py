import os
from collections import defaultdict

def get_total_points(input_array, p2=False):
    total_sum = 0
    input_len = len(input_array)

    total_cards = []
    total_cards = defaultdict(lambda: 0 * len(input_array)) # init dict with length of input and default value of 0

    for i in range(input_len):
        total_cards[i] += 1
        curr_card = input_array[i]
        winning_nums, our_nums = curr_card.split('|')
        winning_nums, our_nums = winning_nums.split(), our_nums.split()

        card_occurrences = sum(x in winning_nums for x in our_nums)

        if p2 and card_occurrences:
            for j in range(min(i + 1, input_len), min(i + (1*card_occurrences) + 1, input_len)):
                total_cards[j] += total_cards[i] # add to next cards the amount of instances (original + copies) of current card
        elif card_occurrences:
            total_sum += 1 * pow(2, card_occurrences - 1)
    
    if p2:
        total_sum = sum(total_cards.values())

    return total_sum

def main():
    current_path = os.path.dirname(__file__)
    input_path = "day4-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.strip()[line.index(':') + 2:] for line in input]

    result1 = get_total_points(input_array)
    result2 = get_total_points(input_array, True)

    print(result1)
    print(result2)


if __name__ == '__main__':
    main()