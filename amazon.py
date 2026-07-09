import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-IN,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}


def check_amazon(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=25,
            allow_redirects=True
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        title = "Amazon Product"

        if soup.title:
            title = soup.title.text.strip()

        page = soup.get_text(" ", strip=True).lower()

        # Amazon CAPTCHA
        if "enter the characters you see below" in page or "captcha" in page:
            return {
                "title": "Amazon CAPTCHA",
                "stock": False,
                "url": url
            }

        out_of_stock = [
            "currently unavailable",
            "temporarily out of stock",
            "out of stock"
        ]

        in_stock = [
            "add to cart",
            "buy now"
        ]

        stock = False

        for word in in_stock:
            if word in page:
                stock = True
                break

        if not stock:
            for word in out_of_stock:
                if word in page:
                    stock = False
                    break

        return {
            "title": title,
            "stock": stock,
            "url": url
        }

    except Exception:
        return {
            "title": "Amazon Error",
            "stock": False,
            "url": url
        }