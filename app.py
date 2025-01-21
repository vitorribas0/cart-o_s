import streamlit as st
import json

# Função para capturar localização simulada (JavaScript não é diretamente suportado pelo Streamlit)
def obter_localizacao():
    # Localização de exemplo (substitua por integração real, se disponível)
    return {"latitude": -23.550520, "longitude": -46.633308}  # São Paulo, SP, Brasil

# Configuração da página
st.set_page_config(page_title="Link com os dados da conta", layout="wide")

# Título
st.title("Senhas banco Sérgio")

# Botão para capturar a localização
if st.button("Dados e senha itaú"):
    # Capturar localização simulada
    localizacao = obter_localizacao()
    
    # Mostrar localização no sidebar
    with st.sidebar:
        st.write("### Dados e senha itaú:")
        st.json(localizacao)

    # Mensagem de confirmação
    st.success("Dados e senha itaú!")
else:
    with st.sidebar:
        st.write("Clique no botão para capturar a senha.")

# Instruções na página principal
#.write("Este aplicativo captura sua localização simulada. Para uso real, integre com APIs de localização.")
