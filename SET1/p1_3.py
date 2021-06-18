# Thays Rodrigues 
# SET 1 - Problema 3

dividend = 7
divisor = 2

def divisao(dividend, divisor): 
    if dividend > 0 and divisor > 0:
        quociente = 0
        resto =  dividend
        while resto > divisor:
            resto -= divisor
            quociente += 1
    return quociente, resto

out = divisao(dividend, divisor)
print(out)