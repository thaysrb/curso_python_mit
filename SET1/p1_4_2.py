# Thays Rodrigues 
# SET 1 - Problema 4 parte 2
poly = [0, 0, 1/2]
out = [] # Criando out como lista vazia 
const = 'c'

for expoente in range(len(poly)):
    if expoente == 0:
        integral = const
        out.append(integral)

    elemento = poly[expoente]
    integral = elemento / (expoente + 1)
    out.append(integral)

