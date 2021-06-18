# Thays Rodrigues 
# SET 2 - Problema 2.1


def square(numero):
    return numero**2 


def fourth_power(numero):
    return square(square(numero))


def perfect_square(numero):
    raiz = (numero ** 0.5)
    raiz = int(raiz)

    if raiz ** 2 == numero:
        return True
    else:
        return False

