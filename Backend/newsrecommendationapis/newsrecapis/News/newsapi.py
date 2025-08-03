import requests

class NewsAPI:
    NEWS_API_KEY = ""
    def __init__(self):
        self.NEWS_API_KEY = ""

    def get_news(self):
        extracted_data_list = []
        base_url = f"https://newsapi.org/v2/everything?q=currents&sortBy=publishedAt&apiKey=&language=en"
        response = requests.get(base_url)
        response.raise_for_status() 
        data = response.json()
        articles = data.get('articles', [])
        if articles:
            for article in articles:
                extracted_data = {
                "title": article.get("title"),
                "source_name": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "url_to_image": article.get("urlToImage"),
                "content": article.get("content"),
                "description": article.get("description")}

                extracted_data_list.append(extracted_data)
        return extracted_data_list
