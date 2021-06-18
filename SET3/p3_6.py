# Thays Rodrigues 
# SET 3 - Problema 3_6

def binary_tree_max(tree):
    if tree['children'] == []:
        return tree['value']
    return max([binary_tree_max(tree['children'][0]),binary_tree_max(tree['children'][1]),tree['value']])

def tree_max(tree):
    valores = [tree['value']]
    for children in tree['children']:
        valores.append(tree_max(children))
    return max(valores)

