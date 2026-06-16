from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def main():
    image_path = "animal.jpeg"
    image = ft_load(image_path)
    if image is None:
        return
    print(image)

    zoomed_img = image[100:500, 450:850, 0:1]
    print(f"The shape of image is: {zoomed_img.shape} or {zoomed_img.shape[:2]}")
    print(zoomed_img)
    print(zoomed_img[0][0])
    roated_img = []
    for x in range(zoomed_img.shape[1]):
        row = []
        for y in range(zoomed_img.shape[0]):
            row.append(zoomed_img[y][x])
        roated_img.append(row)

    plt.imshow(np.array(roated_img), cmap="gray")
    plt.show()

if __name__ == "__main__":
    main()
