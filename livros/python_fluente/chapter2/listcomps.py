# listcomps servem para uma coisa: criar listas

symbols = '$¢£¥€¤'

# 2.1
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

#print(codes)

# 2.2
codes = [ord(symbol) for symbol in symbols]
#print(codes)

# 2.3
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
#print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
#print(beyond_ascii)

# exemplo mostra que NESSE caso o listcomps e mais rapido que com filter e map
# https://github.com/fluentpython/example-code/blob/master/02-array-seq/listcomp_speed.py

# 2.4 produto cartesiano usando listcomps
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))