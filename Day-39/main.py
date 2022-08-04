# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
destination_data = data_manager.get_destination_data()
flight_data = FlightData()
notification_manager = NotificationManager()

for data in destination_data:
    if data['iataCode'] == '':
        response = flight_search.get_destination_code(data)
        data['iataCode'] = response
        data_manager.update_destination_codes(data)
    price_data = flight_data.get_flight_data(data)
    # print(f'{data["city"]}: £{price_data["price"]}')
    if data['lowestPrice'] >= price_data["price"]:
        notification_manager.send_message(price_data)

