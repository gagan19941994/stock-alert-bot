import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-IN,en;q=0.9"
}

def check_amazon(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(r.text, "lxml")

        title = soup.title.text.strip() if soup.title else "Amazon Product"

        page = soup.get_text(" ", strip=True).lower()

        if "currently unavailable" in page:
            stock = False
        else:
            stock = True

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
