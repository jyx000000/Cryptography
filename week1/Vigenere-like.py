def hex_decode(hexString):
    return [int(hexString[i:i + 2], 16) for i in range(0, len(hexString), 2)]


def howManySpaces(isSpace):
    spaces = 0
    for each in isSpace:
        if each:
            spaces += 1
    return spaces


if __name__ == '__main__':
    string = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"
    hexDecoded = hex_decode(string)
    punctuations = "., !();"
    lowercase = [chr(ord('a') + i) for i in range(0, 26)]
    uppercase = [chr(ord('A') + i) for i in range(0, 26)]
    spaced = [0x63 ^ ord(each) for each in list(punctuations) + lowercase + uppercase]

    for length in range(1, 14):
        blk = [hexDecoded[i * length:(i + 1) * length] for i in range(0, len(hexDecoded) // length)]
        isSpace = [False for i in range(len(blk) * len(blk[0]))]
        for idx, xx in enumerate(blk):
            xored = []
            for yy in blk:
                xored.append([xx[i] ^ yy[i] for i in range(len(blk[0]))])
            for i in range(len(blk[0])):
                for j in range(len(blk)):
                    if xored[j][i] not in spaced:
                        break
                else:
                    isSpace[idx * len(blk[0]) + i] = True
        print("There are %d spaces when key length is %d" % (howManySpaces(isSpace), length))
        index = [i for i in range(len(isSpace)) if isSpace[i] == True]
        if howManySpaces(isSpace) != 0:
            # Finding key
            key = [0x00 for i in range(length)]
            for idx, each in enumerate(isSpace):
                if each:
                    tmp = key[idx % length]
                    new = hexDecoded[idx] ^ 0x63
                    if tmp == 0x00:
                        key[idx % length] = new
                    elif new != tmp:
                        break
                    else:
                        pass
            else:
                print("Corresponding key is:" + ''.join(["%02x" % each for each in key]))

    plain = ''
    for idx, each in enumerate(hexDecoded):
        plain += chr(key[idx % len(key)] ^ each)

    print(plain)