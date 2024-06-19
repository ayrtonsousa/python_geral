from dominio import Usuario, Lance, Leilao


ayrton = Usuario('Ayrton', 500.0)
ariston = Usuario('Ariston', 500.0)

lance_do_ayrton = Lance(ayrton, 100.0)
lance_do_ariston = Lance(ariston, 150.0)

leilao = Leilao('Xbox One')

leilao.propoe(lance_do_ayrton)
leilao.propoe(lance_do_ariston)


for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')


print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')