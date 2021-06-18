# Thays Rodrigues 
# SET 3 - Problema 3_3

def dictmap(d, f):
    for chave in d:
        d[chave] = f(d[chave])
