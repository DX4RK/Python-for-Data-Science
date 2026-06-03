def ft_filter(func: callable, iterable: list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    new_iterable = []
    for value in iterable:
        try:
            if func and func(value) or value:
                new_iterable.append(value)
        finally:
            continue
    return new_iterable
