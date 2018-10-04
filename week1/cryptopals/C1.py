import binascii
import base64

def change(s):
    decoded = binascii.unhexlify(s)
    print(decoded)                          #正常字符串
    return base64.b64encode(decoded).decode('ascii')

x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expectedY = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
y = change(x)
print(y)

if y != expectedY:
    raise Exception(y + ' != ' + expectedY)