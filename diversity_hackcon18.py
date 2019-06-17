with open('diversity.txt') as fh:
    fh = fh.read().split()
text = ""
for i in fh:
    if i[0] == 'b':
        text += chr(int(i[1:], 2))

    elif i[0] == 'o':
        text += chr(int(i[1:], 8))

    elif i[0] == 'd':
        text += chr(int(i[1:]))

    elif i[0] == 'x':
        text += chr(int(i[1:], 16))

print(text)
