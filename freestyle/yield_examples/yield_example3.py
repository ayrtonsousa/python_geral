def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fib()
print(next(fib_gen))


# O uso do yield pode ocasionar um aumento no tempo de processamento, visto que o código vai ficar toda hora parando para gerar o próximo elemento, então,
# modele-o bem para o seu caso de uso;
# Abrir grandes arquivos para processá-los em partes é um uso bem interessante, seguindo a linha dos exemplos que dei aqui;
# Um caso elegante é quando temos uma sequência que cresce indefinidamente, conforme o uso, onde podemos ir gerando os valores sob demanda com yield;
# Cheguei a ver alguns exemplos de paginação de queries com yield, seguindo uma ideia parecida com a divisão de chunks que mostrei, então,
# mantenha isso no radar.