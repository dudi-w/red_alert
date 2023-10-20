from datetime import datetime, timedelta
import requests


class alertManager:
    def __init__(self, location: str = None, date_threshold: int = 10) -> None:
        self._custom_location = location
        self._date_threshold = date_threshold
        self._date_format = "%Y-%m-%d %H:%M:%S"
        self._lest_date = None
        self._lest_location = None
        self._src_url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json?_='

        self._headers = {
            'Referer': 'https://www.oref.org.il/11226-he/pakar.aspx',
            'X-Requested-With': 'XMLHttpRequest',
            'accept': 'application/json, text/javascript, /; q=0.01',
            'accept-language': 'en-US,en;q=0.9,he;q=0.8',
            'content-type': 'application/json; charset=utf-8',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        }

    def alerts_to_json(self):
        try:
            response = requests.get(self._src_url, headers=self._headers)
            response.raise_for_status()  # Check for any HTTP errors
            data = response.json()  # Parse the JSON data
            return data

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        except ValueError as e:
            print(f"Failed to parse JSON: {e}")

    def check_custom_location(self, location: str) -> bool:
            if not self._custom_location or self._custom_location == location:
                return True
            return False

    def check_date_threshold(self, date: str) -> bool:
        input_date = datetime.strptime(date, self._date_format)
        time_difference = datetime.now() - input_date
        threshold = timedelta(minutes=self._date_threshold)

        return True if time_difference <= threshold else False

    def look_for_new_alerts(self, data) -> (dict | None):
        if data and data[0]['alertDate'] != self._lest_date:
            new_alerts: dict = []
            i: int = 0
            while data[i]['alertDate'] != self._lest_date and i < len(data)-1:
                if self.check_custom_location(data[i]['data']) and self.check_date_threshold(data[i]['alertDate']):
                    new_alerts.append(data[i])
                i = i+1
            self._lest_date = data[0]['alertDate']
            self._lest_location = data[0]['data']
            return new_alerts
        else:
            return None
