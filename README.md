# Teste - IntuitiveCare

Este repositório contém os testes técnicos realizados para a vaga na IntuitiveCare. Os testes abordam diferentes áreas, como Web Scraping, Transformação de Dados, Banco de Dados e APIs.

## 📦 Estrutura do Projeto

A estrutura de diretórios do repositório está organizada da seguinte forma:
```
├── README.md # Documentação do projeto
├── web_scraping/ # Scripts para o teste de Web Scraping
│    ├── scraping.py # Código para realizar o web scraping
│    ├── requirements.txt # Dependências para o Web Scraping
├── data_transformation/ # Scripts para o teste de Transformação de Dados
│    ├── transform.py # Código para transformar os dados extraídos
│    ├── requirements.txt # Dependências para Transformação de Dados
├── database/ # Scripts para o teste de Banco de Dados
│    ├── scripts.sql # Consultas SQL para importar e consultar dados
├── api/ # Scripts para o teste de API
│    ├── server.py # Servidor em Python
├── frontend/ # Frontend em Vue.js
├── tests/ # Testes unitários e de integração
│    ├── test_scraping.py # Testes para o Web Scraping
│    ├── test_transform.py # Testes para a transformação de dados
└── .gitignore # Arquivos a serem ignorados pelo Git ## Como rodar os testes
```

1. Clone este repositório:
   ```bash
   git clone https://github.com/VitorArruda7/intuitivecare-testes.git

2. Instale as dependências para os scripts de Python:
cd web_scraping
pip install -r requirements.txt

cd ../data_transformation
pip install -r requirements.txt

3. Para rodar o web scraping:
python web_scraping/scraping.py

4. Para rodar a transformação de dados:
python data_transformation/transform.py

5. Para rodar os testes: 
pytest

## 📍 Acessando a API

- **A API está ativamente rodando na AWS**
- Podemos realizar uma busca por Unimed por exemplo:

- **```http://15.228.149.143:5000/busca?q=Unimed```**

**Parâmetros da requisição**:
- **q**: Palavra-chave para buscar na base de dados das operadoras.
- Exemplo: Para buscar por "operadora", use `q=operadora`.

**Exemplo de requisição**:
- **URL completa**:
  ```
  http://15.228.149.143:5000/busca?q=operadora
  ```

Isso retornará uma lista das operadoras que correspondem à palavra-chave "operadora".

- A coleção Postman pode ser encontrada dentro do diretório da API

⚙️ Dependências:
- Python 3.11.9

- Vue.js

- MySQL 8+ ou PostgreSQL 10+

Observações:
- As queries SQL estão preparadas para MySQL ou PostgreSQL.

- O frontend foi feito utilizando Vue.js, com integração ao backend em Python.
