import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

#Transformação Logarítmica
df['salario_log'] = np.logip(df['salario']) #logip é usado para evitar problemas com valores zero

print("\nDataFrame após transformação logarítmica no 'salario':\n", df.head())

#Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)

print("\nDataFrame após transformação Box-Cox no 'salario':\n", df.head())

#Codificação de Frequência de 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após codificação de frequência para 'estado':\n", df.head())

#Interações
df['Interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print("\nDataFrame após criação de interações entre 'idade' e 'numero_filhos':\n", df.head())