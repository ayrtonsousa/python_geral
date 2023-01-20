# Implemente a função count_numbers que aceita uma lista classificada de números inteiros exclusivos e, 
# de forma eficiente  em relação ao tempo usado, conta o número de elementos da lista que são menores que o parâmetro less_than .

#Por exemplo, count_numbers([1, 3, 5, 7], 4) deve retornar 2 porque há dois elementos de lista menores que 4.

def count_numbers(sorted_list, less_than):
    #return len(list(filter(lambda x: x < less_than, sorted_list)))
    return  len([item for item in sorted_list if item < less_than])

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2