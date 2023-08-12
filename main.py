import requests
from datetime import datetime

API_ENDPOINT = "https://api.sunrise-sunset.org/json"
LONDON_LATITUDE = 51.509865
LONDON_LONGITUDE = -0.118092
TWENTY_HOUR_FORMAT = 0

parameters = {
    "lat": LONDON_LATITUDE,
    "lng": 	LONDON_LONGITUDE,
    "formatted": TWENTY_HOUR_FORMAT
}


response = requests.get(url=API_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise_data = data["results"]["sunrise"]
print(sunrise_data.split("T")[1].split(":")[0])
sunset_data = data["results"]["sunset"]
print(sunset_data.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)


"""

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response.raise_for_status())
data = response.json()
print(data)

iss_position_data = response.json()["iss_position"]
print(iss_position_data)

iss_latitude_data = response.json()["iss_position"]["latitude"]
iss_longitude_data = response.json()["iss_position"]["longitude"]

iss_latitude_longitude_position = (iss_latitude_data, iss_longitude_data)
print(iss_latitude_longitude_position)


"""