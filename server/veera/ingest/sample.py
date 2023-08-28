import requests

from datetime import datetime, timezone
from superdesk.metadata.utils import generate_tag_from_url
from superdesk.io.feeding_services import HTTPFeedingService


class SampleFeedingService(HTTPFeedingService):
    NAME = "sample-service"
    label = "Sample service"

    url = "https://newsapi.org/v2/top-headlines"
    fields = (
        {
            "id": "apikey",
            "type": "text",
            "label": "Api Key",
            "placeholder": "News API key",
            "required": True,
        },
    )

    def _update(self, provider, update, **kwargs):
        apikey = provider["config"].get("apikey")
        if not apikey:
            return []
        resp = requests.get(self.url, params={"country": "us", "apikey": apikey})
        resp.raise_for_status()
        data = resp.json()
        yield [
            {
                "type": "text",
                "uri": article["url"],
                "guid": generate_tag_from_url(article["url"]),
                "versioncreated": datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=timezone.utc
                ),
                "byline": article.get("author"),
                "headline": article.get("title"),
                "abstract": article.get("description"),
                "body_html": article.get("content"),
            }
            for article in data["articles"]
        ]
