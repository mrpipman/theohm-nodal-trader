from fetch_miso import fetch_miso_lmp
import sqlite3
import os

DB_PATH = "nodal_prices.db"
TABLE = "nodal_prices"

def ingest_miso():
    df = fetch_miso_lmp()
    os.makedirs("logs", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE, conn, if_exists="append", index=False)
    conn.close()
    print(f"✅ MISO: salvati {len(df)} record in {DB_PATH}")

if __name__ == "__main__":
    ingest_miso()