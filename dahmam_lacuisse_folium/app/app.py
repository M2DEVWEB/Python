import folium
import http.server
from sys import argv

from request import retrieve

map = folium.Map(location=[48.8534, 2.3488])

map_data = retrieve(argv[1])

for data in map_data:
  name = data['name']
  long = data['long']
  lat = data['lat']
  price = data['price']
  folium.Marker(
    location=[long, lat],
    icon=folium.DivIcon(html=f"""<div> <button onclick="alert('{price}')"> {name} </button> </div>""")
  ).add_to(map)

map.save('./map/index.html')

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler

print("Server running on port 8888")
server(('', 8888), handler).serve_forever()
