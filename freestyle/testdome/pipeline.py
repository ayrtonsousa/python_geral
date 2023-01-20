#Como parte de um pipeline de processamento de dados, conclua a implementação do método de pipeline :

#O método pipeline deve aceitar um número variável de funções e deve retornar uma nova função que aceite um parâmetro  arg .
#A função retornada deve chamar a primeira função no pipeline com o parâmetro  arg e chamar a segunda função com o resultado da primeira função.
#A função retornada deve continuar chamando cada função do pipeline na ordem, seguindo o mesmo padrão, e retornar o valor da última função.
#Por exemplo, chamar pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2) e, em seguida, chamar a função retornada com 3 deve retornar 5.0.

def pipeline(*funcs):
    def helper(arg):
        for func in funcs:
            arg = func(arg)
        return arg
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0