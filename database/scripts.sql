-- Configurações iniciais para permitir importação de arquivos locais
SET GLOBAL local_infile=1;

-- Seleciona o banco de dados para realizar as operações
USE intuitive_care_test;

-- Criação da tabela para armazenar demonstrações contábeis
-- Estrutura definida para compatibilidade com os arquivos CSV
-- Uso de UTF-8 para suportar caracteres especiais
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    data DATE,                    -- Data do registro contábil
    registro_ans VARCHAR(20),     -- Registro da Agência Nacional de Saúde
    codigo_conta VARCHAR(50),     -- Código da conta contábil
    descricao VARCHAR(255),       -- Descrição detalhada da conta
    valor_saldo_inicial DECIMAL(18,2),  -- Saldo inicial com precisão de 2 casas decimais
    valor_saldo_final DECIMAL(18,2)     -- Saldo final com precisão de 2 casas decimais
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Limpa a tabela antes de importar novos dados
-- Garante que não haverá dados duplicados de importações anteriores
TRUNCATE TABLE demonstracoes_contabeis;

-- Importação do 1º Trimestre de 2023
-- Tratamentos:
-- 1. Conversão de datas
-- 2. Substituição de vírgulas por pontos
-- 3. Remoção de espaços em branco
-- 4. Uso de UTF-8 para encoding correto
LOAD DATA INFILE './uploads/1T2023.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'   -- Separador de colunas
ENCLOSED BY '"'            -- Delimitador de texto
LINES TERMINATED BY '\n'   -- Finalizador de linhas
IGNORE 1 ROWS              -- Ignora o cabeçalho
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 2º Trimestre de 2023
LOAD DATA INFILE './uploads/2T2023.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 3º Trimestre de 2023
LOAD DATA INFILE './uploads/3T2023.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 4º Trimestre de 2023
LOAD DATA INFILE './uploads/4T2023.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 1º Trimestre de 2024
LOAD DATA INFILE './uploads/1T2024.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 2º Trimestre de 2024
LOAD DATA INFILE './uploads/2T2024.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 3º Trimestre de 2024
LOAD DATA INFILE './uploads/3T2024.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- Importação do 4º Trimestre de 2024
LOAD DATA INFILE './uploads/4T2024.csv' 
INTO TABLE demonstracoes_contabeis 
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, registro_ans, codigo_conta, descricao, 
 @valor_saldo_inicial, @valor_saldo_final)
SET
    data = IF(@data LIKE '%/%/%', STR_TO_DATE(@data, '%d/%m/%Y'), @data),
    valor_saldo_inicial = REPLACE(REPLACE(@valor_saldo_inicial, ',', '.'), ' ', ''),
    valor_saldo_final = REPLACE(REPLACE(@valor_saldo_final, ',', '.'), ' ', '');

-- View para análise das 10 operadoras com maiores despesas no último trimestre
-- Usa subquery para determinar automaticamente o último trimestre
CREATE OR REPLACE VIEW top_10_operadoras_trimestre AS
WITH UltimoTrimestre AS (
    SELECT 
        MAX(data) as data_max,
        YEAR(MAX(data)) as ano,
        QUARTER(MAX(data)) as trimestre
    FROM demonstracoes_contabeis
)
SELECT 
    registro_ans,                  -- Identificador da operadora
    SUM(valor_saldo_final) as total_despesas  -- Soma total de despesas
FROM 
    demonstracoes_contabeis,
    UltimoTrimestre
WHERE 
    YEAR(data) = ano AND 
    QUARTER(data) = trimestre AND
    descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS%MEDICO HOSPITALAR%'  -- Filtro específico para despesas médico-hospitalares
GROUP BY 
    registro_ans
ORDER BY 
    total_despesas DESC
LIMIT 10;  -- Limitado às 10 maiores

-- View para análise das 10 operadoras com maiores despesas no último ano
CREATE OR REPLACE VIEW top_10_operadoras_ano AS
WITH UltimoAno AS (
    SELECT 
        MAX(YEAR(data)) as ano
    FROM demonstracoes_contabeis
)
SELECT 
    registro_ans,                  -- Identificador da operadora
    SUM(valor_saldo_final) as total_despesas  -- Soma total de despesas
FROM 
    demonstracoes_contabeis,
    UltimoAno
WHERE 
    YEAR(data) = ano AND
    descricao LIKE '%EVENTOS/ SINISTROS CONHECIDOS%MEDICO HOSPITALAR%'  -- Filtro específico para despesas médico-hospitalares
GROUP BY 
    registro_ans
ORDER BY 
    total_despesas DESC
LIMIT 10;  -- Limitado às 10 maiores

-- Verificação da quantidade total de registros importados
SELECT COUNT(*) AS total_registros FROM demonstracoes_contabeis;

-- Consulta final para exibir os resultados das views
SELECT * FROM top_10_operadoras_trimestre;
SELECT * FROM top_10_operadoras_ano;