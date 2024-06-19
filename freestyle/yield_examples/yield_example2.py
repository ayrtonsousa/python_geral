from sys import getsizeof

def generator_split(x, chuck_size):
  for i in range(0, len(x), chuck_size):
    yield x[i:i+chuck_size]

def process_chunk(chunk):
  pass

def save_processed(processed):
  pass

if __name__ == '__main__':
  one_million = 10**6
  x = [x for x in range(one_million)]
  gen = generator_split(x, 100)

  for chunk in gen:
    print(chunk)
    processed = process_chunk(chunk)
    save_processed(processed)

# Percebeu onde quero chegar? Estamos falando de momentos em que vale mais a pena gerar uma iteração do que carregar todos os dados em memória.