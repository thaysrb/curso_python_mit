# Thays Rodrigues 
# SET 3 - Problema 3_7

def hailstone_sequence(a_0):
    sequencia = []
    sequencia.append(a_0) 
    a = a_0

    while a > 1:
        if a % 2 == 0:
            a = a / 2
            sequencia.append(a)
        else:
            a = 3 * a + 1
            sequencia.append(a)
    return sequencia

