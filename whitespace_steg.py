import re

h = open('file.txt')
c = [x[:-1] for x in h.readlines()]
h.close()
flag = []
for line in c:
    num = (re.findall(r"(\s+)", line))  # finds any multiple white spaces
    if num:
        # replace whitespaces with 1
        num = (int(''.join(num).replace(' ', '1').replace('\t', '0')), 2)
        # int (,2) binarye çevir
        if num in range(255):
            flag.append(chr(num))

print(''.join(flag))
