import pandas as pd

# Função para extrair campos com base nas posições iniciais e finais
def extrair_campos(linha, inicio_campo1, fim_campo1, inicio_campo2, fim_campo2):
    campo1 = linha[inicio_campo1 - 1:fim_campo1].strip()
    campo2 = linha[inicio_campo2 - 1:fim_campo2].strip()
    return campo1, campo2

# Especifique as posições iniciais e finais dos campos
inicio_campo1 = 3
fim_campo1 = 10
inicio_campo2 = 171
fim_campo2 = 188

# Crie listas para armazenar os valores de cada campo
campo1_lista = []
campo2_lista = []

# Abra o arquivo
with open('C:\TCC\HISTCOT\COTAHIST_A2002.TXT', 'r', encoding='latin1') as arquivo:

    # Itere sobre as linhas do arquivo
    for linha in arquivo:
        # Extraia os valores usando as posições iniciais e finais
        campo1, campo2 = extrair_campos(linha, inicio_campo1, fim_campo1, inicio_campo2, fim_campo2)

        # Adicione os valores às listas
        campo1_lista.append(campo1)
        campo2_lista.append(campo2)

# Crie o DataFrame do pandas
df = pd.DataFrame({
    'Data': campo1_lista,
    'Volume': campo2_lista
})

df['Volume'] = pd.to_numeric(df['Volume'])
df.dtypes

df_sum = df.groupby('Data')['Volume'].sum().reset_index()
pd.options.display.float_format = '{:,.2f}'.format

df_sum.to_excel('A2002.xlsx', index=False)
