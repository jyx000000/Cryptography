from C3 import force, pretty_print_result

def detect_encrypted_text(encrypted_strings):
    candidates = []

    for string in encrypted_strings:
        candidates.append(force(string))

    print(candidates)
    return sorted(candidates, key=lambda c: c['score'], reverse=True)[0]


def main():
    ciphertexts = [bytes.fromhex(line.strip()) for line in open("C4.txt")]
    most_likely_plaintext = detect_encrypted_text(ciphertexts)
    pretty_print_result(most_likely_plaintext)

    assert most_likely_plaintext['plaintext'].rstrip() == b"Now that the party is jumping"  #检查

if __name__ == "__main__":
    main()