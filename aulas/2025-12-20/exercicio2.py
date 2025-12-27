#Escreva um programa que leia o ano de nascimento de um rapaz e 
# mostre a sua situação em relação ao alistamento militar. ​
#- Se estiver antes dos 18 anos, mostre em quantos anos faltam 
# para o alistamento. ​
#- Se já tiver depois dos 18 anos, mostre quantos anos já se 
# passaram do alistamento.
# resultado = verdade if condição else mentira

ano_nascimento = int (input("Digite o ano de Nascimento"))
ano_atual = 2025
idade = ano_atual - ano_nascimento

e_maior = True if idade>=18 else False

data_passada = (idade - 18) if e_maior else (18 - idade)

print ("Você tem ", idade, " anos de vida ", 
       (("e é maior de idade, já se passando ", data_passada, 
        " do alistamento")  if e_maior else (" e é menor de idade e faltam",
        data_passada, " para o seu alistamento")))