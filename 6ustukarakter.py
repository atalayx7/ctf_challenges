#!/usr/bin/env python
from hashlib import md5, sha1
import random
x = random.randint(100000, 999999)

x_md5 = (md5(str(x).encode('utf-8')).hexdigest())

x_sha1 = sha1(str(x_md5).encode('utf-8')).hexdigest()
print("The random number is", x)
print("The md5 value of", x, ":", x_md5)
print("The sha1 value of ", x_md5, ":", x_sha1)
print("The first 6 characters of", x_sha1, ":", x_sha1[:6])

print("...")

first6 = x_sha1[:6]

for i in range(100000, 999999):
    i_md5 = md5(str(i).encode('utf-8')).hexdigest()
    i_sha1 = sha1(str(i_md5).encode('utf-8')).hexdigest()
    i_first6 = i_sha1[:6]
    if i_first6 == first6:
        print("We successfully got the result:", i_first6)
        break
