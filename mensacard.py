from bs4 import BeautifulSoup
import requests
import json
import os
import readchar


def show():
    try:
        b = getbalance()    
    except:
          writefile(input("Enter your cardnumber: "))
    print(f"Dein Guthaben beträgt {getbalance()/100}€")
    print("Press 'c' to change your cardnumber or any other key to exit")
    k = readchar.readchar()
    if k == "c":
        writefile(input("Enter your cardnumber: "))
        show()


def getbalance():
    file = open("./buf.txt", "r")
    cardnumber = file.read()
    file.close()
    link = f'https://api.topup.klarna.com/api/v1/STW_MUNSTER/cards/{cardnumber}/balance'
    page = requests.get(link)
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    data = json.loads(soup)
    return data["balance"]
    

def writefile(number):
    file = open("./buf.txt", "w")
    file.write(str(number))
    file.close()    


def file_is_empty(path):
    return os.stat(path).st_size==0

file = open("./buf.txt", "w")
file.close()
show()