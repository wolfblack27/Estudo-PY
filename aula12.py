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