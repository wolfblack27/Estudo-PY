#usando *(args) e **(Keyargs)#

key = "4564512hghg3dfdsfsdfsdfsd"
apiKey ="4545644fdshghghfsdfsfsdfsdfsdfdsfd"

def getKey():
    return key

def getapiKey():
    return apiKey


"Estudo do Args"
def calculoimposto(valor,*tributos):
    resultados =[]
    for v in tributos:
        resultados.append(valor*v)
        print(v)
        
    return resultados


"Estudos Keyargs"

def dados(nome,**dados):
    print(dados)
    return

