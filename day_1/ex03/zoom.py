from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    image_path = "animal.jpeg"
    image = ft_load(image_path)
    if image is None:
        return
    print(image)

    zoomed = image[100:500, 450:850, 0:1]

    print(f"New shape after slicing: {zoomed.shape} or {zoomed.shape[:2]}")
    print(zoomed)

    plt.imshow(zoomed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
