from collections import namedtuple

# 2.9 tuplas nomeadas
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.633, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

# 2.10 atributos e metodos de uma tupla nomeada
print(City._fields) # _fields exibe campos

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.123123, 77.208999))
delhi = City._make(delhi_data) # com _make possivel instanciar usando um iteravel City(*delhi_data) faria o msm
print(delhi._asdict()) # retorna um orderedDict para exibir de forma mais legivel
