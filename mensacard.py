from bs4 import BeautifulSoup
import requests
import json
import os


import os

def file_is_empty(path):
    return os.stat(path).st_size==0

file = open("./buf.txt", "w")
file.close()

if file_is_empty("./buf.txt"):
    file = open("./buf.txt", "w")
    file.write(input("Please enter your Card-ID from STW-Muenster: (eg.123456)"))
    file.close()




file = open("./buf.txt", "r")
cardnumber = file.read()
file.close()
link = f'https://api.topup.klarna.com/api/v1/STW_MUNSTER/cards/{cardnumber}/balance'
page = requests.get(link)
soup = str(BeautifulSoup(page.content, 'html.parser'))
data = json.loads(soup)

balance = data["balance"]
print(f"Dein Guthaben beträgt {balance/100}€")