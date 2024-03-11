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

selected_gender = st.sidebar.selectbox(
    "Top GAT Point Players", ("All", "Male", "Female")
)
active = (df["Active"]).value_counts()
active = active[True]
numall = 30
if active < 30:
    numall = active
if selected_gender == "All":
    num = st.slider(
        "Please select a range of top GAT Point active players", 10, active, numall
    )
    title = "Current Top " + str(num) + " Active Players Ranking"
    st.title(title)
    df2 = df[df["Active"] == True]
    current_gat = df2.columns[8]
    df2 = df2.sort_values([current_gat, "Dan-ID"], ascending=(False, True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))

if selected_gender == "Male":
    df2 = df[df["Gender"] == "♂️"]
    active = (df2["Active"]).value_counts()
    active = active[True]
    numall = 30
    if active < 30:
        numall = active
    num = st.slider(
        "Please select a range of top GAT Point ctive players", 10, active, numall
    )
    title = "Current Top " + str(num) + " Active Male Players Ranking"
    st.title(title)
    current_gat = df2.columns[8]
    df2 = df2.sort_values([current_gat, "Dan-ID"], ascending=(False, True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))
if selected_gender == "Female":
    df2 = df[df["Gender"] == "♀️"]
    active = (df2["Active"]).value_counts()
    active = active[True]
    numall = 30
    if active < 30:
        numall = active
    num = st.slider(
        "Please select a range of top GAT Point active players", 10, active, numall
    )
    title = "Current Top " + str(num) + " Active Female Players Ranking"
    st.title(title)
    df2 = df[df["Gender"] == "♀️"]
    df2 = df2[df2["Active"] == True]
    current_gat = df2.columns[8]
    df2 = df2.sort_values([current_gat, "Dan-ID"], ascending=(False, True))
    df2 = df2.iloc[:num, [1, 2, 4, 5, 6, 8]]
    df2.insert(loc=0, column="Rank", value=range(1, num + 1))
    df2.set_index("Rank", inplace=True)
    df2.rename(columns={current_gat: "GAT Point"}, inplace=True)
    df2.rename(columns={"Diamond": "💎?"}, inplace=True)
    st.table(df2.style.format(subset=["GAT Point"], formatter="{:.2f}"))
