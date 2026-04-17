import psycopg2
import pandas as pd

def load_data():
    conn = psycopg2.connect(
        dbname="sales_db",
        user="postgres",
        password="Aaisaheb@04",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    # 👉 CREATE df FIRST
    df = pd.read_csv("data/sales.csv")

    # 👉 THEN loop
    for _, row in df.iterrows():
        print("Row length:", len(row))
        print("Row data:", row.values)

        cursor.execute("""
            INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row.values[:19]))

    conn.commit()
    cursor.close()
    conn.close()

load_data()