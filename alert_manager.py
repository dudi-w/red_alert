from datetime import datetime, timedelta
import requests

class AlertDataFetcher:
    _src_url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json?_='
    _headers = {
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

    @staticmethod
    def fetch_alerts() -> list[dict]:
        try:
            response = requests.get(AlertDataFetcher._src_url, headers=AlertDataFetcher._headers)
            response.raise_for_status()  # Check for any HTTP errors
            data = response.json()  # Parse the JSON data
            return data

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

        except ValueError as e:
            print(f"Failed to parse JSON: {e}")

class AlertManager:
    def __init__(self, location: str = None, date_threshold: int = 10) -> None:
        self._custom_location = location
        self._date_threshold = date_threshold
        self._date_format = "%Y-%m-%d %H:%M:%S"
        self._last_date = None
        self._last_location = None

    def _check_custom_location(self, location: str) -> bool:
            if not self._custom_location or self._custom_location == location:
                return True
            return False

    def _check_date_threshold(self, date: str) -> bool:
        input_date = datetime.strptime(date, self._date_format)
        time_difference = datetime.now() - input_date
        threshold = timedelta(minutes=self._date_threshold)

        return time_difference <= threshold

    def look_for_new_alerts(self) -> list[dict]:
        alerts = AlertDataFetcher.fetch_alerts()        
        new_alerts = []
        if alerts and alerts[0]['alertDate'] != self._last_date:
            i = 0
            while i < len(alerts) and alerts[i]['alertDate'] != self._last_date:
                if self._check_custom_location(alerts[i]['data']) and self._check_date_threshold(alerts[i]['alertDate']):
                    new_alerts.append(alerts[i])
                i += 1
            self._last_date = alerts[0]['alertDate']
            self._last_location = alerts[0]['data']

        return new_alerts
