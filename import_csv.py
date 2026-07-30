import pandas as pd
import psycopg2

# Read CSV file
df = pd.read_csv("final_articles.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="akc_scraper",
    user="postgres",
    password="YOUR_PASSWORD",   # <-- apna PostgreSQL password likho
    port=5432
)

cur = conn.cursor()

# Insert each row into database
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO final_articles
        (source, category, query, title, url, description, published)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row["source"],
        row["category"],
        row["query"],
        row["title"],
        row["url"],
        row["description"],
        row["published"]
    ))

# Save changes
conn.commit()

print("✅ CSV imported successfully!")

cur.close()
conn.close()