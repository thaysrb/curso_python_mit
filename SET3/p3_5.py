# Thays Rodrigues 
# SET 3 - Problema 3_5

def approx_derivative(f, x, delta = 1e-6):
    return (f(x+delta) - f(x-delta)) / (2 * delta)

def approx_derivative_2(f, delta = 1e-6):
    def funcao(x):
        return (f(x+delta) - f(x-delta)) / (2 * delta)
    return funcao

def approx_integral(f, lo, hi, num_regions):
    high = (hi - lo) / num_regions
    sum_areas = 0

    areas = [(lo + k * high) for k in range(num_regions + 1)]
    results = [f(area) for area in areas]

    for i in range(1, num_regions):
        sum_areas += results[i]

    return (high / 2) * (results[0] + 2 * sum_areas + results[-1])