#Classes: sobrecarga de métodos (Polimorfirmo)

class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


    def atacar(self, alvo):
        pass

    def fugir(self, destino):
        pass
    
class PassaroAerreo(Passaro):
        
    pass