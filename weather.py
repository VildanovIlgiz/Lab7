import requests


class Weather:
    def __init__(self, api_key):
        self.key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather"

    def get(self, lat, lon):
        prms= {
            "lat": lat,
            "lon": lon,
            "appid": self.key,
            "units": "metric",
            "lang": "ru"
        }

        r = requests.get(self.url, prms)
        data = r.json()

        if r.status_code != 200:
            print("Ошибка API:", data)
            return

        print("Город:", data["name"])
        print("Описание:", data["weather"][0]["description"])
        print("Температура:", data["main"]["temp"], "°C")
        print("Влажность:", data["main"]["humidity"], "%")
        print("Давление:", data["main"]["pressure"], "hPa")


if __name__ == "__main__":
    weather = Weather("9983b0af3812b443d3236b58660d96f2")
    weather.get(43.12, 5.30)