import streamlit as st
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("group4cleaneddata.csv", parse_dates=['booking_datetime'])

st.title("ADTA5410 Team 4 Dashboard")
st.write(
    "Welcome to Team 4's Dashboard."
)

# 3. Graph: Cancelled/NoShow over time
st.subheader("Cancelled / NoShow Over Time")
df['booking_date'] = pd.to_datetime(df['booking_datetime']).dt.date
cancel_data = df[df['target_class'].isin(['Cancelled', 'NoShow'])]
cancel_summary = cancel_data.groupby(['booking_date', 'target_class']).size().unstack(fill_value=0)
st.line_chart(cancel_summary)

# 4. Map: Cancelled or NoShow by Country
st.subheader("Map of Cancelled / NoShow Bookings by Country")

# Mock lat/lon dictionary for countries (you can extend as needed)
country_coords = {
    'US': [37.0902, -95.7129],
    'CA': [56.1304, -106.3468],
    'DE': [51.1657, 10.4515],
    'JP': [36.2048, 138.2529],
    'ZA': [-30.5595, 22.9375],
    'IN': [20.5937, 78.9629],
    'FR': [46.6034, 1.8883],
    'UK': [55.3781, -3.4360],
    'AU': [-25.2744, 133.7751]
}

map_data = cancel_data['country_code'].value_counts().rename_axis('country_code').reset_index(name='count')
map_data[['lat', 'lon']] = map_data['country_code'].apply(lambda x: pd.Series(country_coords.get(x, [None, None])))
map_data = map_data.dropna()

st.map(map_data[['lat', 'lon']])
