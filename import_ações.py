import requests

# Definir a data da negociação
data = "2024-01-11"

# Definir a URL da API
url = "https://www.alphavantage.co/query?function=SYMBOL_LOOKUP&symbol=ABEV3&outputsize=full&apikey=E58NPINRO0HQVEN7"

# Fazer a solicitação HTTP
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:

    # Ler o resultado como um JSON
    data = response.json()

    # Extrair os símbolos das ações
    symbols = data["Symbols"][0]["Symbol"]

else:

    print("Erro ao acessar a API")

# Imprimir os símbolos das ações
print(symbols)

data