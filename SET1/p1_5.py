# Thays Rodrigues 
# SET 1 - Problema 5

size = 'small'
toppings = ['presunto', 'abacaxi']
preco_pizza = 0

if size == 'small':
    preco_pizza = 14
if size == 'medium':
    preco_pizza = 16
if size == 'large':
    preco_pizza = 18

for n in range(len(toppings)):
    recheio = toppings[n]
    m = len(recheio)
    porcentagem_recheio = (12 + n + m)/100
    preco_pizza = preco_pizza + porcentagem_recheio * preco_pizza

if 'bacon' in toppings:
    preco_pizza = preco_pizza + preco_pizza * 0.1

if 'anchovas' in toppings:
    preco_pizza = preco_pizza + preco_pizza * 0.1

print(preco_pizza)
out = preco_pizza

    