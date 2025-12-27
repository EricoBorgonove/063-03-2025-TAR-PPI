#Desenvolver um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa 
# e classifique seu estado de saúde com base nesse índice. 
# IMC = peso / (altura²)

peso = float (input ("Digite o seu peso: "))
altura = float (input ("Digite a sua altura"))

imc = peso / altura **2

print ("O seu IMC é:", imc)

if imc >=0 and imc < 18.5:
    print ("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print ("Peso normal")
elif imc >= 25 and imc < 30:
    print ("Sobrepeso")
elif imc >= 30 and imc < 35:
    print ("Obesidade grau 1")
elif imc >= 35 and imc <40:
    print ("Obesidade grau 2")
elif imc >=40:
    print ("você vai morrer")
else:
    print ("IMC incorreto")