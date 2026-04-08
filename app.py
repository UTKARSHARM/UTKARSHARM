import streamlit as st
import pandas as pd

st.set_page_config(page_title="StreamPulse", layout="wide")

st.title("🎬 StreamPulse Dashboard")

media = pd.read_csv("media_content.csv")
reviews = pd.read_csv("user_review.csv")

st.subheader("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

col1.metric("🎥 Total Content", len(media))
col2.metric("👤 Total Users", len(reviews["UserID"].unique()))
col3.metric("⭐ Avg Rating", round(reviews["Stars"].mean(), 2))

st.subheader("📽 Media Content")
st.dataframe(media)

st.subheader("⭐ User Reviews")
st.dataframe(reviews)

st.subheader("📊 Ratings Distribution")
st.bar_chart(reviews.set_index("ContentID")["Stars"])