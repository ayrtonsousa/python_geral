import pprint

#Retorna string utilizando pformat e cria ela em um novo arquivo
cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py','w')
fileObj.write('cats = '+pprint.pformat(cats)+'\n')
fileObj.close()