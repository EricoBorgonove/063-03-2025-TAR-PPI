# Faça um programa que possua uma função chamada potencia(), 
# que vai receber dois parâmetros numéricos (base e expoente) 
# e vai calcular o resultado da exponenciação. ​
# Ex: Potencia(5,2) vai calcular 5² = 25

# from minhas_funcoes import * (má prática, pois derruba a segurança)
#from minhas_funcoes import potencia
# from minhas_funcoes import somar

from minhas_funcoes import potencia, somar, subtrair, dividir, multiplicar

num1 = float (input("Digite o primeiro numero (Base): "))
num2 = float (input ("Digite o segundo numero (Expoente): "))

print (f"A potenciação entre base {num1} e expoente {num2} é {potencia(num1, num2)}")
print (f"A soma entre {num1} e {num2} é {somar(num1, num2)}")
print (f"A subtração entre {num1} e {num2} é {subtrair(num1, num2)}")
print (f"A multiplicação entre {num1} e {num2} é {multiplicar(num1, num2)}")
print ((f"A divisão entre {num1} e {num2} é {dividir(num1, num2)}") if num2 !=0 
            else f"Não existe divição entre {num1} e zero ")



