# Thays Rodrigues 
# SET 1 - Problema 1

interest_rate = 0.2

def dobra_valor (interest_rate):
    if interest_rate != 0:
        out = (72/(interest_rate * 100))
    else:
        out = "NEVER"
    return out 

out = round(dobra_valor(interest_rate))
print(out)