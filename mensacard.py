from bs4 import BeautifulSoup
import requests
import json
import os
import readchar


def getbalance(cardnumber):
    link = f'https://api.topup.klarna.com/api/v1/STW_MUNSTER/cards/{cardnumber}/balance'
    page = requests.get(link)
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    data = json.loads(soup)
    try:
        return data["balance"]
    except: 
        writefile(input("Enter your cardnumber: "))

    

def file_is_empty(path):
    return os.stat(path).st_size==0

file = open("./buf.txt", "r")
file.close()

def writefile(number):
    file = open("./buf.txt", "w")
    file.write(str(number))
    file.close()

if file_is_empty("./buf.txt"):
    writefile(input("Enter your cardnumber: "))
    



def show():
    file = open("./buf.txt", "r")
    cardnumber = file.read()
    file.close()
    try:
        print(f"Dein Guthaben beträgt {getbalance(cardnumber)/100}€")
    except:
          writefile(input("Enter your cardnumber: "))
    print("Press 'c' to change your cardnumber or any other key to exit")
    k = readchar.readchar()
    if k == "c":
        writefile(input("Enter your cardnumber: "))
        show()
show()