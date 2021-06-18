# Thays Rodrigues 
# SET 0 - Problema 3

kwh_used = 1000
consumo = kwh_used
conta = 0

if consumo >= 2500:
    consumo_prop = consumo - 2500
    tx = 2
    conta += consumo_prop * tx # conta = conta + (consumo_prop * tx)
    consumo -= consumo_prop # consumo = consumo - consumo_prop

if consumo > 1500 and consumo <= 2500:
    consumo_prop = consumo - 1500
    tx = 1.25
    conta += consumo_prop * tx # conta = conta + (consumo_prop * tx)
    consumo -= consumo_prop # consumo = consumo - consumo_prop

if consumo > 500 and consumo <= 1500:
    consumo_prop = consumo - 500
    tx = 0.74
    conta += consumo_prop * tx # conta = conta + (consumo_prop * tx)
    consumo -= consumo_prop # consumo = consumo - consumo_prop

if consumo <= 500:
    tx = 0.45
    conta += consumo * tx # conta = conta + (consumo_prop * tx)

txProporcional = conta * 0.2
out = conta + txProporcional
print(out)
