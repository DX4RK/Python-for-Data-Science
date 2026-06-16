import PIL
from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """Load an image from path, print its shape, and return its pixels in RGB."""
    try:
        image = Image.open(path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error: could not load image: {e}")
        return None

    pixels = np.array(image)
    print(f"The shape of image is: {pixels.shape}")
    print(pixels)
    return pixels
