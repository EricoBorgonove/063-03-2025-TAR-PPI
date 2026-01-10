nomes = ["Rafalel","Valmir","Denis", "Marcos", "Valmir", "Raimundo"]

# for i in range (0,len(nomes)):
#     if nomes[i] == "Valmir":
#         nomes.pop(i)
#     print (nomes)
#     input (f"posição do for: {i}")
    
# for indice, nome in enumerate(nomes):
#     print (nome)
#     print (indice)
    
#     input (f"posição do for: {indice}")
    
for indice, nome in enumerate(nomes):
    if nome == "Valmir":
        nomes.pop(indice)
    print (nomes)
    input (f"posição do for: {indice}")
    