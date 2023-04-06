#Classes: sobrecarga de métodos (Polimorfirmo)

class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


    def atacar(self, alvo):
        print("Metodo classe mae")
        print(f'Executando {alvo}')
        print("Metodo de classe mae realizado")
        return 'Fim do metodo'

    def fugir(self, destino):
        pass
    
class PassaroAerreo(Passaro):
    def __init__(self, vida, ataque, defesa,companheiro):
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)
    
    def atacar(self, alvo):
        print("Metodo sobrecarga")
        print(f'Executando {alvo}')
        print("Metodo de sobrecarga realizado")
        return 'Fim do metodo'


class PassaroAquatico(Passaro):
    def __init__(self, vida, ataque, defesa,forcanado):
        self.forcanado = forcanado
        super().__init__(vida, ataque, defesa)
    
    def atacar(self, alvo):
        return super().atacar(alvo)


#Teste Classe:

aguia = PassaroAerreo(500,700,800,'thiago')
pinguin = PassaroAquatico(700,700,500,1000)

aguia.atacar('cobra')
pinguin.atacar('peixe')