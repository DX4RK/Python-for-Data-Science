import PIL
from PIL import Image
import numpy as np


def check_file(path: str) -> PIL.Image:
    """Check if file path really exist."""
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return
    return image


def ft_load(path: str) -> np.ndarray:
    """"Load an image from path, print its shape, and return its pixels."""
    image = check_file(path)

    if not image:
        print("Image not found.")
        return

    pixels_list = []
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixels_list.append(
                image.getpixel((x, y))
            )
    pixels = np.array(image)
    pixels_array = np.array(pixels_list)

    print(f"The shape of image {pixels.shape}")
    return pixels_array
