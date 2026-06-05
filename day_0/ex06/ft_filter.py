def ft_filter(func: callable, iterable: list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if not func:
        return list
    return [value for value in iterable if func(value)]
