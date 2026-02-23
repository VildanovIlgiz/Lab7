import requests 
import json
#5886b96f6755446594793226bdc69eec API


class NewsAPI:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://newsapi.org/v2/top-headlines"
        self.data = None

    def get_news(self):
        url = self.url
        params = {
            "country": "us",
            "q": "Trump",
            "pageSize": 3,
            "apiKey": self.api_key
        }

        response = requests.get(url, params=params)
        self.data = response.json()

    def print_news(self):
        data = self.data
        
        if not data:
            print("Нет данных для отображения. Сначала вызовите get_news()")
            return
        
        if data.get("status") != "ok":
            print("Ошибка API:", data)
            return
        for i in range(len(data["articles"])):
            article = data["articles"][i]
            print(f"Новость № {i+1}")
            print("Источник  :", article["source"]["name"])
            print("Заголовок :", article["title"])
            print("Автор     :", article["author"])
            print("Дата      :", article["publishedAt"])
            print("Ссылка    :", article["url"])
            print("Описание  :", article["description"])

api = NewsAPI("5886b96f6755446594793226bdc69eec")
data = api.get_news()
api.print_news()