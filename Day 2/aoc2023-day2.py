import os
from math import prod

def check_set_values(dictionary):
    ret = True
    max_red, max_green, max_blue = 12, 13, 14
    if (dictionary['red'] > max_red) or (dictionary['blue'] > max_blue) or (dictionary['green'] > max_green):
        ret = False
    return ret

def get_max(game_maxes, dictionary):
    for key in dictionary.keys():
        if dictionary[key] > game_maxes[key]:
            game_maxes[key] = dictionary[key]

    return game_maxes


def possible_games(games, p2 = False):
    total_sum = 0

    for i in range(len(games)):
        possible_game = True
        game = games[i]
        game_maxes = {'red': 0, 'blue': 0, 'green': 0}
        for set in game.split('; '):
            # create dict with red, green, blue keys and respective values
            dictionary = dict((y.strip(), int(x.strip()))
             for x, y in (element.split(' ') 
             for element in set.split(', ')))
            
            if 'red' not in dictionary:
                dictionary['red'] = 0
            if 'blue' not in dictionary:
                dictionary['blue'] = 0
            if 'green' not in dictionary:
                dictionary['green'] = 0
            
            if p2:
               game_maxes = get_max(game_maxes, dictionary)
            elif not check_set_values(dictionary):
                possible_game = False
                break
                

        if p2:
            game_maxes_val_list = game_maxes.values()
            total_sum += prod(game_maxes_val_list)
        elif possible_game:
            total_sum += i + 1
    
    return total_sum


def main():
    current_path = os.path.dirname(__file__)
    input_path = "day2-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path, "r")
    input_array = [line.strip()[line.index(':') + 2:] for line in input]

    result1 = possible_games(input_array)
    result2 = possible_games(input_array, True)

    print(result1)
    print(result2)

if __name__ == '__main__':
    main()