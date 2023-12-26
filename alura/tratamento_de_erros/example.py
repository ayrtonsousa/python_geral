def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber somente argumentos inteiros")
    try:
        aux = dividendo // divisor
    except:
        print(f"Não foi possivel dividir {dividendo} por {divisor}")
        raise #faz o erro continuar a pilha de excepts

    return aux


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisao de 10 por {divisor} e {resultado}")


try:
    testa_divisao(0)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("tratamento generico")

print("Programa encerrado")


# Mais simples usando suppress, sem interromper o codigo
from contextlib import suppress

with suppress(ZeroDivisionError):
    result = 1 / 0
    print(result)

print("Programa novamente encerrado")