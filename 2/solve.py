def clean_row(row):
    split_row = row.strip().split('x')
    sorted_int_row = sorted([int(val) for val in split_row])
    return sorted_int_row

def parse_input(filename):
    with open(filename) as f:
        return map(clean_row, f.readlines())

def solve1(filename):
    input_tuples = parse_input(filename)

    running_total = 0
    for low, mid, high in input_tuples:
        running_total += 2*low*mid + 2*mid*high + 2*high*low
        running_total += low*mid

    return running_total

def solve2(filename):
    input_tuples = parse_input(filename)

    running_total = 0
    for low, mid, high in input_tuples:
        running_total += 2*low + 2*mid
        running_total += low*mid*high

    return running_total

if __name__ == '__main__':
    print(solve1('./data.txt'))
    print(solve2('./data.txt'))
