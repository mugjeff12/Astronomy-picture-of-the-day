import requests
import streamlit as st
from io import BytesIO
from PIL import Image

api_key = "gLWraVyVri8rkUaRPvepPbqbj20fx14aqUQ45Med"

# Title
st.markdown(
    '<h1 style="text-align: center; font-size: 2em; font-weight: bold; color: black;">🌌 NASA Astronomy Picture of the Day 🌠</h1>',
    unsafe_allow_html=True,
)

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
    st.markdown(f"<div style='color: black;'>{content['explanation']}</div>", unsafe_allow_html=True)

# Automatically display today's picture on first load
if not selected_date and not get_picture:
    fetch_and_display_apod()

# Fetch picture for the selected date when button is clicked
if get_picture:
    fetch_and_display_apod(selected_date)




