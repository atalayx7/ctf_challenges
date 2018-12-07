#!/usr/bin/env python
x = '58186778266652'
oddN = 0
for i in range(0, 14, 2):
    oddN += int(x[i])


total = 0
for i in range(1, 14, 2):
    evenN = 0
    evenN = 2 * int(x[i])
    if evenN < 100:
        total += evenN % 10
        evenN /= 10
        total += evenN
if ((oddN + total) % 10) == 0:
    result += 0
else:
    result = 10 - ((oddN + total) % 10)
print '15th digit:', result
