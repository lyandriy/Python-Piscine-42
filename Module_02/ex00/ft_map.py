from collections.abc import Iterable

def myfunc(a, b):
    return a + b

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if isinstance(iterable, Iterable):
        for x in iterable:
            yield function_to_apply(x)
    else:
        raise TypeError("ERROR")


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(list(ft_map(lambda dum: dum + 1, x)))
    print(list(ft_map(lambda t: t + 1, x)))