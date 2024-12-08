import requests
import streamlit as st

api_key = "gLWraVyVri8rkUaRPvepPbqbj20fx14aqUQ45Med"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

req = requests.get(url)

content = req.json()

print(content)

st.title(content["title"])
st.image(content["hdurl"])
st.write(content["explanation"])
