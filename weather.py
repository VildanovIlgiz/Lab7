import requests
import os
# 9983b0af3812b443d3236b58660d96f2 API


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class Weather:
    def __init__(self, api_key):
        self.key = api_key

    def get(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.key,
            "units": "metric",
            "lang": "ru"
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            print("Ошибка при получении данных от API:", e)
            return

        try:
            print("Город:", data["name"])
            print("Описание:", data["weather"][0]["description"])
            print("Температура:", data["main"]["temp"], "°C")
            print("Влажность:", data["main"]["humidity"], "%")
            print("Давление:", data["main"]["pressure"], "hPa")
        except (KeyError, IndexError, TypeError):
            print("Ошибка обработки данных: формат ответа API изменился.")


if __name__ == "__main__":
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("API-ключ не найден.")
    else:
        weather = Weather(api_key)
        weather.get(43.12, 5.30)