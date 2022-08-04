import requests
import json
import os
from twilio.rest import Client

apikey = (os.environ['apikey'])
lon = 54
lat = 21
units = 'metric'
TWILIO_SID = (os.environ['twilio_sid'])
TWILIO_AUTH = (os.environ['twilio_auth'])

params = {
    'lat': lat,
    'lon': lon,
    'appid': apikey,
    'exclude': "current,minutely,daily",
    'units': units,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()

with open("weather.json", "w") as file:
    json.dump(data, file, indent=2)

will_rain = False

hourly_forecast = data["hourly"][:12]

for hour in hourly_forecast:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
            body='It is going to rain today. Remember to bring an umbrella',
            from_=(os.environ['twilio_number']),
            to=(os.environ['my_number']),
        )
