# Faça um programa que possua uma função chamada potencia(), 
# que vai receber dois parâmetros numéricos (base e expoente) 
# e vai calcular o resultado da exponenciação. ​
# Ex: Potencia(5,2) vai calcular 5² = 25

def potencia (base, expoente):
    return base ** expoente

bs = float (input("Digite a Base: "))
ex = float (input ("Digite o expoente: "))

print (f"A potenciação entre {bs} e {ex} é {potencia(bs, ex)}")



