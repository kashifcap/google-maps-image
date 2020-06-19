import requests

api_key = "Api-key"

center = "Delhi"

zoom = 10

url = f"https://maps.googleapis.com/maps/api/staticmap?center={center}&zoom={str(zoom)}&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key={api_key}"

try:
    response = requests.get(url)    
except:
    print("some error occured")

f = open("file loaction", 'wb')

print(type(response.content))
f.write(response.content)

f.close()

