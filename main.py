from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_sheet_endpoint = 'https://api.sheety.co/dc0d2beb892f08faeb450a08c2d3f55a/flightDeals/prices'

sheet_data = DataManager.get_data(flight_sheet_endpoint)

for entry in sheet_data:
    if entry['iataCode'] == '':
        entry['iataCode'] = FlightSearch.get_iata(entry['city'])

for entry in sheet_data:
    DataManager.change_sheet_row(f"{flight_sheet_endpoint}/{entry['id']}", entry['iataCode'])


for entry in sheet_data:
    FlightData.get_flights(entry['iataCode'])

pprint(sheet_data)
