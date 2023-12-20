import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo


def logo():
    add_logo("./images/logo.jpg", height=150)


logo()

st.markdown(
    "<b><h2 style='text-align: center; color: LightCoral;'>About This Project</h2><b>",
    unsafe_allow_html=True,
)

# st.write(
#   "Go is a mind sport where two players aim to surround more territory than the opponent. The game was invented in China more than 4,500 years ago, and it is believed to be the oldest board game still being played today."
# )

st.write(
    "In this project, I analyze and visualize GAT Point (a scoring system to estimate the players' Go strengths in Thailand), which is stored in Google Sheets and updated twice a month by the Thailand Go Association. I wrote a Python program to download the data in CSV format and clean it. After that, I analyzed and visualized the data on the website using Plotly and Streamlit libraries. This website comprises three main pages: Dashboard, Top N ranking Players (by GAT-Point), and Search Players (by Name). This web app is my final project in the [CS50x 2023](https://cs50.harvard.edu/x/2023/) course."
)


st.markdown(
    "<b><h2 style='text-align: center; color: LightCoral;'>About Me</h2><b>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns((1, 1.5), gap="Medium")

with col1:
    st.image("./images/me.jpg")

with col2:
    st.write(
        "I've been playing Go since I was a little young girl. Go has helped me develop many life skills, such as calculation, memory, and creativity. From there, I developed this web application to visualize GAT Point of Go players in Thailand. GAT Point web will let Go players know their status, progress, and ranking in Thailand. Last, I hope this web application will inspire Go players to continuously improve their Go capabilities and benefit the Thailand Go community.🖤🤍"
    )

st.markdown(
    "###### [GAT-Point Data](https://drive.google.com/file/d/14SMzCtmljfmfT2OpVxmrN0XrBb1P4hCU/view)",
)
