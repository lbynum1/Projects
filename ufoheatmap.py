import requests
from bs4 import BeautifulSoup
import pickle
import time



location = []
places = []
dic = {}
final = []

# open the file for dictionary
data = open("bynum_lashawnda_cities.txt", "wb")

# page with all url links
main = requests.get("http://www.nuforc.org/webreports/ndxevent.html")

# get all the links on the main page by parsing through it
soup = BeautifulSoup(main.text, "html.parser")
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

# this gets the cities and states
        cities = data[2] + "," + data[3]
        places.append(cities)

# this counts the number of reports in each city and state
for i in range(0, len(places)):
    if places[i] in dic:
        dic[places[i]] += 1
    else:
        dic[places[i]] = 1

# this enables a tab between the reports and each city and state
for a,b in dic.items():
    string = a + " " + str(b)
    final.append(string)
each = '\n'.join(final)


pin = open("bynum_lashawnda_cities.txt", "rb")
pickle.dump(each, out)
fin = pickle.load(pin)
print(fin)

out.close()
