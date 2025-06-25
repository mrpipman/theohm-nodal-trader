from fetch_pjm import fetch_pjm_lmp
import pandas as pd
import sqlite3
import os
from datetime import datetime

DB_PATH = "nodal_prices.db"
TABLE_NAME = "nodal_prices"

def ingest_pjm():
    df_rt = fetch_pjm_lmp("rt_lmp_by_location")
    df_da = fetch_pjm_lmp("da_lmp_by_location")

    df_merged = pd.merge(df_da, df_rt, on=["timestamp", "node"], suffixes=("_da", "_rt"))
    df_merged["roi"] = (df_merged["lmp_rt"] - df_merged["lmp_da"]) / df_merged["lmp_da"] * 100
    df_merged["congestion_diff"] = df_merged["congestion_rt"] - df_merged["congestion_da"]
    return df_merged

def save_to_db(df):
    os.makedirs("logs", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    df = ingest_pjm()
    save_to_db(df)