import pandas as pd
import os

# Diretório onde estão os arquivos Excel
diretorio = 'C:\TCC\SUM'

# Nome do arquivo de saída
arquivo_saida = 'b3_23anos.xlsx'

# Lista para armazenar os DataFrames de cada arquivo Excel
dfs = []

# Loop pelos arquivos no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.xlsx'):
        # Caminho completo do arquivo
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Leitura do arquivo Excel e armazenamento do DataFrame na lista
        df = pd.read_excel(caminho_arquivo)
        dfs.append(df)

# Concatenação dos DataFrames
df_final = pd.concat(dfs, ignore_index=True)

# Salva o DataFrame concatenado em um novo arquivo Excel
df_final.to_excel(arquivo_saida, index=False)

print(f'Append concluído. Resultado salvo em {arquivo_saida}')
