##classes com atributos privados

class TV:
    def __init__(self, tela, resolucao, fabricante, preco,local):
        self.__preco = preco
        self.__local = local

#  atributo preco
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

#atributo localizacao
    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self,novo_local):
        self.__local = novo_local


listtvs = [];
    
tv1 = TV(43,'Full HD','LG',1100,'B12')
tv2 = TV(40,'Full HD','LG',1000,'B12')
tv3 = TV(41,'Full HD','LG',1100,'B12')
tv4 = TV(33,'Full HD','LG',1000,'B12')
tv5 = TV(53,'Full HD','LG',1200,'B12')

listtvs.append(tv1)
listtvs.append(tv2)
listtvs.append(tv3)
listtvs.append(tv4)
listtvs.append(tv5)

for tv in listtvs:
    print(f'Localização: {tv.local} -- Preco: {tv.preco}')
