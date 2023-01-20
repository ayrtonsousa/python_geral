
# Onde funcao interior se aproveita do escopo da funcao exterior
def externa(lingua):
    linguas = {'pt': 'Olá', 'en': 'Hello', 'es': 'Hola'}

    def interna(nome):
        print(f"{linguas[lingua]} {nome}")
    return interna

func = externa('pt')
func('tinho')
func('cleiton')

func = externa('en')
func('Messi')