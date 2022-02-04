import requests
import time

mylist = []

with open('addresses.csv', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

myfile = open('results.txt', 'w')

print("\n\n########################################################\nPlease be aware there is a 10 second timeout per request \nto blockchain.info to prevent API being blocked.\n########################################################\n\n")

for i in range(0,len(mylist)):
    address = mylist[i]
    link = f"https://blockchain.info/q/pubkeyaddr/{address}"
    f = requests.get(link)
    if(f.text == ''):
        pass
    else:
        myfile.write("%s\n" % f.text)
        print(f.text)
        time.sleep(10)

myfile.close()
