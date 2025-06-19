
import requests
import streamlit as st

def fetch_youtube_links(query, max_results=3):
    api_key = st.secrets["youtube"]["api_key"]
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "key": api_key,
        "maxResults": max_results
    }
    response = requests.get(url, params=params)
    videos = response.json().get("items", [])
    return [f"https://www.youtube.com/watch?v={v['id']['videoId']}" for v in videos]
