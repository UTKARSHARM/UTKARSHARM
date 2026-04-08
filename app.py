import streamlit as st
from db import run_query

st.set_page_config(page_title="StreamPulse", layout="wide")

st.title("🎬 StreamPulse Dashboard")

# KPIs
st.subheader("📊 Platform Overview")

total_content = run_query("SELECT COUNT(*) as count FROM Media_Content")
total_users = run_query("SELECT COUNT(*) as count FROM User_Account")
avg_rating = run_query("SELECT AVG(Stars) as avg FROM User_Review")

col1, col2, col3 = st.columns(3)

col1.metric("🎥 Total Content", int(total_content["count"][0]))
col2.metric("👤 Total Users", int(total_users["count"][0]))
col3.metric("⭐ Avg Rating", round(avg_rating["avg"][0], 2))

# Content Table
st.subheader("📽 Media Content")
df = run_query("SELECT * FROM Media_Content")
st.dataframe(df, use_container_width=True)

# Reviews Table
st.subheader("⭐ User Reviews")
reviews = run_query("SELECT * FROM User_Review")
st.dataframe(reviews, use_container_width=True)

# Chart
st.subheader("📊 Ratings Distribution")
st.bar_chart(reviews.set_index("ContentID")["Stars"])