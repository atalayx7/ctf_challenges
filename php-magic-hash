from hashlib import md5

i = 0
while True:
    plaintext = '0e%d' % i
    m = md5()
    m.update(bytes(plaintext, "ascii"))
    hash = m.hexdigest()
    # print(h)

    if hash.startswith('0e'):
        if hash[2:].isdigit():
            print(plaintext, hash)
            break # you may continue
    # print(plaintext,h)
    i += 1
