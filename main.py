import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple data analysis dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

  st.subheader("Data preview - first 5 rows")
  st.write(df.head())

  st.subheader("Data summary")
  st.write(df.describe())

  st.subheader("Filter data")
  columns = df.columns.tolist()
  selected_column = st.selectbox("Select column to filter by", columns)
  unique_values = df[selected_column].unique()
  selected_values = st.selectbox("Select value", unique_values)

  filtered_df = df[df[selected_column] == selected_values]
  st.write(filtered_df)

  st.subheader("Plot data")
  x_column = st.selectbox("Select x-axis column", columns)
  y_column = st.selectbox("Select y-axis column", columns)

  if st.button("Generate plot"):
    st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
  st.write("Waiting on file upload...")