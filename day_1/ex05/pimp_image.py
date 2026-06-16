from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def ft_invert(array) -> np.ndarray:
    inverted = 255 - array
    return Image.fromarray(inverted)

def ft_red(array) -> np.ndarray:
    

def main():
    image_path = "landscape.jpg"
    image = ft_load(image_path)
    if image is None:
        return

    img = ft_invert(image)
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()
