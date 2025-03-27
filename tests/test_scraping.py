import os
import pytest
from unittest.mock import patch, MagicMock
from web_scraping.scraping import baixar_anexos, compactar_anexos

@patch("web_scraping.scraping.requests.get")
def test_baixar_anexos(mock_requests_get):
    """Testa se os anexos são encontrados e baixados corretamente."""

    # Simulação da resposta da página HTML
    mock_html_response = MagicMock()
    mock_html_response.text = """
        <html>
            <body>
                <a href="https://example.com/Anexo1.pdf">Anexo 1</a>
                <a href="https://example.com/Anexo2.pdf">Anexo 2</a>
            </body>
        </html>
    """
    mock_html_response.status_code = 200

    # Configura o mock para a requisição da página HTML
    mock_pdf_response = MagicMock()
    mock_pdf_response.content = b"PDF FILE CONTENT"
    
    mock_requests_get.side_effect = [mock_html_response, mock_pdf_response, mock_pdf_response]

    arquivos = baixar_anexos()

    # Teste se a lista de arquivos não está vazia
    assert arquivos is not None, "A função deve retornar uma lista, não None"
    assert len(arquivos) == 2, "Devem ser baixados 2 arquivos"
    assert "Anexo1.pdf" in arquivos[0], "O primeiro arquivo deve ser 'Anexo1.pdf'"
    assert "Anexo2.pdf" in arquivos[1], "O segundo arquivo deve ser 'Anexo2.pdf'"

    # Limpeza dos arquivos baixados
    for arquivo in arquivos:
        os.remove(arquivo)

@patch("web_scraping.scraping.ZipFile")
def test_compactar_anexos(mock_zipfile):
    """Testa a compactação dos arquivos."""
    arquivos_mock = ["anexos/test1.pdf", "anexos/test2.pdf"]

    # Criar arquivos fictícios para teste
    os.makedirs("anexos", exist_ok=True)
    for arquivo in arquivos_mock:
        with open(arquivo, "wb") as f:
            f.write(b"mock data")

    compactar_anexos(arquivos_mock)

    # Verifica se o método de escrita foi chamado corretamente
    mock_zipfile.assert_called_with("anexos.zip", "w")

    # Limpeza
    if os.path.exists("anexos.zip"):
        os.remove("anexos.zip")
    for arquivo in arquivos_mock:
        if os.path.exists(arquivo):
            os.remove(arquivo)
    if os.path.exists("anexos") and not os.listdir("anexos"):
        os.rmdir("anexos")
