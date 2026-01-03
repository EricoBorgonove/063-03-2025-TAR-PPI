def media_3_numeros_simples ():
    numero1 = int (input("Digite o 1 numero: "))
    numero2 = int (input("Digite o 2 numero: "))
    numero3 = int (input("Digite o 3 numero: "))
    
    media = (numero1 + numero2 + numero3) /3
    
    print (f"A média entre {numero1}, {numero2} e {numero3} é {media}")
    
def media_3_numeros_com_parametros (numero1, numero2, numero3):

    media = (numero1 + numero2 + numero3) /3
    
    print (f"A média entre {numero1}, {numero2} e {numero3} é {media}")
    
def media_3_numeros_com_parametros_retorno (numero1, numero2, numero3):

    media = (numero1 + numero2 + numero3) /3
    
    return media
    # return (numero1 + numero2 + numero3) /3


n1 = int (input("Digite o 1 numero: "))
n2 = int (input("Digite o 2 numero: "))
n3 = int (input("Digite o 3 numero: "))

# media_3_numeros_simples()
# media_3_numeros_com_parametros(n1, n2, n3)
md = media_3_numeros_com_parametros_retorno (n1, n2, n3)
print (f"A média entre {n1}, {n2} e {n3} é {md}")