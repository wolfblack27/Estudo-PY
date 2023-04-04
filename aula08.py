
#classes python : Classe com parametros personalizados

class TV:
    def __init__(self, tela, resolucao, fabricante, preco):
        self.tela = tela
        self.resolucao = resolucao
        self.fabricante = fabricante
        self.preco = preco
        self.fotos = []
        self.descricao = f'TV {resolucao} {tela}" - {fabricante}'

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def editar_fotos(self):
        pass

    def editar_descricao(self):
        pass


tv_1 = TV(43, 'FullHD', 'Samsung', 2400)
tv_2 = TV(50, '4K', 'LG', 3200)
print(tv_2.descricao)