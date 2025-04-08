import requests
import streamlit as st

# Deine URL für die API
url = "http://51.21.199.100:8000/upload/"

# Deine Bilddaten (Stellen Sie sicher, dass du die richtigen Dateien übergibst)
files = {
    'plan_image': open('plan.png', 'rb'),
    'verzeichnis_image': open('verzeichnis.png', 'rb')
}

# POST-Request an den Server
response = requests.post(url, files=files)

# Überprüfe, ob die Antwort erfolgreich war
if response.status_code == 200:
    try:
        # Versuche, die Antwort als JSON zu parsen
        st.write(response.json())
    except ValueError as e:
        # Falls die Antwort kein gültiges JSON ist, logge den Fehler
        st.error(f"Fehler beim Parsen der Antwort als JSON: {e}")
        st.write("Antworttext:", response.text)
else:
    st.error(f"Fehler: Server antwortete mit Statuscode {response.status_code}")
    st.write("Antworttext:", response.text)


