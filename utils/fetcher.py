import requests
from bs4 import BeautifulSoup


def fetch_article(url):

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.text if soup.title else ""

        paragraphs = soup.find_all("p")

        content = " ".join(
            p.text for p in paragraphs[:5]
        )

        return {
            "title": title.strip(),
            "content": content.strip(),
            "url": url
        }

    except Exception as e:

        return {
            "title": "",
            "content": "",
            "url": url,
            "error": str(e)
        }