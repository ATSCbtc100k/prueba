# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.title("Read Google Sheet as DataFrame")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="dadesdaga", usecols=list(range(6)),ttl=5)
df = df.dropna(how="all")

st.dataframe(df)