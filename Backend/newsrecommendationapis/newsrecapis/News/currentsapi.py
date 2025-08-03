import requests

class CurrentsapiAPI:
    def get_news(self, page):
        base_url = f"https://api.currentsapi.services/v1/latest-news?&language=us&apiKey="
        response = requests.get(base_url)
        response.raise_for_status() 
        data = response.json()
        return base_url
