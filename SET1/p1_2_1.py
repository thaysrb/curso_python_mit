# Thays Rodrigues 
# SET 1 - Problema 2 Parte 1

# Somar números da lista 
# Dividir pela quantidade de números -> len(numbers)
numbers = [2, 7, 3, 9, 13]
soma = 0

if numbers == []:
    out = None

else: 
    for number in numbers:
        soma = soma + number

    out = soma / len(numbers)
    print(out)