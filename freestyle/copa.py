from random import randint

pote1=[
    ['Catar','AS'],
    ['Brasil','SA'],
    ['Bélgica','EU'],
    ['França','EU'],
    ['Argentina','SA'],
    ['Inglaterra','EU'],
    ['Espanha','EU'],
    ['Portugal','EU']
]
pote2=[
    ['Holanda','EU'],
    ['Alemanha','EU'],
    ['Dinamarca','EU'],
    ['México','NA'],
    ['Estados Unidos','NA'],
    ['Suíça','EU'],
    ['Uruguai','SA'],
    ['Croácia','EU']
]
pote3=[
    ['Senegal','AF'],
    ['Irã','AS'],
    ['Japão','AS'],
    ['Sérvia','EU'],
    ['Polônia','EU'],
    ['Coreia do Sul','AS'],
    ['Marrocos','AF'],
    ['Tunísia','AF']
]
pote4=[
    ['Canadá','NA'],
    ['Equador','SA'],
    ['Arábia Saudita','AF'],
    ['Gana','AF'],
    ['Camarões','AF'],
    ['Peru','SA'],
    ['País de Gales','EU'],
    ['Costa Rica','NA']
]

grupos = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
}

# sorteia selecoes grupos    

for pote in [pote1, pote2, pote3, pote4]:
    
    sede = True

    for letra in ['A','B','C','D','E','F','G','H']:
        for pais in pote:
            if sede:
                index_pais = 0
                pais = pote[0]
                sede = False
            else:
                index_pais = randint(0,len(pote)-1)
                pais = pote[index_pais]       

            print(pais[0], ':' ,letra)
            # se primeiro do grupo
            if len(grupos[letra]) == 0:
                grupos[letra].append(pais)
                del pote[index_pais]
                break
            # checa se grupo esta cheio
            elif len(grupos[letra]) == 4:
                print('grupo cheio ja !')
                continue
            # checa se tem mais de 2 europeus
            elif pais[1] == 'EU':
                europeus = list(filter(lambda x: x[1] == 'EU', grupos[letra]))
                if len(europeus) == 2:
                    print('ja tem 2 europeus !')
                    continue
            # checa se pais não europeu ja tem outro representante
            else:
                paises_mesma_confederacao = list(filter(lambda x: x[1] == pais[1], grupos[letra]))
                if len(paises_mesma_confederacao) >= 1:
                    print('pais da mesma confederacao')
                    continue

            # remove do pote e adiciona ao grupo
            grupos[letra].append(pais)
            del pote[index_pais]
            break

print(grupos)
