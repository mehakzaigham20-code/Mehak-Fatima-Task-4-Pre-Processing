import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="akc_scraper",
        user="postgres",
        password="5432",
        port="5432"
    )

    print("✅ Connected to PostgreSQL!")

    cur = conn.cursor()
    cur.execute("SELECT version();")

    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)