import streamlit as st
import requests

st.title("Shakespeare translator")

def translate():
  url = "https://shakespeare.p.rapidapi.com/shakespeare.json"

  querystring = {"text": user_input}
  
  headers = {
  	"X-FunTranslations-Api-Secret": "<REQUIRED>",
  	"X-RapidAPI-Key": "3f3b11d37emsh3cdf63d8eb9dcd9p1b66d6jsn0f5674878782",
  	"X-RapidAPI-Host": "shakespeare.p.rapidapi.com"
  }
  
  response = requests.get(url, headers=headers, params=querystring)
  
  
  tranalated = response.json()["contents"]["translated"]

  st.subheader(f"Translation: {tranalated}")





user_input = st.text_input("Enter text to translate")

st.button("Convert", type="primary", use_container_width=True, on_click=translate)
