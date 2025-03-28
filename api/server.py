import pandas as pd
import numpy as np
import json
import unicodedata
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from fuzzywuzzy import process


app = Flask(__name__)
CORS(app)

# Função para normalizar acentos e caracteres especiais
def normalizar_texto(texto):
    if isinstance(texto, str):
        # Remover caracteres invisíveis ou corrompidos
        texto = texto.encode("utf-8", "ignore").decode("utf-8")
        # Normalizar acentos
        nfkd_form = unicodedata.normalize("NFKD", texto)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return texto

# Função para carregar e limpar os dados
def load_data():
    try:
        df = pd.read_csv(
            '../Relatorio_cadop.csv', 
            sep=';', 
            encoding='utf-8-sig',  # Tenta manter os acentos corretos
            dtype=str  # Trata todas as colunas como string
        )

        # Garantir que todas as colunas sejam string e aplicar normalização
        def clean_column(column):
            return (
                column.fillna('')
                .astype(str)
                .str.strip()
                .apply(normalizar_texto)  # Remove acentos corrompidos e caracteres invisíveis
                .str.upper()  # Deixa tudo maiúsculo para padronizar
            )

        columns_to_clean = [
            'Razao_Social', 'Nome_Fantasia', 'Cidade', 'UF', 
            'Modalidade', 'CNPJ', 'Registro_ANS'
        ]

        for col in columns_to_clean:
            df[col] = clean_column(df[col])

        # Remover registros completamente vazios
        df = df[df[columns_to_clean].apply(lambda row: any(row != ''), axis=1)]

        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

# Carregar dados globalmente
df_operadoras = load_data()

@app.route('/busca', methods=['GET'])
def buscar_operadoras():
    if df_operadoras is None:
        return Response(
		json.dumps(resultados,ensure_ascii=False),
		content_type='application/json; charset=utf-8'
		)

    # Parâmetros da requisição
    consulta = request.args.get('q', '').strip()
    max_resultados = int(request.args.get('limit', 10))
    pagina = int(request.args.get('page', 1))
    modalidade_filtro = request.args.get('modalidade', '').strip()

    # Copiar DataFrame e aplicar filtros
    df_filtrado = df_operadoras.copy()

    # Normalizar a consulta (remover acentos e converter para maiúsculas)
    consulta_normalizada = normalizar_texto(consulta).upper()

    # Busca com múltiplos critérios se houver consulta
    if consulta_normalizada:
        mask = (
            df_filtrado['Razao_Social'].str.contains(consulta_normalizada, case=False, na=False) |
            df_filtrado['Nome_Fantasia'].str.contains(consulta_normalizada, case=False, na=False) |
            df_filtrado['Cidade'].str.contains(consulta_normalizada, case=False, na=False) |
            df_filtrado['CNPJ'].str.contains(consulta_normalizada, na=False) |
            df_filtrado['Registro_ANS'].str.contains(consulta_normalizada, na=False)
        )
        df_filtrado = df_filtrado[mask]

    # Ordenar por Razao_Social para consistência
    df_filtrado = df_filtrado.sort_values('Razao_Social')

    # Paginação
    inicio = (pagina - 1) * max_resultados
    fim = inicio + max_resultados

    # Converter para dicionário, preenchendo valores vazios corretamente
    resultados = df_filtrado.iloc[inicio:fim].to_dict('records')

    for resultado in resultados:
        for chave, valor in resultado.items():
            if pd.isna(valor) or valor.strip() == '':
                resultado[chave] = 'Não informado'

    return Response(
	json.dumps(resultados, ensure_ascii=False),
	content_type='application/json; charset=utf-8'
	)
@app.route('/')
def home():
    return jsonify({"mensagem": "API de busca de operadoras está rodando!"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
