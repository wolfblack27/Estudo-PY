import requests
"https://economia.awesomeapi.com.br/json/daily/BTC-USD/1"
"https://economia.awesomeapi.com.br/json/daily/BTC-BRL/1"
"https://economia.awesomeapi.com.br/json/daily/USD-BRL/1"

listaMoedas = ['BTC-USD','BTC-BRL','USD-BRL','BNB-USD']
moeda = int(input ("Qual moeda deseja informações: (0-BTC-USD) (1-BTC-BRL)"))
qtd = int(input("Dugute a quantidade de dias: "))
requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{listaMoedas[moeda]}/{qtd}')
dic_requicisao1 = requisicao.json()
dic_requicisao2 = dic_requicisao1[0]
print(dic_requicisao2['high'])

