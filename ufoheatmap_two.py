import requests

places = []
again = []

file = open("sight.txt", "r")

feel = open("sight_new.txt", "w")

for a in file:
    places.append(a)

for a in places:
    slice = a.split("\t")
    location = slice[0]
    again.append(slice)

for i in range(0,len(again)):
    url = "http://open.mapquestapi.com/geocoding/v1/address?outFormat=CSV&key=cjRJU8XSER3dlEqkGkA4OnfGJdD430OA" + "&location=" + again[i][0]
    data = requests.get(url)

    for line in data.text.splitlines()[1:]:
        d = line.split(",")
        lat = d[6]
        la = lat.replace('"', '')

        lon = d[7]
        lo = lon.replace('"', '')

        print(again[i][0] + "\n"+ "Lat:" + lat + "," + "Lon:" + lon + "\n")
        feel.write(again[i][0] + "\n"+ "Lat:" + lat + "," + "Lon:" + lon + "\n")


file.close()
feel.close()
