import shelve2 as shelve

#salva arquivos em shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

#abri arquivos shelve
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

#passar como list
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()