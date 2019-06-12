import requests

places = []
again = []
all = []

file = open("sight.txt", "r")

lalon = open("sightlatlon.txt", "w")

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

        print("Lat:" + la + "," + "Lon:" + lo + "\n" + again[i][1])
        lalon.write("Lat:" + la + "," + "Lon:" + lo + "\n" + again[i][1])


file.close()
lalon.close()
