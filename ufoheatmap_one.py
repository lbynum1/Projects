import requests
from bs4 import BeautifulSoup

html = []
data = []
places = []
final = []
dic = {}

out = open("sight.txt", "w")

# page with all the url links
main = requests.get("http://www.nuforc.org/webreports/ndxevent.html")
print(main)

# get all the links on the main page by parsing through it
search = BeautifulSoup(main.text,"html.parser")
find = search.findAll("a")

for i in range(0, len(find)):
    destination = find[i]["href"]

    # every single link
    link = "http://www.nuforc.org/webreports/" + destination
    l = requests.get(link)

    # parsing through each link
    each = BeautifulSoup(l.text, "html.parser")

    for element in each.findAll("tr"):
        html.append([element.text])

for i in html[1:]:
    for element in i:
        data = element.split("\n")

    # this gets cities + states
        cities = data[2] + "," + data[3]
        places.append(cities)

# this counts the number of reports in each city and state
for i in range(1,len(places)):
    if places[i] in dic:
        dic[places[i]] += 1

    else:
        dic[places[i]] = 1

# this enables a tab between the reports and each city and state
for a,b in dic.items():
    out.write("{} \t {}" "\n".format(a,b))

out.close()
