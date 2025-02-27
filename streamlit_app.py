
import streamlit as st
import pandas as pd



df = pd.read_csv('data/titanic_data.csv')

st.title("Titanic Data Analysis")

st.header("Survivors by gender")
bar_color = st.color_picker("Pick a color for the bar chart", "#1f77b4")


survivors = df[df["Survived"] == 1]
survivor_counts = survivors["Sex"].value_counts()

st.bar_chart(survivor_counts, use_container_width=False,width = 250, color=bar_color)

st.header("Embarkation data")

embarked_counts = df["Embarked"].value_counts().reset_index()
embarked_counts.columns = ["Harbour", "Count"]

st.dataframe(embarked_counts)


