import numpy as np

class NumpyCreator:
    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        if len(lst) > 0:
            n = len(lst[0])
        for x in lst:
            if len(x) != n:
                return None
        return np.array(lst)
        
    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        if len(tpl) > 0:
            n = len(tpl[0])
        for x in tpl:
            if len(x) != n:
                return None
        return np.array(tpl)
        
    def from_iterable(self, itr):
        return np.array(list(itr))
        
    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            return None
        for x in shape:
            if x <= 0:
                return None
        return np.full(shape, value)
        
    def random(self, shape):
        if not isinstance(shape, tuple):
            return None
        return np.random.random(shape)

    def identity(self, n):
        if not isinstance(n, int) or n <= 0:
            return None
        return np.identity(n)