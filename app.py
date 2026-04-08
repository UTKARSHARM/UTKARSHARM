import streamlit as st
import pandas as pd

st.set_page_config(page_title="StreamPulse", layout="wide")

st.title("🎬 StreamPulse Dashboard")

# Load data
media = pd.read_csv("media_content.csv")
reviews = pd.read_csv("user_review.csv")
cast = pd.read_csv("cast_crew.csv")
mapping = pd.read_csv("content_cast_map.csv")

# Merge data
merged = mapping.merge(cast, on="PersonID").merge(media, on="ContentID")

# Sidebar filters
st.sidebar.header("Filters")

actor_list = ["All"] + sorted(cast["Legal_Name"].unique())
selected_actor = st.sidebar.selectbox("Select Actor", actor_list)

# Filter logic
if selected_actor != "All":
    filtered = merged[merged["Legal_Name"] == selected_actor]
else:
    filtered = merged

# KPIs
st.subheader("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

col1.metric("🎥 Total Content", len(media))
col2.metric("👤 Total Users", len(reviews["UserID"].unique()))
col3.metric("⭐ Avg Rating", round(reviews["Stars"].mean(), 2))

# Content display
st.subheader("📽 Media Content")

if selected_actor != "All":
    st.dataframe(filtered[["Title", "Legal_Name"]])
else:
    st.dataframe(media)

# Reviews
st.subheader("⭐ User Reviews")
st.dataframe(reviews)

# Chart
st.subheader("📊 Ratings Distribution")
st.bar_chart(reviews.set_index("ContentID")["Stars"])