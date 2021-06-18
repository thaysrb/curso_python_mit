# Thays Rodrigues 
# SET 3 - Problema 3_4

def lend_money(debts, person, amount):
    if person in debts.keys():
        debts[person].append(amount)
    else:
        debts[person] = [amount]
    return None

def amount_owed_by(debts, person):
    total = 0
    if person in debts:
        for valor in debts[person]:
            total += valor
        return total
    else: 
        return 0

def total_amount_owed(debts):
    total = 0
    for valor in debts.values():
        for valor_devido in valor:
            total += valor_devido
    return total




