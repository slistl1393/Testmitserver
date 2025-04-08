import streamlit as st
import requests

# URL des Servers
url = "http://51.21.199.100:8000/upload/"

# Lade die Bilder über Streamlit hoch
plan_image = st.file_uploader("Lade das Planbild hoch", type=["png", "jpg", "jpeg"])
verzeichnis_image = st.file_uploader("Lade das Verzeichnisbild hoch", type=["png", "jpg", "jpeg"])

# Wenn beide Bilder hochgeladen wurden
if plan_image is not None and verzeichnis_image is not None:
    # Erstelle ein Dictionary, um die Dateien zu senden
    files = {
        'plan_image': plan_image,
        'verzeichnis_image': verzeichnis_image
    }

    # POST-Anfrage an den Server
    try:
        response = requests.post(url, files=files)
        
        # Überprüfe, ob die Antwort erfolgreich war
        if response.status_code == 200:
            st.write("Serverantwort:", response.json())  # Zeige die Antwort des Servers
        else:
            st.error(f"Fehler: Server antwortete mit Statuscode {response.status_code}")
            st.write("Antworttext:", response.text)
    except Exception as e:
        st.error(f"Fehler bei der Anfrage: {e}")



