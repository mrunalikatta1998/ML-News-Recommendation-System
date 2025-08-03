from newsrecapis.News.newsapi import NewsAPI
from newsrecapis.News.marketaux import MarketauxAPI
import pandas as pd

def get_registered_api_urls():
    print("get_registered_api_urls")
    return [NewsAPI()]

def fetch_news_article():
        api_urls = get_registered_api_urls()
        print('Fetched Api urls', api_urls)
        api_response_objects = []
        for api_url in api_urls:
             try:
        #         logging.info(f"Fetching data from API: {api_url}")
                 response = api_url.get_news()
                 api_response_objects.extend(response)
             except Exception as e:
                 print(e)

        #print(api_response_objects)
        return api_response_objects

def get_newsText(api_response_objects):
    # Initialize a list to store the combined data

    # Iterate through the API response objects
    for api_response_object in api_response_objects:
        title = api_response_object.get("title", "")
        content = api_response_object.get("content", "")
        description = api_response_object.get("description", "")
        
        # Combine the fields into a single text field
        combined_text = f"{title} {content} {description}".strip()
        
        # Add the combined data to the list
        api_response_object["text"] = combined_text
    
    # Create a DataFrame from the data
    df = pd.DataFrame(api_response_objects)
    return df
          