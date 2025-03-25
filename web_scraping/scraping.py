import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

def baixar_anexos():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Erro ao acessar a página.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    anexos = []
    for link in links:
        if "Anexo" in link.text and link["href"].endswith(".pdf"):
            anexos.append(link["href"])
    
    if not anexos:
        print("Nenhum anexo encontrado.")
        return
    
    os.makedirs("anexos", exist_ok=True)
    arquivos_baixados = []
    
    for anexo in anexos:
        nome_arquivo = anexo.split("/")[-1]
        caminho_arquivo = os.path.join("anexos", nome_arquivo)
        
        with open(caminho_arquivo, "wb") as file:
            file.write(requests.get(anexo).content)
            arquivos_baixados.append(caminho_arquivo)
        
        print(f"Baixado: {nome_arquivo}")
    
    return arquivos_baixados

def compactar_anexos(arquivos):
    zip_filename = "anexos.zip"
    
    with ZipFile(zip_filename, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
    
    print(f"Arquivos compactados em {zip_filename}")

def main():
    arquivos = baixar_anexos()
    if arquivos:
        compactar_anexos(arquivos)

if __name__ == "__main__":
    main()