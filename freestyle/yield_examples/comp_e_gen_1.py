# artigo https://medium.com/@bernardo.costa/quando-usar-o-yield-no-python-ebae18b144ba 

# list comprehension
list_compr = [x for x in range(10)]
print(list_compr)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]

# list generator
list_gener = (x for x in range(10))
print(list_gener)
# >> <generator object <genexpr> at 0x7fcd403145c8>

print(next(list_gener))
# >> 0

for i in list_gener:
  print(i)
## >> 1, 2, ..., 9