import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

# Import data from CSV files as dataframes
preference_dataframe = pd.read_csv("preference_data.csv")
summary_matrix = pd.read_csv("preference_summary.csv")
visitor_dataframe = pd.read_csv("visitor_data.csv")
plant_dataframe = pd.read_csv("plant_data.csv")
sales_dataframe = pd.read_csv("sales_data.csv")

# Example 1: Display preference data as an interactable table
st.header("Interactive Table")
st.dataframe(preference_dataframe)

# Example 2: Display preference summary matrix as a static table
st.header("Static Table")
st.table(summary_matrix)

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
sales_dataframe['Month'] = pd.to_datetime(sales_dataframe['Month'], format="%Y-%b")
sales_dataframe = sales_dataframe.sort_values('Month')
st.header("Line Chart")
st.line_chart(sales_dataframe, x="Month", y="Sales")
