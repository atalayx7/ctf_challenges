#!/usr/bin/env python
from scapy.all import *
"""
We found this packet capture. Recover the flag. 
You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.
"""
a = rdpcap('capture.pcap')
flag = []
for i in a[UDP]:
    try:
        if i[IP].src == '10.0.0.2' and i[IP].dst == '10.0.0.12':
            flag.append((i[Raw].load).decode())
    except IndexError:
        continue
print("".join(flag))
