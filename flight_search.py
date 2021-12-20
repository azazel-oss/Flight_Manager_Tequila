import requests

tequila_endpoint = 'https://tequila-api.kiwi.com/locations/query'


class FlightSearch:
    @staticmethod
    def get_iata(city_name):
        tequila_header = {
            "apikey": '90YWyDfUP9OvPMsxSbVH_sPe1XQMPYgP',
            "accept": "application/json"
        }

        tequila_params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"
        }

        response = requests.get(tequila_endpoint, params=tequila_params, headers=tequila_header)
        iata_code = response.json()['locations'][0]['code']
        print(iata_code)
        return iata_code
