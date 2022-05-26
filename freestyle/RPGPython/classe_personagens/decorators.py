from functools import partial, wraps


def checa_energia(func=None, *, custo_energia):
    if func is None:
        return partial(checa_energia, custo_energia=custo_energia)

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result_func = func(self, *args, **kwargs)
        if self.energia >= custo_energia:
            self.energia -= custo_energia
            return result_func
        else:
            return  f'Sem energia suficiente: {self.energia}'
    return wrapper