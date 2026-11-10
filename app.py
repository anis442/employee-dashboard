import streamlit as st
import pandas as pd

st.title("Employee Dashboard")

df = pd.read_csv(r"C:\Users\suhan ali\Downloads\member.csv")

st.metric("Total Employees", len(df))

st.metric("Highest Salary", df["salary"].max())

st.metric("Average Salary", round(df["salary"].mean()))

st.subheader("Employee Information")
st.dataframe(df)

st.subheader("Salary Chart")
st.bar_chart(df.set_index("name")["salary"])