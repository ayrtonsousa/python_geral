#Como parte do planejador de rotas, o método route_exists  é usado como um filtro rápido se o destino for alcançável,
# antes de usar procedimentos computacionais mais intensivos para encontrar a rota ideal.

#As estradas no mapa são rasterizadas e produzem uma matriz de valores booleanos - True se a estrada estiver presente ou False se não estiver.
# As estradas na matriz são conectadas apenas se a estrada estiver imediatamente à esquerda, à direita, abaixo ou acima dela.

#Conclua o método route_exists  para que ele retorne True se o destino for alcançável ou False se não for.
# Os parâmetros from_row e from_column  são a linha e coluna inicial no map_matrix . O to_row  e to_column  são a linha e a coluna de destino no map_matrix .
# O parâmetro map_matrix  é a matriz acima mencionada produzida a partir do mapa.

#Por exemplo, para o mapa rasterizado fornecido, o código abaixo deve retornar True , pois o destino é alcançável:

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited = [[False for i in range(len(map_matrix[0]))] for j in range(len(map_matrix))]
    
    def route_exists2(from_row, from_column, to_row, to_column, map_matrix):
        if from_row < 0 or from_row >= len(map_matrix) or from_column < 0 or from_column >= len(map_matrix[0]) or visited[from_row][from_column] == True:
            return False

        if map_matrix[from_row][from_column]:
            visited[from_row][from_column] = True

            if from_row == to_row and from_column == to_column:
                return True
            return (route_exists2(from_row-1, from_column, to_row, to_column, map_matrix) or
                    route_exists2(from_row, from_column-1, to_row, to_column, map_matrix) or
                    route_exists2(from_row, from_column+1, to_row, to_column, map_matrix) or
                    route_exists2(from_row+1, from_column, to_row, to_column, map_matrix))

    if route_exists2(from_row, from_column, to_row, to_column, map_matrix):
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ]
    
    print(route_exists(0, 0, 2, 2, map_matrix))

