import os
import re

def check_set_values(dictionary):
    ret = True
    max_red, max_green, max_blue = 12, 13, 14
    if ('red' in dictionary and dictionary['red'] > max_red) or ('blue' in dictionary and dictionary['blue'] > max_blue) or ('green' in dictionary and dictionary['green'] > max_green):
        ret = False
    return ret


def possible_games(games):
    
    total_sum = 0

    for i in range(len(games)):
        possible_game = True
        game = games[i]
        for set in game.split('; '):
            dictionary = dict((y.strip(), int(x.strip()))
             for x, y in (element.split(' ') 
             for element in set.split(', ')))
            
            if not check_set_values(dictionary):
                possible_game = False
                break

        if possible_game:
            total_sum += i + 1
    
    return total_sum


def main():
    current_path = os.path.dirname(__file__)
    input_path = "day2-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.strip()[line.index(':') + 2:] for line in input]

    result = possible_games(input_array)
    print(result)

if __name__ == '__main__':
    main()