import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_extras.app_logo import add_logo


def logo():
    add_logo("./images/logo.jpg", height=150)


logo()

df = pd.read_csv("./data/thai-go-all.csv")

st.sidebar.header("Options")

selected_gender = st.sidebar.selectbox("Dan Players", ("All", "Male", "Female"))

if selected_gender == "All":
    num = st.slider("Please select a range of Dan players by Dan-ID", 10, len(df), 100)
    title = str(num) + " Dan Players Ordered by Dan-ID"
    st.title(title)
    current_gat = df.columns[8]
    df2 = df.sort_values(["Dan-ID"], ascending=(True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))

dfmale = df[df["Gender"] == "♂️"]
if selected_gender == "Male":
    num = st.slider(
        "Please select a range of Male Dan players by Dan-ID", 10, len(dfmale), 100
    )
    title = str(num) + " Male Dan Players Ordered by Dan-ID"
    st.title(title)
    df2 = df[df["Gender"] == "♂️"]
    current_gat = df2.columns[8]
    df2 = df2.sort_values(["Dan-ID"], ascending=(True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))

dffemale = df[df["Gender"] == "♀️"]
if selected_gender == "Female":
    num = st.slider(
        "Please select a range of top GAT Point players", 10, len(dffemale), 30
    )
    title = str(num) + " Female Players Ordered by Dan-ID"
    st.title(title)
    df2 = df[df["Gender"] == "♀️"]
    current_gat = df2.columns[8]
    df2 = df2.sort_values(["Dan-ID"], ascending=(True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))
