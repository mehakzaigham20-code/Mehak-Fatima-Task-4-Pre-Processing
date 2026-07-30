def limit_articles(articles, limit=1000):

    source_count = {}
    limited_articles = []

    for article in articles:

        source = article.get("source", "Unknown")

        if source not in source_count:
            source_count[source] = 0


        if source_count[source] < limit:

            limited_articles.append(article)
            source_count[source] += 1


    return limited_articles