import streamlit as st
import streamlit.components.v1 as components

# Função para capturar a localização via JavaScript
#def get_geolocation():
    # Código JavaScript para capturar a localização
    js_code = """
    <script>
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        window.parent.postMessage({latitude: latitude, longitude: longitude}, "*");
    });
    </script>
    """
    components.html(js_code, height=0)  # Executa o código JS para capturar a localização

# Função para mostrar a localização no sidebar
def show_location(latitude, longitude):
    with st.sidebar:
        st.write(f"### Localização capturada:")
        st.write(f"**Latitude**: {latitude}")
        st.write(f"**Longitude**: {longitude}")

# Configuração da página
st.set_page_config(page_title="Captura de Localização", layout="wide")

# Título
st.title("Captura de Localização Atual")

# Se o botão for pressionado, executa a captura da localização
if st.button("Capturar Localização"):
    # Inicia o processo de captura de localização com JS
    st.write("Capturando localização...")

    # Chama a função para obter a geolocalização
    get_geolocation()

# Mensagem de instrução na página
st.write("Quando você clicar no botão, sua localização atual será capturada e exibida no sidebar.")
