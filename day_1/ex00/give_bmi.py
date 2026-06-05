import numpy as np


def is_array_int_or_float(array: np.array) -> bool:
    return np.issubdtype(array.dtype, np.integer) or\
           np.issubdtype(array.dtype, np.floating)


def vaidate_arrays(h_arr: np.array, w_arr: np.array) -> bool:
    return (h_arr.size == w_arr.size) and \
        (is_array_int_or_float(h_arr) and is_array_int_or_float(w_arr))


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate bmi based on given parameters."""
    height_array = np.array(height)
    weight_array = np.array(weight)

    if not vaidate_arrays(height_array, weight_array):
        return []

    result = np.divide(weight_array, height_array ** 2)
    return result.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi)
    if not is_array_int_or_float(bmi_array):
        return []
    return (bmi_array > limit).tolist()
