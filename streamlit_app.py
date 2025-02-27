
import streamlit as st
import pandas as pd

df = pd.read_csv('data/titanic_data.csv')

st.title("Titanic Data Analysis")

st.header("Survivors by gender")
bar_color = st.color_picker("Pick a color for the bar chart", "#1f77b4")


col1, col2 = st.columns(2)


with col1:
    survivors = df[df["Survived"] == 1]
    survivor_counts = survivors["Sex"].value_counts()
    st.bar_chart(survivor_counts, use_container_width=True, color=bar_color)


with col2:
    st.header("Embarkation data")
    
    embarked_counts = df["Embarked"].value_counts().reset_index()
    embarked_counts.columns = ["Harbour", "Count"]
    embarked_counts["Harbour"] = embarked_counts["Harbour"].replace({"S": "Southampton", "C": "Cherbourg", "Q": "Queenstown"})
    
    st.dataframe(embarked_counts, use_container_width=True)


