import requests
import streamlit as st

api_key = "gLWraVyVri8rkUaRPvepPbqbj20fx14aqUQ45Med"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

req = requests.get(url)

content = req.json()

print(content)

image_url = content["url"]
# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)


st.title(content["title"])
st.image("img.png")
st.write(content["explanation"])

