#Estudo dos parametros *args e **kweargs

"""Usamos *args quando temos parametros não pocisionais, ou seja, parametros 
com estrutura parametro=valor

"""
#exemplo:

def somarnumeros(*args):
    soma=0
    for n in args:
        soma+=n
    print(soma)


somarnumeros(1,2,3,4,5)

#exemplo kweargs

def atributos(**kweargs):
    
    print(kweargs['nome'])
    print(kweargs['idade'])
    print(kweargs['altura'])

    pass

atributos(nome='thiago',idade=35, altura=1.74)


from requisicaocripto import fear_and_greed

response=fear_and_greed(limite=2,formato ='json',date_format='world')
"""
{'name': 'Fear and Greed Index', 
    'data': [
        {'value': '48', 'value_classification': 'Neutral', 'timestamp': '14-05-2023', 'time_until_update': '-1684014484'},
          {'value': '48', 'value_classification': 'Neutral', 'timestamp': '13-05-2023'}
        ],
    'metadata': {'error': None}}"""

for dicionario in response['data']:
    print(f'Valor:{dicionario["value"]} Classificação: {dicionario["value_classification"]}')
