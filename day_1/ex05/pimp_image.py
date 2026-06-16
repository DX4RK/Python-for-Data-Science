from PIL import Image
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color fo the image received."""
    inverted = 255 - array
    return Image.fromarray(inverted).show()


def ft_red(array) -> np.ndarray:
    """Converts the image by turning its colors red."""
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0

    image = Image.fromarray(red)
    image.save("")
    return image


def ft_green(array) -> np.ndarray:
    """Converts the image by turning its colors green."""
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]

    image = Image.fromarray(green)
    image.show()
    return image


def ft_blue(array) -> np.ndarray:
    """Converts the image by turning its colors blue."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    image = Image.fromarray(blue)
    image.show()
    return image


def ft_grey(array):
    """Converts the image by turning its colors grey."""
    grey = np.mean(array, axis=2, keepdims=True)
    np_grey = np.squeeze(grey, axis=2)

    image = Image.fromarray(np_grey)
    image.show()
    return image
