# Escreva uma função que, ao receber uma lista e uma soma alvo, retorne, de  forma eficiente  em relação ao tempo usado, 
# dois índices distintos  baseados em zero de quaisquer dois dos números, cuja soma é igual à soma alvo.
# Se não houver dois números, a função deve retornar None .

# Por exemplo, find_two_sum([3, 1, 5, 7, 5, 9], 10) deve retornar uma única tupla contendo qualquer um dos seguintes pares de índices:

# 0 e 3 (ou 3 e 0) como 3 + 7 = 10
# 1 e 5 (ou 5 e 1) como 1 + 9 = 10
# 2 e 4 (ou 4 e 2) como 5 + 5 = 10

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    
    for index in range(len(numbers)):

        for index_ in range(len(numbers)):

            if numbers[index] + numbers[index_] == target_sum:
                return (index, index_)            

    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
