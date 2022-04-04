import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/9d7dfe2286aa4bc0831907c596b0202d/myFightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}  # Stores data from Google Sheets

    def get_destination_data(self):
        """Method that requests all information from Google Sheets"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Method that updates the destination codes"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
