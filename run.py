import requests
import csv
mylist = []

with open('addresses.csv', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

myfile = open('results.txt', 'w')

for i in range(0,len(mylist)):
    address = mylist[i]
    link = f"https://blockchain.info/q/pubkeyaddr/{address}"
    f = requests.get(link)
    if(f.text == ''):
        pass
    else:
        myfile.write("%s\n" % f.text)
        print(f.text)

myfile.close()
