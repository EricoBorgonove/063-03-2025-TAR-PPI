from faker import Faker
import random
from pprint import pformat

fake = Faker("pt_BR")

dados = []

for _ in range(2000):
    nascimento = fake.date_of_birth(minimum_age=18, maximum_age=70)

    registro = {
        "nome": fake.name(),
        "genero": random.choice(["Masculino", "Feminino"]),
        "cpf": fake.cpf(),
        "rg": fake.rg(),
        "data_nascimento": nascimento.isoformat(),
        "local_nascimento": fake.city(),
        "estado_nascimento": fake.state(),
        "can_drive": random.choice([True, False]),
        "can_vote": True,
        "matrimonial_state": random.choice(
            ["single", "married", "divorced", "widowed"]
        ),
        "degree": random.choice(
            ["High School", "Bachelor", "Master", "PhD"]
        )
    }

    dados.append(registro)

# gera arquivo Python bem formatado
with open("dados_faker_150.py", "w", encoding="utf-8") as f:
    f.write("# Arquivo gerado automaticamente com Faker\n")
    f.write("# Lista Python válida e indentada\n\n")
    f.write("dados = ")
    f.write(pformat(dados, indent=4, width=120))
    f.write("\n")

print("Arquivo dados_faker_150.py gerado com indentação correta!")
