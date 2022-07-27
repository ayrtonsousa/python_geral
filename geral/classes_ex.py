class Point:
    ...

class Point2:
    ...


p = Point()
p.z = 1995
p.y = 100

# tipo objeto
print(type(p))

# se e da instancia
print(isinstance(p, Point))
print(isinstance(p, Point2))

# se atributo existir
print(hasattr(p, 'z'))
print(hasattr(p, 'w'))

try:
    x = p.x
except AttributeError:
    print('Error attribute')