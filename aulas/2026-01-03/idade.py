from datetime import date
from minhas_funcoes import calcular_idade


dia_nas = int (input("Digite o dia que você nasceu: "))
mes_nas = int (input ("Digite o mes que você nasceu: "))
ano_nas = int (input ("Digite o ano que você nasceu: "))

# data_nascimento = date(ano_nas, mes_nas, dia_nas)
# print (data_nascimento)
idade = calcular_idade(date(ano_nas, mes_nas, dia_nas))

print (f"A sua idade é {idade}")