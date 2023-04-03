#Estrutura de fluxo
#Faz a seleção de acordo com a condição inicial



""""Exemplo 01
idade = int(input("Digite a idade:"))

#Estrutura de seleção:
if idade>=18:
    print("Maior que 18")

else:
    print("Menor que 18")
"""

"""Exemplo 2 (Variavel maior, irá receber o maior salario e acrescentar 20%)"""

s1 =2000
s2 =3000
maior =0

if s1>s2:
    maior = s1*1.2
else:
    maior = s2*1.2

print(f'Novo salario:{maior}')
