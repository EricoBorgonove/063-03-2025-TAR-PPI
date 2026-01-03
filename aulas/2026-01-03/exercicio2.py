def calcular_media (numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) /3

def status_aluno (numero1, numero2, numero3):
    media = calcular_media (numero1, numero2, numero3)
    
    if media >= 0 and media <5:
        return "reprovado"
    elif media >=5 and media <7:
        return "recuperação"
    elif media >=7 and media <=10:
        return "aprovado"
    else:
        return "error"
    
nota1 = int (input("Digite a 1 nota: "))
nota2 = int (input("Digite a 2 nota: "))
nota3 = int (input("Digite a 3 nota: "))

print (f"O aluno está {status_aluno(nota1, nota2, nota3)}")


