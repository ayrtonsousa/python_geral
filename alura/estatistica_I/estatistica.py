import statistics
from scipy import stats

#media
lista = [1,2,3,4,1,2,4,3]
media = statistics.median(lista)
print('Media', media)
print(stats.normaltest(lista))





