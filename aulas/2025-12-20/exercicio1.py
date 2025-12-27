# Escreva um programa que pergunte a velocidade de um carro. 
# Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário 
# foi multado. Nesse caso, exiba o valor da multa, cobrando 
# R$5 por cada Km acima da velocidade permitida.  

velocidade = float (input ("Digite a Velocidade do Carro: "))

if velocidade > 80:
    print ("Você foi Multado.")
    print ("O valor da multa é ", (velocidade - 80 )*5)
else:
    print ("Você não foi multado")
    
print ("fim")