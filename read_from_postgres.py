import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="akc_scraper",
    user="postgres",
    password="5432",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM final_articles LIMIT 10")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()