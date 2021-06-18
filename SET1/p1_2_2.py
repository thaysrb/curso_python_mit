# Thays Rodrigues 
# SET 1 - Problema 2 Parte 2

# multiplcar todos os numeros da lista entre eles 
# raiz de n (numero elementos da lista)
numbers = [2, 7, 3, 9, 13]
mult = None

if numbers == []:
    out = None

for number in numbers:
    if mult == None:
        mult = number
    
    else:
        mult = mult * number

out = (mult)**(1/len(numbers))
print(out)
