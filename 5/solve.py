from collections import Counter

VOWELS = 'aeiou'
FORBIDDEN_TEXTS = ('ab', 'cd', 'pq', 'xy')

def parse_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def is_string_nice_1(input_string):
    vowel_count = len([char for char in input_string if char in VOWELS])
    if vowel_count < 3:
        return False

    string_offset = zip(input_string[:-1], input_string[1:])
    twice_in_a_row_count = sum(map(lambda tup: tup[0]==tup[1], string_offset))
    if twice_in_a_row_count == 0:
        return False

    forbidden_count = len([txt for txt in FORBIDDEN_TEXTS if txt in input_string])
    if forbidden_count > 0:
        return False

    return True

def solve1(filename):
    input_strings = parse_input(filename)

    num_nice_strings = len([string for string in input_strings if is_string_nice_1(string)])
    return num_nice_strings

def is_string_nice_2(input_string):
    letter_pairs = zip(input_string[:-1], input_string[1:])
    valid_letter_pairs_counter = 0

    true_count = None
    for pair, count in Counter(letter_pairs).items():
        if count > 1:
            if pair[0] == pair[1]:
                tri_counter = Counter(zip(input_string[:-1], input_string[1:], input_string[2:]))
                overlap_count = 2 * tri_counter.get((pair[0], pair[0], pair[0]), 0)
                true_count = count - overlap_count
            else:
                true_count = count
            print(pair, count, true_count)
            if true_count > 1:
                valid_letter_pairs_counter += 1

    if valid_letter_pairs_counter == 0:
        return False

    string_offset = zip(input_string[:-1], input_string[1:], input_string[2:])
    pattern_matches = [tup for tup in string_offset if tup[0]==tup[2]]
    if len(pattern_matches) == 0:
        return False
    else:
        print(pattern_matches)

    return True

def test_string(input_string):
     if is_string_nice_2(input_string):
         print(f'+: {input_string}')
     else:
        print(f'-: {input_string}')

def solve2(filename):
    input_strings = parse_input(filename)

    for string in input_strings:
         test_string(string)

    # num_nice_strings = len([string for string in input_strings if is_string_nice_2(string)])
    # return num_nice_strings

if __name__ == '__main__':
    # print(solve1('./data.txt'))
    print(solve2('./data.txt'))

    test_string('qjhvhtzxzqqjkmpb')
