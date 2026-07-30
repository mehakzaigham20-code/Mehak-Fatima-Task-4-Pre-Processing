import csv


def save_csv(articles, filename):

    if not articles:
        print("No articles found")
        return


    keys = articles[0].keys()


    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=keys
        )

        writer.writeheader()

        writer.writerows(articles)