from twilio.rest import Client

account_sid = 'AC9e5950b7340450514dd89e85552031a6'
auth_token = 'faa3399bd8e9d0e262d35848633a57b9'
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/9d7dfe2286aa4bc0831907c596b0202d/myFightDeals/prices'

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'FhDyA3MaUFy4uSpRGlEohmCS1_AB-RaA'

class NotificationManager:

    def send_message(self, from_city, to_city, price, link, from_date, to_date, stop_overs=0, via_city=""):
        """Method that sends a message with flight information"""
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f'Low price alert! Only ${price} to fly '
                                              f'from {from_city} to {to_city}, from '
                                              f'{from_date} to {to_date}\n{link}',
                                         from_='+14159385765',
                                         to='+14246751559')
        print(message.status)

