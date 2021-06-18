# Thays Rodrigues 
# SET 2 - Problema 2.1

def prime(numero):
    count = 0
    if numero == 1 or numero == 0 or numero < 0:
        return False

    elif numero == 2:
        return True

    elif numero % 2 == 0:
        return False
    
    else:
        for multiplicaco in range(2,numero):
            if numero % multiplicaco == 0:
                count += 1
        if count == 0:
            return True
    
    return False

