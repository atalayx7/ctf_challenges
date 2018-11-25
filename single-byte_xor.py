#!/usr/bin/env python

import pwn

with open('ciphertext.txt') as handle:
    cipher = handle.read()
    cipher = cipher.decode('base64')

    for i in range(256):
        message = pwn.xor(cipher, i)
        print message
