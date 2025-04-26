# intro_preparacao_dados.py
## Tratamento de Dados de Clientes

Este script realiza o tratamento e análise de um conjunto de dados de clientes contido no arquivo CSV `clientes-v2.csv`. O objetivo é limpar, analisar e salvar um novo arquivo CSV com os dados tratados.

## Descrição do Script

1. **Leitura do arquivo CSV**: O arquivo `clientes-v2.csv` é carregado em um DataFrame do Pandas.

2. **Exibição das primeiras e últimas linhas**: São exibidas as primeiras e últimas 5 linhas dos dados para uma visão geral inicial.

3. **Conversão de coluna de data**: A coluna `data` é convertida para o formato de data, utilizando o formato `'%d/%m/%Y'`. Caso algum valor seja inválido, ele é convertido para `NaT` (Not a Time).

4. **Análise de Dados Nulos**:
   - Exibe informações gerais sobre o DataFrame.
   - Verifica e exibe a quantidade de dados nulos em cada coluna.
   - Exibe a porcentagem de dados nulos por coluna.
   - Remove linhas com dados nulos e verifica a remoção.

5. **Análise de Dados Duplicados**:
   - Verifica a quantidade de linhas duplicadas no DataFrame.

6. **Análise de Dados Únicos**: Exibe o número de valores únicos por coluna.

7. **Estatísticas Descritivas**: Exibe estatísticas descritivas básicas (como média, desvio padrão, valores mínimo e máximo) para as colunas numéricas.

8. **Seleção de Colunas Relevantes**: Seleciona um subconjunto de colunas relevantes para análise:
   - `idade`, `data`, `estado`, `salario`, `nivel_educacao`, `numero_filhos`, `estado_civil`, `area_atuacao`

9. **Salvamento do Novo Arquivo**: O DataFrame tratado é salvo em um novo arquivo CSV chamado `clientes-v2-tratados.csv`.

## Como Usar

1. Certifique-se de ter o arquivo `clientes-v2.csv` no mesmo diretório do script ou forneça o caminho correto para o arquivo CSV.
2. Execute o script em um ambiente Python com a biblioteca Pandas instalada. Caso ainda não tenha o Pandas, instale com o comando:

   ```bash
   pip install pandas
# normalizacao_padronizacao.py
## Tratamento e Escalonamento de Dados de Clientes

Este script realiza o tratamento e escalonamento dos dados de um arquivo CSV (`clientes-v2-tratados.csv`). O objetivo é aplicar diferentes técnicas de escalonamento (Normalização e Padronização) para as colunas `idade` e `salario`.

## Descrição do Script

1. **Leitura do Arquivo CSV**: O arquivo `clientes-v2-tratados.csv` é carregado em um DataFrame do Pandas.

2. **Exclusão de Colunas**: As colunas `data`, `estado`, `nivel_educacao`, `numero_filhos`, `estado_civil` e `area_atuacao` são removidas, pois não serão utilizadas para o escalonamento.

3. **Aplicação de Escalonamento**:
   - **MinMaxScaler**: Aplica uma transformação linear, escalando os valores das colunas `idade` e `salario` para o intervalo de 0 a 1.
   - **MinMaxScaler (com intervalo customizado)**: Aplica a mesma transformação, mas com o intervalo ajustado para valores entre -1 e 1.
   - **StandardScaler**: Padroniza os dados, ajustando a média para 0 e o desvio padrão para 1.
   - **RobustScaler**: Escalona os dados utilizando a mediana e o intervalo interquartil (IQR), tornando-o mais robusto a outliers.

4. **Exibição dos Resultados**: Exibe as primeiras 15 linhas do DataFrame após a aplicação do escalonamento.

5. **Cálculo das Estatísticas**: Para cada técnica de escalonamento, são exibidas as estatísticas descritivas das colunas `idade` e `salario` (mínimo, máximo, média e desvio padrão).

## Como Usar

1. Certifique-se de ter o arquivo `clientes-v2-tratados.csv` no mesmo diretório do script ou forneça o caminho correto para o arquivo CSV.
2. Execute o script em um ambiente Python com as bibliotecas Pandas e Scikit-learn instaladas. Caso ainda não tenha essas bibliotecas, instale-as com os comandos:

   ```bash
   pip install scikit-learn
# codificacoes_variaveis_categoricas.py
## Codificação de Variáveis no Dataset de Clientes

Este script realiza diferentes técnicas de **codificação de variáveis** categóricas no conjunto de dados `clientes-v2-tratados.csv`, tornando-as adequadas para o uso em modelos de Machine Learning.

## Descrição do Script

1. **Leitura do Arquivo CSV**:
   - Carrega o dataset `clientes-v2-tratados.csv` utilizando Pandas.

2. **One-Hot Encoding (`estado_civil`)**:
   - Utiliza `pd.get_dummies()` para transformar a coluna `estado_civil` em múltiplas colunas binárias (0 ou 1).
   - **Objetivo**: Representar categorias de maneira que não introduza ordem implícita nos dados.

3. **Codificação Ordinal (`nivel_educacao_ordinal`)**:
   - Mapeia o nível de educação para números inteiros, respeitando uma ordem lógica:
     - `Ensino Fundamental`: 1
     - `Ensino Médio`: 2
     - `Ensino Superior`: 3
     - `Pós-Graduação`: 4
   - **Objetivo**: Preservar a hierarquia natural existente nas categorias.

4. **Codificação de Categorias (`area_atuacao_cod`)**:
   - Usa `.astype('category').cat.codes` para transformar a coluna `area_atuacao` em códigos numéricos.
   - **Objetivo**: Atribuir um número inteiro a cada categoria de forma simples.

5. **Label Encoding (`estado_cod`)**:
   - Utiliza `LabelEncoder` do Scikit-Learn para transformar a coluna `estado` em códigos numéricos.
   - **Objetivo**: Codificar rótulos sem criar múltiplas colunas (diferente do one-hot).

## Como Usar

1. Certifique-se de que o arquivo `clientes-v2-tratados.csv` esteja disponível no mesmo diretório do script.
2. Execute o script em um ambiente Python com as bibliotecas necessárias instaladas:

   ```bash
   pip install pandas scikit-learn
# transformacao_features.py
## Transformações e Engenharia de Atributos no Dataset de Clientes

Este script realiza **transformações estatísticas** e **engenharia de atributos** sobre o conjunto de dados `clientes-v2-tratados.csv`. As técnicas aplicadas visam melhorar a distribuição dos dados e criar novos atributos úteis para futuras análises ou modelos preditivos.

## Descrição do Script

1. **Leitura do Arquivo CSV**: 
   - O dataset `clientes-v2-tratados.csv` é carregado utilizando o Pandas.

2. **Transformação Logarítmica** (`salario_log`):
   - Aplicada ao atributo `salario` utilizando uma função de log segura (`log1p` — corrigir no código, veja Observação).
   - **Objetivo**: Reduzir a assimetria dos dados e lidar melhor com valores muito grandes ou distribuídos de forma exponencial.

3. **Transformação Box-Cox** (`salario_boxcox`):
   - Aplicada ao atributo `salario` somando 1 para evitar problemas com valores zero.
   - **Objetivo**: Tornar a distribuição dos dados mais próxima de uma distribuição normal (Gaussianização).

4. **Codificação de Frequência de `estado`** (`estado_freq`):
   - A coluna `estado` é codificada com base na frequência de ocorrência de cada valor.
   - **Objetivo**: Converter variáveis categóricas em numéricas, preservando a importância relativa de cada categoria.

5. **Criação de Interação** (`Interacao_idade_filhos`):
   - Geração de uma nova variável que é o produto de `idade` e `numero_filhos`.
   - **Objetivo**: Capturar relações entre idade e número de filhos que possam ser relevantes para análise.

## Como Usar

1. Certifique-se de ter o arquivo `clientes-v2-tratados.csv` no mesmo diretório do script.
2. Execute o script em um ambiente Python com as seguintes bibliotecas instaladas:

   ```bash
   pip install pandas numpy scipy
