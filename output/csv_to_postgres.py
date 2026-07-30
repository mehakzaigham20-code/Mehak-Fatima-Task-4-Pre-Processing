import pandas as pd
import psycopg2
from pathlib import Path

# ==========================
# CSV FILE PATH
# ==========================
csv_file = Path(r"C:\Users\HP\Desktop\limoex\NewsScraperProject task 3 (28 july)\output\final_articles.csv")

# Read CSV
df = pd.read_csv(csv_file)

# ==========================
# CONNECT TO POSTGRESQL
# ==========================
conn = psycopg2.connect(
    host="localhost",
    database="akc_scraper",
    user="postgres",
    password="5432",   # <-- apna password likho
    port="5432"
)

cur = conn.cursor()

# ==========================
# CREATE TABLE IF NOT EXISTS
# ==========================
cur.execute("""
CREATE TABLE IF NOT EXISTS final_articles (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255),
    category VARCHAR(255),
    query TEXT,
    title TEXT,
    url TEXT UNIQUE,
    description TEXT,
    published TEXT
);
""")

conn.commit()

# ==========================
# INSERT DATA
# ==========================
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO final_articles
        (source, category, query, title, url, description, published)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (url)
        DO NOTHING;
    """, (
        row["source"],
        row["category"],
        row["query"],
        row["title"],
        row["url"],
        row["description"],
        row["published"]
    ))

conn.commit()

print(f"✅ {len(df)} records imported successfully.")

cur.close()
conn.close()