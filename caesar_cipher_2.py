#!usr/bin/env python
content = "PICO#4&[C!ESA2?#I0H%R3?JU34?A2%N4?S%C5R%]"
for i in range(255):
    text = []
    for j in content:
        text += (chr((ord(j) + i) % 255))
        text = "".join(text)
    if 'picoCTF' in text:
        print text
