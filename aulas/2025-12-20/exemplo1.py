# operador ternário

ano_nascimento = int (input("Digite o ano de Nascimento"))
ano_atual = 2025
idade = ano_atual - ano_nascimento


# resultado = verdade if condição else mentira

maior_idade = True if idade >= 18 else False

pode_dirigir = "sim" if idade>=18 else "não"

if idade >= 18:
    pode_dirigir = "sim"
else:
    pode_dirigir = "não"