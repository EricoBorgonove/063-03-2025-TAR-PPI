# leiam numeros da tela até o usuário digitar o numero 17
# então mostrem a quantidade de numeros lidos, a média e 
# a quantidade de numeros pares, impares e zeros

numero = None
qtd_numero = 0
soma_numero = 0
qtd_zero = 0
qtd_par = 0
qtd_impar = 0

while numero != 17:
    numero = int (input ("Digite um numero: "))
    if numero != 17:
        qtd_numero += 1
        soma_numero += numero
        if numero == 0:
            qtd_zero += 1
        elif numero % 2 == 0:
            qtd_par += 1
        else: 
            qtd_impar += 1
    
if qtd_numero == 0:
    print ("Não há números a exibir")
else:
    media_numero = soma_numero / qtd_numero
    print ("Qtd Numero: ", qtd_numero)
    print ("Soma Numero: ", soma_numero)
    print ("Media: ", media_numero)
    print ("Qtd Zeros: ", qtd_zero)
    print ("Qtd pares: ", qtd_par)
    print ("Qtd impar ", qtd_impar)
    
