import requests
import os

tequila_endpoint = 'https://tequila-api.kiwi.com/locations/query'
tequila_search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
tequila_api = {
    'apikey': (os.environ['apikey'])
}


class FlightData:
    @staticmethod
    def get_flight_data(data):
        flight_inputs = {
            "fly_from": 'LON',
            'fly_to': f'{data["iataCode"]}',
            'date_from': '13/07/2022',
            'date_to': '13/01/2023',
            'return_from': '13/07/2022',
            'return_to': '13/03/2023',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'max_fly_duration': 48,
            'flight_type': 'round',
            'adults': 1,
            'children': 0,
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            'max_stopovers': 0,
            'max_sector_stopovers': 0,
            'sort': 'price',
            'limit': 1,
            'curr': 'GBP',
        }

        try:
            flight_response = requests.get(url=tequila_search_endpoint, params=flight_inputs, headers=tequila_api)
            flight_result = flight_response.json()
            print(flight_result)
            lowest_price = flight_result['data'][0]
        except IndexError:
            flight_inputs["max_stopovers"] = 1
            flight_response = requests.get(url=tequila_search_endpoint, params=flight_inputs, headers=tequila_api)
            flight_result = flight_response.json()
            print(flight_result)
            lowest_price_stop = flight_result['data'][0]
            return lowest_price_stop

        return lowest_price
