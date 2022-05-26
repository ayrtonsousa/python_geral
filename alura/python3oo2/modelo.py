class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    #sempre quando alguem acessar o valor
    def nome(self):
        return self._nome

    @nome.setter
    #sempre quando alguem muda o valor
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - Ano:{self.ano} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - Ano:{self.ano} - Duração:{self.duracao} min - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano:{self.ano} - Temporadas:{self.temporadas} - Likes: {self._likes}'  


class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    #Torna objeto iteravel
    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
batman = Filme('batman - bavaleito das trevas', 2008, 120)
spiderman = Serie('homem-aranha - amigo da vizinhança', 2018, 1)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

batman.dar_likes()
batman.dar_likes()
batman.dar_likes()

spiderman.dar_likes()
spiderman.dar_likes()


filmes_e_series = [vingadores, atlanta, spiderman, batman]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da Lista: {len(playlist_fim_de_semana)}')

for minha_playlist in playlist_fim_de_semana:
    print(minha_playlist)

print(f'Existe? {vingadores in playlist_fim_de_semana}')

