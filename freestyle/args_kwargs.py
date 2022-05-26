def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(1,2,3)


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)