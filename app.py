import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

# Import data from CSV files as dataframes
visitor_dataframe = pd.read_csv("visitor_data.csv")
plant_dataframe = pd.read_csv("plant_data.csv")

# Example 1: Display visitor as an interactable table
st.header("Visitor Data (Interactable Table)")
st.dataframe(visitor_dataframe)

# Example 2: Display visitor data as a static table
st.header("Plant Height Data (Static Table)")
st.table(plant_dataframe)

# Example 3: Display last visitor count as a metric
last_recorded = visitor_dataframe["Count"].iloc[-1]
previous_recorded = visitor_dataframe["Count"].iloc[-2]

value = last_recorded
delta = last_recorded - previous_recorded

st.header("Metric")
st.metric("Visitors", value, delta, border=True)

# Example 4: Create bar chart for plant height data
st.header("Bar Chart")
st.bar_chart(plant_dataframe, x="Plant", y="Height (in cm)")

# Example 5: Create line chart for visitor data
st.header("Line Chart")
st.line_chart(visitor_dataframe, x="Year", y="Count")
