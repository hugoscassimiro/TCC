import pandas_datareader as pdr
import datetime

# Defina a data de início e fim para o histórico
data_inicio = datetime.datetime(2000, 1, 1)
data_fim = datetime.datetime(2023, 12, 31)

# Escolha 'SELIC' como o código da série temporal do Banco Central do Brasil
codigo_selic = 'SELIC'

# Obtenha os dados usando o pandas_datareader
dados_selic = pdr.get_data_fred(codigo_selic, start=data_inicio, end=data_fim)

# Exportar para excel
dados_selic.to_excel('selic_24anos.xlsx', index=False)
