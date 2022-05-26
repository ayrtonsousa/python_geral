def verificaTelefone(text):
    if len(text) != 12:
        return False  # não e tamanho de telefone
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # nao e um codigo de area
    if text[3] != '-':
        return False  # nao tem o primeiro hifen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # nao tem os primeiros 3 digitos
    if text[7] != '-':
        return False  # nao tem o segundo hifen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # nao tem os ultimos 4 digitos
    return True  # "text" nao e um numero de telefone!

mensagem = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'

for i in range(len(mensagem)):
    chunk = mensagem[i:i+12]
    if verificaTelefone(chunk):
        print('Número de telefone encontrado:',chunk)
    print('Completo')