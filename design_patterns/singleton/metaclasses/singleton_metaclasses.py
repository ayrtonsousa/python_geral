# Metaclasses com singleton


class MetaSingleTon(type):

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleTon, cls).__call__(*args, **kwargs)
        return cls.__instances


class Logger(metaclass=MetaSingleTon):
    ...


log1 = Logger()
print(f'Log 1: {id(log1)}')

log2 = Logger()
print(f'Log 2: {id(log2)}')