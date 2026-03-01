import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path

# Page Config
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load Data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent

    DATA_PATH = BASE_DIR.parent / "data" / "day.csv"

    day = pd.read_csv(DATA_PATH)
    
    day["dteday"] = pd.to_datetime(day["dteday"])
    
    return day

day_df = load_data()

# Sidebar Filter
st.sidebar.header("Filter")

selected_season = st.sidebar.multiselect(
    "Season",
    options=sorted(day_df["season"].unique()),
    default=sorted(day_df["season"].unique())
)

selected_weather = st.sidebar.multiselect(
    "Weather Situation",
    options=sorted(day_df["weathersit"].unique()),
    default=sorted(day_df["weathersit"].unique())
)

selected_workingday = st.sidebar.multiselect(
    "Working Day",
    options=[0, 1],
    default=[0, 1]
)

# Apply filter
filtered_day = day_df[
    (day_df["season"].isin(selected_season)) &
    (day_df["weathersit"].isin(selected_weather)) &
    (day_df["workingday"].isin(selected_workingday))
]

# Title
st.title("🚲 Bike Sharing Analytics Dashboard")

st.markdown("Dashboard ini menjawab dua pertanyaan utama:")
st.markdown("1. Faktor apa yang mempengaruhi jumlah peminjaman sepeda dan kapan peak terjadi?")
st.markdown("2. Bagaimana perbedaan perilaku casual vs registered?")

# Overview KPI
st.subheader("📊 Overview")

col1, col2, col3, col4 = st.columns(4)

total_rental = filtered_day["cnt"].sum()
total_casual = filtered_day["casual"].sum()
total_registered = filtered_day["registered"].sum()
avg_daily = filtered_day["cnt"].mean()

col1.metric("Total Rental", f"{int(total_rental):,}")
col2.metric("Total Casual", f"{int(total_casual):,}")
col3.metric("Total Registered", f"{int(total_registered):,}")
col4.metric("Average Daily Rental", f"{int(avg_daily):,}")

# Deman Analysis
st.subheader("📈 Demand Analysis")

# Trend over time
fig_trend = px.line(
    filtered_day,
    x="dteday",
    y="cnt",
    title="Trend Rental Over Time"
)
st.plotly_chart(fig_trend, use_container_width=True)

# Temperature effect
fig_temp = px.scatter(
    filtered_day,
    x="temp",
    y="cnt",
    trendline="ols",
    title="Effect of Temperature on Rental"
)
st.plotly_chart(fig_temp, use_container_width=True)

# Season effect
season_avg = filtered_day.groupby("season")["cnt"].mean().reset_index()

fig_season = px.bar(
    season_avg,
    x="season",
    y="cnt",
    title="Average Rental by Season"
)
st.plotly_chart(fig_season, use_container_width=True)

# Weather effect
weather_avg = filtered_day.groupby("weathersit")["cnt"].mean().reset_index()

fig_weather = px.bar(
    weather_avg,
    x="weathersit",
    y="cnt",
    title="Average Rental by Weather"
)
st.plotly_chart(fig_weather, use_container_width=True)

# Working day effect
workingday_avg = filtered_day.groupby("workingday")["cnt"].mean().reset_index()

fig_workingday = px.bar(
    workingday_avg,
    x="workingday",
    y="cnt",
    title="Average Rental by Working Day"
)
st.plotly_chart(fig_workingday, use_container_width=True)

# User Segmentation
st.subheader("👥 User Segmentation")

# Pie chart
user_totals = pd.DataFrame({
    "User Type": ["Casual", "Registered"],
    "Total": [total_casual, total_registered]
})

fig_pie = px.pie(
    user_totals,
    names="User Type",
    values="Total",
    title="User Distribution"
)
st.plotly_chart(fig_pie, use_container_width=True)

# Weather by segment
weather_segment = filtered_day.groupby("weathersit")[["casual", "registered"]].mean().reset_index()

fig_weather_segment = px.bar(
    weather_segment,
    x="weathersit",
    y=["casual", "registered"],
    barmode="group",
    title="Weather Impact by User Type"
)
st.plotly_chart(fig_weather_segment, use_container_width=True)

# Key Insight
st.subheader("💡 Key Insights")

st.markdown(f"""
- Registered user mendominasi sistem
- Temperatur memiliki hubungan positif terhadap jumlah rental
- Cuaca buruk menurunkan demand secara signifikan
""")

st.markdown("---")
st.caption("Copyright (c) Farhan Hanif Azhary 2026")