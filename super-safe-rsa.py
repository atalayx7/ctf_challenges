#!usr/bin/env/python
from pwn import *
import codecs
from Crypto.Util.number import inverse
#nc 2018shell2.picoctf.com 59208

c = 7139480764559358032170871091979779839905488768665991981290004480567051962663165
n = 10640772830271567467642118805790498703160706264449113232923118618229013808830763
e = 65537

#factoring the n: http://factordb.com/    
p = 97498147872251080024548827612711861489
q = 109138204801734852021223472903536420399067

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)  # plaintext

print(unhex(hex(m)[2:]).decode('utf-8'))
#print(codecs.decode(hex(m)[2:], "hex").decode('utf-8'))
