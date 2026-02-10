import streamlit as st
import pandas as pd

st.title("CyberCop Adaptive Honeypot Monitor")

try:
    df = pd.read_csv("logs/attacks.csv", names=["ip","user","pass","time"])
    st.metric("Total Attacks", len(df))
    st.dataframe(df.tail(20))
except:
    st.write("No attack data yet")
