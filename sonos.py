import os
from anthropic import Anthropic
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup


import os
"""
This script fetches news articles from Google News based on specified search terms, classifies the sentiment"""
client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

print(os.path.abspath("coverage.txt"))

def fetch_google_news(query = ["sonos"], max_items=5):
    all_articles = {}
    for q in query:
        """Return a list of dicts for Google News results matching `query`."""
        url = (
            "https://news.google.com/rss/search?q="+ quote_plus(q)+ "&hl=en-US&gl=US&ceid=US:en"
        )
        headers = {"User-Agent": "Mozilla/5.0 (student learning project)"}

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 

        soup = BeautifulSoup(response.content, "xml")

        articles = []
        for item in soup.find_all("item")[:max_items]:
            title_tag = item.find("title")
            link_tag = item.find("link")
            date_tag = item.find("pubDate")
            source_tag = item.find("source")

            articles.append(
                {
                    "title": title_tag.get_text(strip=True) if title_tag else None,
                    "link": link_tag.get_text(strip=True) if link_tag else None,
                    "published": date_tag.get_text(strip=True) if date_tag else None,
                    "source": source_tag.get_text(strip=True) if source_tag else None,
                    "source_url": source_tag.get("url") if source_tag else None,
                }
            )
        all_articles[q] = articles

    return all_articles if articles else None

def call_ai_model(title):
   

    message = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1024,
        system="You classify news headlines by the public opinion they suggest about the company. "
               "Respond with exactly one word: ok, good, or bad.",
        messages=[{"role": "user", "content": title}])
    return message.content[-1].text
    # Example: return ai_model.generate_response(prompt)


if __name__ == "__main__":
    search_terms = ["sonos" , "Bose" , "Apple" , "Google Earbuds"]
    results = fetch_google_news(search_terms)
    if not results:
        print("No items found. Print soup.prettify()[:2000] to inspect what came back.")
    x = 1
    ai_dict = {}
    with open("coverage.txt", "w") as f:
        for name in results:
            for article in results[name]:
                f.write(f"{x} {name}. {article['title']}\n")
                f.write(f"   Source:    {article['source']}\n")
                f.write(f"   Published: {article['published']}\n")
                f.write(f"   Link:      {article['link']}\n\n")
                title = article['title']
                source = article['source']
                published = article['published']
                link = article['link']
                ai_response = call_ai_model(title)
                f.write(f"   AI Model Response: {ai_response}\n\n")
                x += 1
                ai_dict[title] = {
                    "ai_response": ai_response
                }
    with open("coverage.txt", "r") as f:
            print(f.read())
    


        
        
