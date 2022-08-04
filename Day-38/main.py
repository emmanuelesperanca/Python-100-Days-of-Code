import requests
from datetime import datetime
import os

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheets_endpoint = os.environ.get('sheets_endpoint')
sheety_header = {
    'Authorization': os.environ.get('Authorization')
}
headers = {
    'x-app-id': os.environ.get('x-app-id'),
    'x-app-key': os.environ.get('x-app-key'),
    'x-remote-user-id': '0',
}

exercise_text = input("Tell me which exercises you did: ")

exercise_config = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 63,
    "height_cm": 175,
    "age": 26
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
result = response.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "página1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheets_endpoint, json=sheet_inputs, headers=sheety_header)


