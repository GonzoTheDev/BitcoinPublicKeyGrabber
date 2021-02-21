import requests
import csv
mylist = []

with open('addresses.csv', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

for i in range(0,len(mylist)):
    address = mylist[i]
    link = f"https://blockchain.info/q/pubkeyaddr/{address}"
    f = requests.get(link)
    print(f.text)
