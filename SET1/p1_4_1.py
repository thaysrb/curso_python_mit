# Thays Rodrigues 
# SET 1 - Problema 4 parte 1

poly = [0, 0, 1/2]
out = [] # Criando out como lista vazia 

for expoente in range(len(poly)):
    elemento = poly[expoente]
    if expoente  == 0:
        derivada = 0
    if expoente == 1:
        derivada = elemento
        out.append(derivada)
    if expoente > 1:
        derivada = expoente * elemento
        out.append(derivada)

print(out)