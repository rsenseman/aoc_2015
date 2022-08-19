import hashlib
from itertools import count

def parse_input(filename):
    with open(filename) as f:
        return f.read().strip()


def get_byte_hash(hash_key, input_string):
    query_string = (hash_key + input_string).encode('utf-8')
    hex_result = hashlib.md5(query_string).hexdigest()
    return hex_result


def solve1(filename):
    hash_key = parse_input(filename)

    for i in count():
        byte_hash = get_byte_hash(hash_key, str(i))
        if byte_hash[:5] == '00000':
            return i


def solve2(filename):
    hash_key = parse_input(filename)

    for i in count():
        byte_hash = get_byte_hash(hash_key, str(i))
        if byte_hash[:6] == '000000':
            return i

if __name__ == '__main__':
    # print(solve1('./data.txt'))
    print(solve2('./data.txt'))
