import requests
import os

tequila_endpoint = 'https://tequila-api.kiwi.com/locations/query'
tequila_search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
tequila_api = {
    'apikey': (os.environ['apikey'])
}


class FlightSearch:
    @staticmethod
    def get_destination_code(data):
        tequila_inputs = {
            "term": data['city'],
            'locale': 'en_US',
            'location_types': 'city',
            'limit': 1,
            'active_only': True
        }
        city_response = requests.get(url=tequila_endpoint, params=tequila_inputs, headers=tequila_api)
        city_result = city_response.json()
        iata_code = city_result['locations'][0]['code']

        return iata_code
