import requests
from bs4 import BeautifulSoup

INSIGHT_URL = "http://your-real-insight-page.com"


def get_latest_insight():
    try:
        res = requests.get(INSIGHT_URL)
        soup = BeautifulSoup(res.text, "html.parser")

        # adjust this selector to your real page
        insight = soup.find(id="insight-message")

        if insight:
            return insight.text.strip()

    except Exception as e:
        print("Insight error:", e)

    return None