#Uma lista de reprodução é considerada uma lista de reprodução repetida se alguma das músicas contiver uma referência a uma música 
# anterior na lista de reprodução. Caso contrário, a lista de reprodução terminará com a última música que aponta para None .

#Implemente uma função is_repeating_playlist que,  eficientemente  em relação ao tempo usado, retorne true se uma lista de reprodução 
# for repetida ou false se não for.

#Por exemplo, o código a seguir imprime "True" quando as duas músicas apontam uma para a outra.


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        if self.name == self.next.next.name:
            self.next.next = None
            self.next = None
            return True
        


            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())
