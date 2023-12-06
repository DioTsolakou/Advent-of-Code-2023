import os

def get_ways_per_race(race_time, rec_dist):
    ret = 0

    for t in range(race_time):
        # the distance we will do is holding time * (total race time - holding time)
        # since increasing holding time increases speed by the same amount
        race_dist = t*(race_time - t) 
        if race_dist > rec_dist:
            ret += 1

    return ret

def get_number_of_ways(times, distances):
    total_ways = 1
    for i in range(len(times)):
        ret = get_ways_per_race(int(times[i]), int(distances[i]))
        total_ways *= ret
        
    return total_ways

def get_number_of_ways_for_race(times, distances):
    total_ways = 0
    time, distance = '', ''

    for i in range(len(times)):
        time += times[i]
        distance += distances[i]
    
    total_ways = get_ways_per_race(int(time), int(distance))
    return total_ways


def main():
    current_path = os.path.dirname(__file__)
    input_path = "day6-input.txt"
    full_path = os.path.join(current_path, input_path)
    input = open(full_path).read().strip().splitlines()
    times, distances = [x.split(':')[1].split() for x in input]

    result1 = get_number_of_ways(times, distances)
    print(result1)
    
    result2 = get_number_of_ways_for_race(times, distances)
    print(result2)



if __name__ == '__main__':
    main()