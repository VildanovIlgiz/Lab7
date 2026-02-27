import requests 
import json
import os

BASE_URL = "https://newsapi.org/v2/top-headlines"


class NewsAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.data = None

    def get_news(self, country="us", page_size=3):
        params = {
            "country": country,
            "pageSize": page_size,
            "apiKey": self.api_key
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            self.data = response.json()
        except requests.RequestException as e:
            print("Ошибка при получении данных:", e)
            self.data = None

    def print_news(self):
        if not self.data:
            print("Нет данных. Сначала вызовите get_news()")
            return

        if self.data.get("status") != "ok":
            print("Ошибка API:", self.data.get("message", "Неизвестная ошибка"))
            return

        articles = self.data.get("articles", [])

        for i, article in enumerate(articles, start=1):
            try:
                print(f"\nНовость № {i}")
                print("Источник  :", article["source"]["name"])
                print("Заголовок :", article["title"])
                print("Автор     :", article.get("author"))
                print("Дата      :", article["publishedAt"])
                print("Ссылка    :", article["url"])
                print("Описание  :", article.get("description"))
            except (KeyError, TypeError):
                print("Ошибка структуры данных — формат API мог измениться.")


if __name__ == "__main__":
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("Переменная окружения NEWS_API_KEY не установлена.")
    else:
        api = NewsAPI(api_key)
        api.get_news()
        api.print_news()