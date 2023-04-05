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

    
tv1 = TV(43,'Full HD','LG',1200,'B12')
tv1.local = 'C12'
print(tv1.local)
