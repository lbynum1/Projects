import requests
import pickle

final_2 = []

cities = open("bynum_lashawnda_cities.txt", "r")
num = 0

for a in cities:
    items = a.split(" ")

    key = "cjRJU8XSER3dlEqkGkA4OnfGJdD430OA"
    location = items[0]

    url = "http://open.mapquestapi.com/geocoding/v1/address?outFormat=CSV&key=" + key + "&location=" + location
    data = requests.get(url)
    # print(data.text)

    for line in data.text.splitlines():
        if num == 1:
           d = line.split(",")
           lat = d[6]
           lat = lat.replace('"', '')
           lon = d[7]
           lon = lon.replace('"', '')
           print(a + "\n" + "Lat:" + lat + "," + "Lon:" + lon + "\n")

       num = num + 1

cities.close()
