#Uma interface de usuário contém dois tipos de controles de entrada de usuário: TextInput ,
#  que aceita todos os caracteres e NumericInput , que aceita apenas dígitos.

#Implemente a classe TextInput que contém:

#Método  add(self, character) - adiciona o caractere dado ao valor atual
#Método get_value(self) - retorna o valor atual
#Implemente a classe NumericInput que:

#Herda TextInput
#Substitui o método add para que cada caractere não numérico seja ignorado
#por exemplo, o código a seguir deve gerar "10":

class TextInput:

    def __init__(self):
        self.value = ''

    def add(self, value):
        self.value += str(value)

    def get_value(self):
        return self.value
    
  
class NumericInput(TextInput):

    def add(self, value):
        if value.isnumeric():
            self.value += str(value)

if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())