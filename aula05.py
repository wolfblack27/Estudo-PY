#Funções

def pontilhados(qtd):
    pontos=" "
    
    for i in range(qtd):
        pontos+="-"
        
    
    print(pontos)

def bem_vindo():
    pontilhados(15)
    print("Bem-Vindo")
    pontilhados(5)


def retornar_media(n1,n2,n3):
    media = (n1+n2+n3)/3
    return media

bem_vindo()
n1 = float(input("Digite o nota1:"))
n2 = float(input("Digite o nota2:"))
n3 = float(input("Digite o nota3:"))

pontilhados(5)
print(retornar_media(n1,n2,n3))
pontilhados(5)