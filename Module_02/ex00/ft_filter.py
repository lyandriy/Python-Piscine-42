from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("ERROR")
    for x in iterable:
        if function_to_apply(x):
            yield x

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    print(ft_filter(lambda dum: not (dum % 2), x))
    print(list(ft_filter(lambda dum: not (dum % 2), x)))