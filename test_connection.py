import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="akc_scraper",
        user="postgres",
        password="5432"
    )

    print("✅ PostgreSQL Connected Successfully!")

    conn.close()

except Exception as e:
    print("❌ Connection Failed:")
    print(e)