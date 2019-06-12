import requests
import xml.etree.ElementTree

key = []
inside = []

box = open("sight.txt","r")
elements= box.readlines()

print(elements)

for a in elements:
    key.append(a.split("\n"))


box = open("sightlatlon.txt","w")
box.write(str(key))

measures = open("heatmap.html", "w")
measures.write(""" <html>
  <head>
    <script src="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.js"></script>
    <link type="text/css" rel="stylesheet" href="https://api.mqcdn.com/sdk/mapquest-js/v1.3.2/mapquest.css"/>
    <script src="https://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
    <script src=".js"></script>

    <script type="text/javascript">
      window.onload = function() {
        L.mapquest.key = 'lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24';
        var baseLayer = L.mapquest.tileLayer('map');

        var map = L.mapquest.map('map', {
          center: [-37.87, 175.475],
          layers: baseLayer,
          zoom: 12
        });

        addressPoints = addressPoints.map(function (addressPoint) { return [addressPoint[0], addressPoint[1]]; });

        L.heatLayer(addressPoints).addTo(map);
      }
    </script>
  </head>

  <body style="border: 0; margin: 0;">
    <div id="map" style="width: 100%; height: 530px;"></div>
  </body>
</html>""")

measures.close()

