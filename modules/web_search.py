# /modules/web_search.py

import requests
import json
import os
from newspaper import Article
import time

# --- Configuration ---
# It's better to use environment variables for API keys for security.
# You can set this in your terminal: export SERPER_API_KEY='your_key_here'
SERPER_API_KEY="SERPER_API_KEY" # Fallback to a default if not set

HEADERS = {
    "X-API-KEY": SERPER_API_KEY,
    "Content-Type": "application/json"
}
SEARCH_URL = "https://google.serper.dev/search"

def fetch_full_article_text(url: str) -> str:
    """
    Fetches and parses the full text content from a news article URL.
    
    Args:
        url: The URL of the news article.
        
    Returns:
        The extracted plain text of the article, or an empty string if fetching fails.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text.strip()
    except Exception as e:
        print(f"[!] Error fetching or parsing article at {url}: {e}")
        return ""

def search_web_for_context(news_title: str) -> list:
    """
    Searches the web for a news title to find related articles for context.
    
    Args:
        news_title: The title of the news article to search for.
        
    Returns:
        A list of dictionaries, where each dictionary contains the title, link,
        snippet, and full text of a related news article.
    """
    if not SERPER_API_KEY or SERPER_API_KEY == "YOUR_SERPER_API_KEY":
        print("[!] SERPER_API_KEY is not configured.")
        return []

    print(f"[*] Searching web for: '{news_title}'")
    payload = json.dumps({"q": news_title})
    
    try:
        response = requests.post(SEARCH_URL, headers=HEADERS, data=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        search_results = response.json().get("organic", [])
        
        context_articles = []
        # Limit to the top 5 results to keep the context concise
        for result in search_results[:5]:
            link = result.get("link")
            if link:
                content = fetch_full_article_text(link)
                context_articles.append({
                    "title": result.get("title", "No Title"),
                    "link": link,
                    "snippet": result.get("snippet", ""),
                    "full_text": content[:2000]  # Truncate to keep the context manageable
                })
                time.sleep(0.5) # Be polite to the servers

        print(f"[*] Found {len(context_articles)} relevant articles.")
        return context_articles

    except requests.exceptions.RequestException as e:
        print(f"[!] Web search failed: {e}")
        return []