#!/usr/bin/env python
"""
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. 
Can you get the flag from this program to prove you are on the way to becoming 1337? 
Connect with nc 2019shell1.picoctf.com 31615.
"""
from pwn import *
import re
sh = remote('2019shell1.picoctf.com', 31615)
binary = sh.recvuntil(' as a word.').strip()
binarytext = re.sub("\s\s+", " ", binary.decode())
y = binarytext.split('the ')[1].split(' as')[0]
z = []
z += y.split(' ')
final = []

for i in z:
    final.append(chr(int(i, 2)))
sh.recvuntil('Input:')
sh.sendline("".join(final))
octal = sh.recvuntil(' as a word.').strip()
octaltext = re.sub("\s\s+", " ", octal.decode())
y2 = octaltext.split('the ')[1].split(' as')[0]

z2 = []
z2 += y2.split(' ')
final2 = []

for i in z2:
    final2.append(chr(int(i, 8)))
sh.recvuntil('Input:')
sh.sendline("".join(final2))

hexi = sh.recvuntil(' as a word.').strip()
hextext = re.sub("\s\s+", " ", hexi.decode())
y2 = hextext.split('the ')[1].split(' as')[0]

thetext = bytearray.fromhex(y2).decode()
sh.recvuntil('Input:')
sh.sendline(thetext)

sh.interactive()
