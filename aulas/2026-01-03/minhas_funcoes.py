from datetime import date

def potencia (base, expoente):
    return base ** expoente

def somar (numero1, numero2):
    return numero1 + numero2

def subtrair (numero1, numero2):
    return numero1 - numero2

def multiplicar (numero1, numero2):
    return numero1 * numero2

def dividir (numero1, numero2):
    return (numero1 / numero2 if numero2 != 0 else "error")

def calcular_idade (data_nascimento: date) -> int:
    hoje = date.today()
    
    idade = hoje.year - data_nascimento.year
    
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day): idade -=1
    
    return idade