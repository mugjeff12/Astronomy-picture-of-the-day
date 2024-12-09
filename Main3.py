import requests
import streamlit as st
from io import BytesIO
from PIL import Image

# Add custom starry background with an overlay for readability
def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("images.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: white;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent overlay */
            z-index: -1;
        }}
        .stTitle {{
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7); /* Add shadow for readability */
        }}
        .stMarkdown {{
            background: none; /* No background */
            padding: 0.5em 0;
            color: white; /* Keep text white */
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7); /* Slight shadow */
            font-size: 1.1em;
            line-height: 1.6em;
        }}
        .stButton button {{
            font-size: 1.1em;
            color: white !important;
            background-color: #1e3a8a; /* Navy Blue */
            border: none;
            border-radius: 8px;
            padding: 0.7em 1.2em;
            margin-top: 1em;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }}
        .stButton button:hover {{
            background-color: #2b4cb0; /* Lighter Blue on Hover */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

api_key = "gLWraVyVri8rkUaRPvepPbqbj20fx14aqUQ45Med"

# Title with a styled box
st.markdown('<h1 class="stTitle">🌌 NASA Astronomy Picture of the Day 🌠</h1>', unsafe_allow_html=True)

# Date picker and button layout
selected_date = st.date_input("Select a date (optional)", value=None)
get_picture = st.button("Get Picture")

# Function to fetch and display the APOD
def fetch_and_display_apod(date=None):
    if date:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    else:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    with st.spinner("Loading data..."):
        req = requests.get(url)
        if req.status_code != 200:
            st.error("Failed to fetch data. Please try again later.")
            st.stop()
        content = req.json()

    # Display content
    st.subheader(content["title"])
    if content["media_type"] == "image":
        image_url = content["url"]
        response2 = requests.get(image_url)
        image_data = BytesIO(response2.content)
        image = Image.open(image_data)
        st.image(image)
    else:
        st.write("This content is a video. Watch it here:")
        st.write(content["url"])
    st.markdown(content["explanation"], unsafe_allow_html=True)

# Automatically display today's picture on first load
if not selected_date and not get_picture:
    fetch_and_display_apod()

# Fetch picture for the selected date when button is clicked
if get_picture:
    fetch_and_display_apod(selected_date)




