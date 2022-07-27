# Criar arquivo
f = open("teste.txt", "w+")
for i in range(5):
     f.write("Essa linha %d\r\n" % (i+1))
f.close()

# Editar arquivo
f = open("teste.txt", "a+")
f.write(f"Nova linha oi\n")
f.close()

# Ler arquivo usando with, mais recomendado que f.close()
with open("teste.txt", "r") as f:
    texto = f.read()
    print(texto)

# Deletar arquivo
import os
os.remove("teste.txt")
