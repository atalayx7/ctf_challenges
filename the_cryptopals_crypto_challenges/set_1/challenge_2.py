import pwn


def challenge_two(arg1, arg2):

    return pwn.xor(arg1, arg2)

arg1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
arg2 = bytes.fromhex('686974207468652062756c6c277320657965')
print(challenge_two(arg1, arg2).hex())

#print (bytes.fromhex('746865206b696420646f6e277420706c6179').decode('utf-8'))
