import pdfplumber
import pandas as pd
import zipfile
import re

# Mapeamento apenas para OD e AMB
abreviacoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

def limpar_texto(texto):
    """
    Normaliza o texto, mantendo campos vazios como string vazia
    """
    if pd.isna(texto) or texto is None:
        return ""
    if isinstance(texto, str):
        return re.sub(r'\s+', ' ', texto).strip()
    return str(texto).strip()

def extrair_tabela_pdf(pdf_path):
    """Extrai tabelas do PDF, mantendo todas as linhas"""
    dados_extraidos = []
    total_paginas = 0
    paginas_com_tabela = 0

    with pdfplumber.open(pdf_path) as pdf:
        total_paginas = len(pdf.pages)
        
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables and len(tables) > 0:
                paginas_com_tabela += 1
                
                for table in tables:
                    # Pula a primeira linha se for cabeçalho
                    start_index = 1 if any('PROCEDIMENTO' in str(cell) for cell in table[0]) else 0
                    for row in table[start_index:]:
                        # Limpa cada célula da linha, mantendo campos vazios
                        row_limpa = [limpar_texto(cell) for cell in row]
                        dados_extraidos.append(row_limpa)
        
        print(f"Relatório de Processamento do PDF:")
        print(f"- Total de páginas no documento: {total_paginas}")
        print(f"- Páginas com tabelas identificadas: {paginas_com_tabela}")
    
    return dados_extraidos

# Caminho do PDF
pdf_path = "anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
output_csv = "Teste_Vitor_Arruda.csv"
output_zip = "Teste_Vitor_Arruda.zip"

# Colunas do DataFrame
colunas = ["PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]

# Extração e processamento dos dados
dados_extraidos = extrair_tabela_pdf(pdf_path)
df = pd.DataFrame(dados_extraidos, columns=colunas)

# Substitui abreviações apenas para OD e AMB
df["OD"] = df["OD"].replace(abreviacoes)
df["AMB"] = df["AMB"].replace(abreviacoes)

# Salva CSV mantendo todos os campos, inclusive vazios
df.to_csv(output_csv, index=False, encoding="utf-8-sig", sep=";", na_rep="")

# Compacta em ZIP
with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(output_csv)

print("\nProcesso concluído. Arquivo ZIP gerado!")