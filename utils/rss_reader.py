import feedparser


def read_rss(feed_url, source, category, query):

    articles = []

    feed = feedparser.parse(feed_url)


    for item in feed.entries:

        title = item.get("title", "").strip()
        url = item.get("link", "").strip()


        if not title or not url:
            continue


        description = (
            item.get("summary", "")
            or item.get("description", "")
        )


        published = (
            item.get("published", "")
            or item.get("updated", "")
        )


        article = {
            "source": source,
            "category": category,
            "query": query,
            "title": title,
            "url": url,
            "description": description,
            "published": published
        }


        articles.append(article)


    return articles