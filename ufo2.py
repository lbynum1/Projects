import requests


# list that will hold all sightings and number of observations
places = []
sights = []

# opens the file that contains the sightings and number of observations
data = open("sight.txt", "r")

#Where lagnitudes and lonitudes will be
lalon = open("sightlatlon.txt", "w")


for a in data:
    places.append(a)

for a in places:
    slice = a.split("\t")
    location = slice[0]
    obser = slice[1]

    key = 'hhQeceUHKeMjesP0PI4tTh0AmwDTT4DW'
    url = 'http://www.mapquestapi.com/geocoding/v1/address?outFormat=csv&key=' + key + '&location=' + location.replace(" ", "")
    results = requests.get(url)

    for line in results.text.splitlines()[1:]:
            d = line.split(",")
            lat = d[6]
            la = lat.replace('"', '')

            lon = d[7]
            lo = lon.replace('"', '')

            print("Lat:" + la + "," + "Lon:" + lo + "," + " " + location + " " + obser)
            lalon.write("Lat:" + la + "," + "Lon:" + lo + "," + " "+ location + " " + obser)


data.close()
lalon.close()