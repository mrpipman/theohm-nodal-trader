
import streamlit as st
import dashboard

st.set_page_config(page_title="Ω Depot", layout="wide")

st.sidebar.title("Ω Menu")
page = st.sidebar.radio("Scegli una sezione", ["Dashboard"])

if page == "Dashboard":
    dashboard.show()
