import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-IN,en;q=0.9"
}

def check_flipkart(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(r.text, "lxml")

        title = soup.title.text.strip() if soup.title else "Flipkart Product"

        page = soup.get_text(" ", strip=True).lower()

        out_words = [
            "out of stock",
            "sold out",
            "currently unavailable"
        ]

        stock = not any(word in page for word in out_words)

        return {
            "title": title,
            "stock": stock,
            "url": url
        }

    except Exception as e:
        return {
            "title": "Error",
            "stock": False,
            "url": url,
            "error": str(e)
        }
