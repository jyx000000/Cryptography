from base64 import b64decode
from C3 import force, get_english_score
from C5 import encodeRepeatingKeyXor
from itertools import combinations

def hamming_distance(binary_seq_1, binary_seq_2):
    assert len(binary_seq_1) == len(binary_seq_2)
    dist = 0

    for bit1, bit2 in zip(binary_seq_1, binary_seq_2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])

    return dist


def break_repeating_key_xor(binary_data):
    normalized_distances = {}
    # print(chunks)
    for key_size in range(2, 41):
        chunks = [binary_data[i:i + key_size] for i in range(0, len(binary_data), key_size)][:4]
        distance = 0
        pairs = combinations(chunks, 2)

        for (x, y) in pairs:
            distance += hamming_distance(x, y)

        distance /= 6
        normalized_distance = distance / key_size
        normalized_distances[key_size] = normalized_distance

    possible_key_sizes = sorted(normalized_distances, key=normalized_distances.get)[:3]
    possible_plaintexts = []

    for d in possible_key_sizes:
        key = b''
        for i in range(d):
            block = b''

            for j in range(i, len(binary_data), d):
                block += bytes([binary_data[j]])

            key += bytes([force(block)['key']])

        possible_plaintexts.append((encodeRepeatingKeyXor(binary_data, key), key))

    print()
    return max(possible_plaintexts, key=lambda k: get_english_score(k[0]))


def main():
    assert hamming_distance(b'this is a test', b'wokka wokka!!!') == 37
    with open("C6.txt") as input_file:
        data = b64decode(input_file.read())
    # print(data)
    result = break_repeating_key_xor(data)
    print("Key =", result[1].decode())
    print("---------------------------------------")
    print(result[0].decode().rstrip())


if __name__ == "__main__":
    main()