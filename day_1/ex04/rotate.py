from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    image_path = "animal.jpeg"
    image = ft_load(image_path)
    if image is None:
        return
    print(image)

    zoom = image[100:500, 450:850, 0:1]
    print(f"The shape of image is: {zoom.shape} or {zoom.shape[:2]}")
    print(zoom)
    print(zoom[0][0])
    roated_img = []
    for x in range(zoom.shape[1]):
        row = []
        for y in range(zoom.shape[0]):
            row.append(zoom[y][x])
        roated_img.append(row)

    plt.imshow(np.array(roated_img), cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
