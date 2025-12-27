#Leia a idade de 20 pessoas 
# e exiba quantas pessoas são maiores de idade 
# e a média de suas idades.
qtd_maior = 0
soma_maior = 0
media_maior = 0
for i in range (1,4):
    idade = int (input(f"Digite a  {i}  idade: "))
    if idade >= 18:
        qtd_maior += 1 # qtd_maior = qtd_maior + 1 
        soma_maior += idade
#validação
if qtd_maior == 0:
    print ("Não há pessoas maiores de idade")
else:
    media_maior = soma_maior / qtd_maior

    print ("Soma: ", soma_maior)
    print ("Quantidade: ", qtd_maior)
    print ("Média: ", media_maior)