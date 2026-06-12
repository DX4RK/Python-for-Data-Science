import numpy as np


def is_array_int_or_float(array) -> bool:
    """Check if array contains only int or float"""
    return (
        np.issubdtype(array.dtype, np.integer)
        or np.issubdtype(array.dtype, np.floating)
    )


def validate_parameters(array, start: int, end: int) -> bool:
    """Validate parametrs, returns false if parameters are bad."""
    return (
        isinstance(start, int)
        and isinstance(end, int)
        and is_array_int_or_float(array)
    )


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of family list and truncated version of it"""
    family_array = np.array(family)

    if not validate_parameters(family_array, start, end):
        raise ValueError("Invalid parameters.")

    truncated_array = family_array[start:end]

    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {truncated_array.shape}")

    return truncated_array.tolist()
