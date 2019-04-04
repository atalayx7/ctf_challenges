
def xor(data, key):

    l = len(key)
    decoded = ""
    for i in range(0, len(data)):
        decoded += chr(ord(data[i]) ^ ord(key[i % l]))
    return decoded
print xor('mydata', '2')
