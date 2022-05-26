#adicionar '* ' ao texto
import pyperclip

#pega texto da area de transferencia
texto = pyperclip.paste()

#quebra por linha
linhas = texto.split('\n')

#adiciona valor ao inicio de cada loop
for i in range(len(linhas)):
    linhas[i] = '* ' + linhas[i]

linhas = ('\n').join(linhas)

print(linhas)