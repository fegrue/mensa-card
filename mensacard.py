from bs4 import BeautifulSoup
import requests
import json
import os


print()

file = open("buf.txt", "w+")
if file.read() == "":
    newcardid = input("Please enter your Card-ID from STW-Muenster: (eg.123456)")
    file.write(newcardid)





cardnumber = file.read()
file.close()
link = f'https://api.topup.klarna.com/api/v1/STW_MUNSTER/cards/{cardnumber}/balance'
page = requests.get(link)
soup = str(BeautifulSoup(page.content, 'html.parser'))
#soupstr = str(soup)
data = json.loads(soup)

balance = data["balance"]
print(f"Dein Guthaben beträgt {balance/100}€")