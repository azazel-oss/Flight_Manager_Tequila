import requests
import datetime as dt

tequila_search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
today = dt.datetime.today()


class FlightData:
    @staticmethod
    def get_flights(city_code):
        tequila_header = {
            "apikey": '90YWyDfUP9OvPMsxSbVH_sPe1XQMPYgP',
            "accept": "application/json"
        }
        tequila_parameters = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": (today + dt.timedelta(days=1)).strftime('%d/%m/%Y'),
            "date_to": (today + dt.timedelta(days=180)).strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'GBP',
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
        }
        response = requests.get(tequila_search_endpoint, params=tequila_parameters, headers=tequila_header)
        print(response.json())
