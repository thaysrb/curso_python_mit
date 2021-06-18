# Thays Rodrigues 
# SET 2 - Problema 2.4


def largest_number(input_list):

    if input_list != []:
        best_so_far = float('-inf') 
        for numero in range(len(input_list)):
            current_num = input_list[numero]

            if current_num > best_so_far:
                best_so_far = current_num

        return best_so_far
    
    return None

def second_largest_number(input_list):

    if len(input_list) != 0 and len(input_list) != 1:
        best_so_far = second_best_so_far = float('-inf')

        for numero in input_list:
            if numero > second_best_so_far:
                if numero > best_so_far:
                    second_best_so_far = best_so_far
                    best_so_far = numero
                else:
                    second_best_so_far = numero
                    
        return second_best_so_far
    return None

