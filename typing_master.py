#!/usr/bin/python

from pwn import *
import re

context.log_level = 'critical'

host = ""
port = 9999

s = remote(host, port)
prompt = s.recv()

numbers = re.findall(r"'(\w)' (\d+)", prompt)

string = []
string.append(number[0][0] * number[0][1])
string.append(number[1][0] * number[1][1])
string.append(str(ord(number[0][0]) + ord(number[0][1])))

answer = ''.join(string)
s.sendline(answer)
print s.recv()
s.close()
