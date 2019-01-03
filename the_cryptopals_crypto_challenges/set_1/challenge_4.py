import pwn
import string

with open('challenge_4_data.txt') as fh:
    fh = fh.readlines()
    fh[:] = [bytes.fromhex(line.rstrip('\n')) for line in fh]
    for i in fh:
        for j in range(255):
            solution = pwn.xor(i, j)
            if b' the ' in solution:
                print(solution.decode('utf-8', errors='ignore'))
