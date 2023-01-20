#A  classe LeagueTable rastreia a pontuação de cada jogador em uma liga. Após cada jogo, o jogador registra sua pontuação com a função record_result  . 

#A classificação do jogador na liga é calculada usando a seguinte lógica:

#O jogador com a maior pontuação é classificado em primeiro lugar (rank 1). O jogador com a pontuação mais baixa é classificado por último.
#Se dois jogadores estiverem empatados na pontuação, o jogador que jogou menos partidas tem a classificação mais alta.
#Se dois jogadores estiverem empatados em pontuação e número de jogos disputados, 
# o jogador que estava em primeiro lugar na lista de jogadores tem a classificação mais alta.
#Implemente a função player_rank que retorna o jogador na classificação dada.

#Por exemplo:
#table = LeagueTable(['Mike', 'Chris', 'Arnold'])
#table.record_result('Mike', 2)
#table.record_result('Mike', 3)
#table.record_result('Arnold', 5)
#table.record_result('Chris', 5)
#print(table.player_rank(1))

#Todos os jogadores têm a mesma pontuação. No entanto, Arnold e Chris jogaram menos partidas que Mike e, como Chris está antes de Arnold na lista de jogadores, 
#ele está classificado em primeiro lugar. Portanto, o código acima deve exibir "Chris".

from collections import Counter, OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        self.standings = OrderedDict(sorted(self.standings.items(), key=lambda x:x[1]['games_played']))
        for index, value in enumerate(self.standings.keys()):
            if index == rank - 1:
                return value

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))