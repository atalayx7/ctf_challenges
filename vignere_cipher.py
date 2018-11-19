from string import uppercase
message = "IjgJUO{P_LOUV_AIRUS_GYQUTOLTD_SKRFB_TWNKCFT}"
numbers = '07271978'
new_message = ""
counter = 0
for i in message:
    if i.upper() in uppercase:
        new_message += uppercase[(uppercase.index(i.upper()) -
                                  int(numbers[counter])) % len(uppercase)]
        counter += 1
    else:
        new_message += i
    if counter == 8:
        counter = 0
print new_message
