import requests
import re

url = 'https://atalaysblog.wordpress.com/'

session = requests.Session()
response = session.get(url)

content = response.text

print(content)
