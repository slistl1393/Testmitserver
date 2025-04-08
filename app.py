import streamlit as st
import requests

# Titel der App
st.title('Dateiupload und Verarbeitung')

# Datei-Upload-Widget
uploaded_file = st.file_uploader("Wählen Sie eine Datei", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Anzeigen des hochgeladenen Bildes
    st.image(uploaded_file, caption="Hochgeladenes Bild", use_column_width=True)

    # Senden der Datei an den Server (via POST-Request)
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://51.21.199.100:8000/upload/", files=files)

    # Antwort des Servers anzeigen
    if response.status_code == 200:
        st.success("Datei erfolgreich verarbeitet!")
        st.write(response.json())  # Falls der Server eine Antwort zurückgibt
    else:
        st.error("Fehler bei der Verarbeitung der Datei!")
