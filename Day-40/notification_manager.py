from twilio.rest import Client
import os

TWILIO_AUTH = (os.environ['TWILIO_AUTH'])
TWILIO_SID = (os.environ['TWILIO_SID'])


class NotificationManager:

    @staticmethod
    def send_message(data):
        client = Client(TWILIO_SID, TWILIO_AUTH)
        text = f'Low price alert! Only £{data["price"]} to fly from {data["cityFrom"]}-{data["cityCodeFrom"]} to ' \
               f'{data["cityTo"]}-{data["cityCodeTo"]}, from {data["local_departure"].split("T")[0]} to ' \
               f'{data["local_departure"].split("T")[0]}'
        message = client.messages.create(
            body=text,
            from_='+19707158568',
            to='+5581982139440',
        )
        if data.stop_overs > 0:
            message += f"\nFlight has {data.stop_overs} stop over, via {data.via_city}."
