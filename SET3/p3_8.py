# Thays Rodrigues 
# SET 3 - Problema 3_7

def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    def f_composta_g(x): 
        return f(g(x))
    return f_composta_g