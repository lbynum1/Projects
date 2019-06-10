import requests
from bs4 import BeautifulSoup
import pickle
import time



location = []
places = []
dic = {}
final = []

out = open("bynum_lashawnda_cities.txt", "wb")

url = requests.get("http://www.nuforc.org/webreports/ndxevent.html")
soup = BeautifulSoup(url.text, "html.parser")
row = soup.findAll("a")


for i in range(1, len(row)):
    link = row[i]["href"]

    link_ = "http://www.nuforc.org/webreports/" + link
    url_2 = requests.get(link_)


    soup_2 = BeautifulSoup(url_2.text, "html.parser")
    # time.sleep(5)

    for record in soup_2.findAll('tr'):
        location.append([record.text])


for i in location[1:]:
    for element in i:
        data = element.split("\n")
        cities = data[2] + "," + data[3]
        places.append(cities)

for i in range(0, len(places)):
    if places[i] in dic:
        dic[places[i]] += 1

    else:
        dic[places[i]] = 1


for a,b in dic.items():
    string = a + " " + str(b)
    final.append(string)
fin = '\n'.join(final)


key = open("bynum_lashawnda_cities.txt", "rb")
pickle.dump(tb, out)
lock = pickle.load(key)
print(lock)

out.close()
