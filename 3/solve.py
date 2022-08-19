from collections import Counter

DIRECTION_PARSER = {
    '<':(-1,0),
    '>':(+1,0),
    '^':(0,+1),
    'v':(0,-1),
}

def parse_input(filename):
    with open(filename) as f:
        return (DIRECTION_PARSER[val] for val in f.read().strip())

def solve1(filename):
    input_directions = parse_input(filename)

    current_house = (0,0)
    house_counter = Counter([current_house])
    for direction in input_directions:
        current_house = (current_house[0] + direction[0], current_house[1] + direction[1])
        house_counter.update([current_house])

    num_visted = len([(house, count) for house, count in house_counter.items() if count >= 1])
    print(house_counter)
    return num_visted

def solve2(filename):
    input_directions = parse_input(filename)

    santa_house = (0,0)
    robo_house = (0,0)
    house_counter = Counter([santa_house, robo_house])
    is_santa_turn = True
    for direction in input_directions:
        if is_santa_turn:
            santa_house = (santa_house[0] + direction[0], santa_house[1] + direction[1])
            house_counter.update([santa_house])
        else:
            robo_house = (robo_house[0] + direction[0], robo_house[1] + direction[1])
            house_counter.update([robo_house])

        is_santa_turn = not is_santa_turn

    num_visted = len([(house, count) for house, count in house_counter.items() if count >= 1])
    return num_visted

if __name__ == '__main__':
    print(solve1('./data.txt'))
    print(solve2('./data.txt'))
