from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()  # Info about flights from Google Sheet
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LAX"

# This code will find the IATA code for the city if the IATA code column from Google Sheet
# is empty.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    # Checks if there is a flight
    flight = flight_search.check_flights(
        destination_city=destination['city'],
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)


# If the program can't find a flight price it will show and Attribute Error
    try:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_message(
                from_city='Los Angeles',
                to_city=flight.destination_city,
                price=flight.price,
                link='',
                from_date=flight.out_data,
                to_date=flight.return_date)
    except AttributeError:
        pass

