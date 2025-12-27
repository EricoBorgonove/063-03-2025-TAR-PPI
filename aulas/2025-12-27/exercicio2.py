# Gere uma sequência de números de 1 a 100, substituindo múltiplos
# de 3 por "Fizz" e múltiplos de 5 por "Buzz".

for numero in range (1, 101):
    if numero %3 == 0 and numero % 5 == 0:
        print ('Fizz / Buzz')
    elif numero %3 == 0:
        print ("Fizz")
    elif numero %5 == 0:
        print ("Buzz")
    else:
        print (numero)
        
