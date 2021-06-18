# Thays Rodrigues 
# SET 2 - Problema 2.3

def ndoors(numero):
    portas = []
    open_doors = []

    for i in range(0, numero):
        portas.append(False)
    
    for m in range(1, numero + 1):
        for k in range(0, numero):
            if (k + 1) % m == 0:
                if (portas[k]) == False:
                    portas[k] = True
                else:
                    portas[k] = False
    
    for k in range(0, numero):
        if portas[k] == True:
            open_doors.append(k + 1)
    
    return open_doors