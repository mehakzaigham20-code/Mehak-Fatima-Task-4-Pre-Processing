import re


def clean_article(article):

    if not isinstance(article, dict):
        return None

    cleaned = {}

    for key, value in article.items():

        if isinstance(value, str):

            value = re.sub(r"\s+", " ", value)
            value = value.strip()

        cleaned[key] = value

    return cleaned



def remove_duplicates(articles):

    unique_articles = []

    seen_urls = set()


    for article in articles:

        url = article.get("url", "").strip()


        if url and url not in seen_urls:

            seen_urls.add(url)
            unique_articles.append(article)


        elif not url:

            unique_articles.append(article)


    return unique_articles