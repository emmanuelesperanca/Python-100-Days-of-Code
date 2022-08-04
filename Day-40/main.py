# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import flight_club

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
    print(f'{data["city"]}: £{price_data["price"]}')
    try:
        if data['lowestPrice'] >= price_data["price"]:
            message = notification_manager.send_message(price_data)
            users = flight_club.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            price = data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport = data["route"][0]["flyFrom"],
            destination_city = data["route"][1]["cityTo"],
            destination_airport = data["route"][1]["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][2]["local_departure"].split("T")[0],
            stop_overs = 1,
            via_city = data["route"][0]["cityTo"]
            link = f'https://www.google.co.uk/flights?hl=en#flt={data["route"][0]["flyFrom"]}.{data["route"][1]["flyTo"]}.' \
                   f'{data["route"][0]["cityFrom"]}*{data["route"][1]["flyTo"]}.{data["route"][0]["flyFrom"]}.' \
                   f'{data["route"][2]["local_departure"].split("T")[0]}'
            flight_club.send_emails(emails, message, link)

    except TypeError:
        continue

# flight_club.join_club()
