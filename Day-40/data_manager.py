import requests
import os

sheet_endpoint = (os.environ['sheet_endpoint'])


class DataManager:

    def __init__(self):
        self.destination_data = {None}

    def get_destination_data(self):
        sheet_response = requests.get(sheet_endpoint)
        result = sheet_response.json()
        print(result)
        self.destination_data = result["flights"]
        return self.destination_data

    @staticmethod
    def update_destination_codes(data):
        sheet_inputs = {
            "flight": {
                "iataCode": data['iataCode'],
            }
        }
        requests.put(url=f'{sheet_endpoint}/{data["id"]}', json=sheet_inputs)




