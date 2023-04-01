n1 = int(input("Digite uma numero maior que 0: \n"))
n2 = int(input("Digite uma numero maior que 0: \n"))



if (n1>=0) and (n1<n2):

    print(f'Numeros pares de: {n1} até {n2}' )
   
    while n1<=n2:

        if(n1%2==0):
            print(n1)

        n1+=1
    



else:
    print('nao faça')


#print(f'numero (1)foi: {n1}  numero (2): {n2}')

