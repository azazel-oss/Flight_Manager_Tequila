import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    @staticmethod
    def get_data(url):
        response = requests.get(url)
        return response.json()['prices']

    @staticmethod
    def change_sheet_row(url, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url, json=body)
        print(response.text)
