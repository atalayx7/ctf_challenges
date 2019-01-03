import pwn
import string


def challenge_three(arg1):
    arg1 = bytes.fromhex(arg1)
    for i in string.ascii_letters:
        solution = pwn.xor(arg1, i)
        if b' ' in solution:
            print(solution.decode('utf-8'))

print(challenge_three(
    '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))
