
import streamlit as st
import pandas as pd
import sqlite3

def show():
    st.title("📊 Dashboard - ENTSO-E Demo")

    try:
        conn = sqlite3.connect("arbitrage_trades.db")
        df = pd.read_sql("SELECT * FROM entsoe_prices", conn)
        conn.close()
        st.dataframe(df)
        st.line_chart(df.groupby("hour")["price"].mean())
    except Exception as e:
        st.error(f"Errore nel caricamento dati: {e}")
