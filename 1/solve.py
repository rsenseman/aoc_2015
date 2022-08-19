def part1(filepath):
    with open(filepath) as f:
        character_generator = (char for char in f.read().strip())
        floor_count = sum(
            (
                1 if char == '(' else -1
                for char
                in character_generator
            )
        )
    return floor_count

def part2(filepath):
    with open(filepath) as f:
        character_generator = (char for char in f.read().strip())

    char_counter = 0
    floor_counter = 0
    for char in character_generator:
        if floor_counter < 0:
            return char_counter
        elif char == '(':
            floor_counter += 1
        elif char == ')':
            floor_counter -= 1
        char_counter += 1

    return char_counter

if __name__ == '__main__':
    solution = part1('./data.txt')
    print(solution)

    solution = part2('./data.txt')
    print(solution)
