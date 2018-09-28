def hex_xor(data1, data2):
    dec1 = int(data1, 16)    #缓冲区
    dec2 = int(data2, 16)
    xor = dec1 ^ dec2
    return hex(xor)[2:]

def main():
    y = hex_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    # y = hex_xor("Burning 'em, if you ain't quick and nimble", "686974207468652062756c6c277320657965")
    print(y)
    expectedY="746865206b696420646f6e277420706c6179"
    if y != expectedY:
        raise Exception(y + ' != ' + expectedY)

if __name__ == '__main__':
    main()