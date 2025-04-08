import streamlit as st
import requests

st.title("Bild hochladen")

plan_image = st.file_uploader("Lade den Plan hoch", type="png")
verzeichnis_image = st.file_uploader("Lade das Verzeichnis-Bild hoch", type="png")

if plan_image and verzeichnis_image:
    files = {
        "plan_image": plan_image,
        "verzeichnis_image": verzeichnis_image
    }

    response = requests.post("http://51.21.199.100:8000//upload/", files=files)

    st.write(response.json())

