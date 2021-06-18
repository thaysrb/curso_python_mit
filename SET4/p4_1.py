# Thays Rodrigues 
# SET 4 - Problema 4_1

class Warehouse:
    def __init__(self):
        self.estoque = {}

    def lookup(self, item):
        if item in self.estoque.keys(): return self.estoque[item]
        return 0
        
    def process(self, operacao):
        warehouse_process(self.estoque, operacao)
    
    

def warehouse_process(stock, transaction):
    if transaction[0] == 'ship':
        if transaction[1] in stock.keys():
            if transaction[2] < stock[transaction[1]]: stock[transaction[1]] = stock[transaction[1]] - transaction[2]
            else:
                print("not enough")
                stock[transaction[1]] = 0 
    else:
        if transaction[1] not in stock.keys(): stock[transaction[1]] = transaction[2]
        else: stock[transaction[1]] = stock[transaction[1]] + transaction[2]