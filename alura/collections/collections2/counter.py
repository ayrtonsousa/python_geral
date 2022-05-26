from collections import Counter

texto1 = """
As batidas do seu coração por minuto, a temperatura registrada com o passar dos meses na cidade de São Paulo, o comportamento da bolsa de valores, a produção mensal de uma fábrica e o número de casos registrados de Covid-19 ao longo de toda a pandemia, são apenas alguns exemplos de séries temporais. De maneira objetiva, podemos pensar que uma série temporal são conjuntos de dados de um determinado evento coletados, de maneira sequencial, ao longo do tempo.

Estudar esse tipo de dado é fundamental na identificação de possíveis padrões e, assim, torna-se essencial na criação de modelos preditivos que têm como motor uma série temporal. Dito isso, pensando sob a perspectiva estratégica, não podemos dissociar essa análise ao planejamento de um negócio e à tomada de decisões mais acertadas, por exemplo.

Mas, parte do nosso problema é entender se o modelo preditivo que construímos está ajustado à base de dados e, para isso, precisamos medí-lo.

E a pergunta é: como podemos medir a qualidade do ajuste de um modelo de previsão para uma série temporal?
Para medir um modelo (seja ele qual for), vamos tentar medir e analisar os erros que ele apresenta, ou seja, vamos comparar Y e Ŷ (Y real e Y previsto, respectivamente) e dar atenção à esses resíduos.

Sendo assim, a seguir, apresentaremos 4 técnicas diferentes para aferir seu modelo de previsão para séries temporais:

Utilizamos essa medida em séries temporais, pois há casos em que o erro negativo pode zerar o positivo ou dar uma ideia de que o modelo é preciso. Mas aqui, medimos apenas a distância do valor real, independente de ser acima ou abaixo.
"""

texto2 = """
Dizemos que uma série temporal é sazonal quando os fenômenos que ocorrem durante o tempo se repetem a cada período idêntico de tempo, ou seja, fenômenos que ocorrem diariamente em uma certa hora, todos os dias, ou em um certo mês em todos os anos.

O conceito de sazonalidade acaba sendo intuitivo, mesmo se você nunca estudou esse assunto tecnicamente. Podemos ter a nítida sensação de que alguns produtos vendem mais em determinados períodos como, por exemplo, o açaí em uma barraca de praia é mais vendido em períodos quentes, como no verão, não é mesmo? E já outros produtos, tais como caldos quentes, sofrem quedas de venda nesses mesmos períodos. Podemos, ainda, exemplificar isso analisando o aumento das vendas de sorvete nos períodos do final do ano, nos meses de verão. Ou ainda, de roupas de frio nos meses de inverno.
É importante lembrar que a sazonalidade não é uma espécie de moda. Por exemplo, houve um aumento grande de vendas de um certo livro quando o seu autor falece (naturalmente ele é mais citado na mídia e nas redes sociais, e isso causaria um aumento nas vendas). Porém, não podemos considerar esse aumento como sazonal, já que ele não irá se repetir (pois o autor não vai falecer de novo).

Conseguimos classificar diferentes tipos de sazonalidade baseados nos períodos que elas ocorrem. Vamos analisar alguns exemplos:

Diária
Muitas pessoas têm comportamentos similares no período de um dia, criando assim um pico de consumo naqueles mesmos períodos. Vamos pensar num restaurante no centro comercial. Existe um pico de pessoas almoçando entre as 12:00 e as 14:00, que é o horário de almoço da maioria dos(as) funcionários(as) das empresas. Já uma academia tem seus picos durante a manhã porque as pessoas vão antes do trabalho e depois das 18:00 porque é quando as pessoas estão voltando do trabalho.

Semanal
Em alguns negócios temos comportamentos diferentes dentro da semana. Uma pizzaria, por exemplo, tem um grande pico de pedidos na sexta-feira, sábado e domingo. Já na segunda-feira quase não há pedidos, o que leva muitas pizzarias a nem abrirem nesse dia.

Mensal
Muitas lojas grandes de varejo sabem que os consumidores compram muito mais nos dias do pagamento. É por esse motivo, inclusive, que já programam algumas promoções para estimular o consumo dentro e fora desses períodos.
"""

def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))

    dez_mais_comuns = proporcoes.most_common(10)
    for letra, percentual in dez_mais_comuns:
        print("{} => {:.2f} %".format(letra, percentual * 100))

print("Texto 1")
analisa_frequencia_letras(texto1)
print("Texto 2")
analisa_frequencia_letras(texto2)