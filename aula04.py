#Estrutura de selecao Encadeada

""" Exemplo 01
media = int(input("Digite a Média:"))

if media>=6:
    print("Aprovado")

elif media<=3:
    print("Reprovado")

else:
    print("Exame")"""

"""Exemplo 02"""

sb = float(input("Digite o salario bruto:"))
tempo = int(input("Digite o tempo de empréstimo:"))
emprestimo = float(input("Valor do Emprestimo:"))

if sb>2000:
    if tempo>2:
        juros = emprestimo*0.15
    else:
        juros=emprestimo*0.20
    
    print(f'Valor total: {juros+emprestimo}')

else:
    print("Reprovado")