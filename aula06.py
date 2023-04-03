import string as st
#alphabeto=['1','2','3','D','E','F','G','H','I','J','L','K','M','N','O','P','Q','R','S','T','U','V','X','Y','W','Z']
letras = st.ascii_uppercase
alphabeto =list(letras)
def mostrar():
    for indice in range(len(alphabeto)):
        contador=0
        linha=""
        while contador<=indice:
            linha+=alphabeto[indice]
            contador+=1
            
        print(linha)

        

mostrar()
