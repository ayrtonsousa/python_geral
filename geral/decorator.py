# 1 - funcao que decora
def decorador(funcao):
    #print(funcao.__name__)
    # 2 - funcao que executa funcao recebida e seus argumentos
    def interna(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("argumentos devem ser inteiros")
        return funcao(*args)
        
    return interna

# como se fosse decorador(soma(2,2))
@decorador
def soma(x, y):
    return x + y

@decorador
def div(x, y):
    return x / y

print(soma(2,2))
print(div(100,3))
#print(soma(2,'nao sou int'))
