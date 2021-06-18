# Thays Rodrigues 
# SET 1 - Problema 6

p_d = 5

def coordenadas(p_d):
    lista =  []
    eixo = range(-int(p_d/2), int(p_d/2) + 1)

    for y in eixo:
        for x in eixo:
            lista.append([x, y])
    return lista

def distancia_etc(p_d, quadrado):
    distancia = (quadrado[0] ** 2 + quadrado[1] ** 2) ** (1/2)
    if distancia < p_d/2:
        return True
    else:
        return False

coordenadas_quadrado = coordenadas(p_d)
quantidade_quadrados = 0 

for quadrado in coordenadas_quadrado:
    avaliar = distancia_etc(p_d, quadrado)
    if avaliar == True:
        quantidade_quadrados += 1 

razao = quantidade_quadrados / len(coordenadas_quadrado)
out = razao * 4 
print(out)
 
