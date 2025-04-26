import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print("\nDataFrame após codificação one-hot para 'estado_civil':\n", df.head())

educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
    
print("\nDataFrame após codificação ordinal para 'nivel_educacao':\n", df.head())

df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataFrame após tranformar 'area_atuacao' em códigos numéricos:\n", df.head())

label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print("\nDataFrame após aplicar LabelEncoder em 'estado':\n",df.head())