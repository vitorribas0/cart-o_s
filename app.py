from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Nome do arquivo Excel
ARQUIVO_EXCEL = "localizacoes.xlsx"

@app.route('/capturar', methods=['POST'])
def capturar_localizacao():
    dados = request.json
    latitude = dados.get('latitude')
    longitude = dados.get('longitude')

    # Carregar ou criar um DataFrame
    try:
        df = pd.read_excel(ARQUIVO_EXCEL)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Latitude', 'Longitude'])

    # Adicionar nova linha
    df = pd.concat([df, pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude]})], ignore_index=True)
    df.to_excel(ARQUIVO_EXCEL, index=False)

    return {"mensagem": "Localização salva com sucesso!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
