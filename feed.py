import os

from config import SOURCES_DIR, OUTPUT_DIR

from utils.json_loader import load_all_sources
from utils.rss_reader import read_rss
from utils.cleaner import clean_article, remove_duplicates
from utils.article_limit import limit_articles
from utils.csv_writer import save_csv



def main():

    print("Loading JSON files...")
    print("-------------------------")

    # Load all source JSON files
    sources = load_all_sources(SOURCES_DIR)

    all_articles = []


    # Read RSS feeds
    for source in sources:

        print(f"Reading RSS: {source['source']}")

        articles = read_rss(
            source["rss"],
            source["source"],
            source["category"],
            source["query"]
        )

        all_articles.extend(articles)


    print("-------------------------")
    print(f"Total Fetched: {len(all_articles)}")


    # Cleaning
    cleaned_articles = []

    for article in all_articles:

        cleaned = clean_article(article)

        if cleaned:
            cleaned_articles.append(cleaned)


    print("-------------------------")
    print(f"After Cleaning: {len(cleaned_articles)}")


    # Remove duplicates
    cleaned_articles = remove_duplicates(cleaned_articles)

    print(f"After Duplicate Removal: {len(cleaned_articles)}")


    # Source limit increase
    cleaned_articles = limit_articles(
        cleaned_articles,
        1000
    )


    print(f"After Source Limit: {len(cleaned_articles)}")


    # Create output folder if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)


    # Save CSV
    output_file = os.path.join(
        OUTPUT_DIR,
        "final_articles.csv"
    )


    save_csv(
        cleaned_articles,
        output_file
    )


    print("-------------------------")
    print("CSV Created Successfully")
    print(f"Total Articles: {len(cleaned_articles)}")
    print(f"File: {output_file}")
    print("-------------------------")



if __name__ == "__main__":
    main()