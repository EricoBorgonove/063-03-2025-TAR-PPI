from dados_faker_2000 import pessoas
from minhas_funcoes import calcular_idade
from datetime import date

# for pessoa in pessoas:
#     if pessoa['genero'] == 'Masculino':
#         print (f"Nome: {pessoa['nome']}")
        
for pessoa in pessoas:
    idade = calcular_idade(date.fromisoformat(pessoa['data_nascimento']))
    if idade >= 18:
        print (f"Nome: {pessoa['nome']}")
        

# for pessoa in pessoas:
#      print (f"Nome: {pessoa['nome']}")
     
# print (pessoas[27]['nome'])