def other_math(number):
  print('do the math with:', number)
  
def gen_squares_in_interval(x, y):
  for i in range(x, y):
    # return i*i
    yield i*i

if __name__ == '__main__':

  x, y = (10, 20)
  
  #for _ in range(x, y):
  #  number = gen_squares_in_interval(x, y)
  #  other_math(number)
  for number in gen_squares_in_interval(x, y):
    other_math(number)

"""Perceba, o yield nesse código funciona mais ou menos como um return, entretanto, mantém salvo o contexto da função, 
e quando o for() de dentro do main itera novamente, a função gen_squares_in_interval() volta a ser chamada,
continuando sua execução de onde parou, mantendo o contexto da sua iteração, 
seguindo a sequência correta do range(x, y).
Ficou meio confuso? Troque o yield por return (altere o loop do main para ter uma lista no for()) e rode de novo.
Você verá que o resultado será sempre 100, pois o return não salva o contexto da função, executando-a "do zero" toda vez. Veja abaixo:
"""
