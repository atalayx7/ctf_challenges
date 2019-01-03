import base64


def challenge_one(hex):
    b16 = bytes.fromhex(hex)
    b64 = base64.b64encode(b16)
    decoding = base64.b64decode(b64)
    #print(decoding.decode('utf-8'))
    return(b64.decode('utf-8'))
print(challenge_one('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
