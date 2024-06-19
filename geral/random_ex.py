import random


# random retorna entre 0.0 e 1 (exceto o 1)
print(random.random())

# randomico entre numeros
print(random.randint(1,5))

# random com range
print(random.randrange(0, 3))

# choice
print(random.choice(['SP','RJ','MG']))
print(random.choice(range(0,3)))

# random entre dados
lista1 = ['a', 'b', 'c', 'd', 'e', 'f']

print(random.choices(lista1))

# embaralha lista randomicamente
fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits)
print(fruits)