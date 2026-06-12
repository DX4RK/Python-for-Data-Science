from load_image import ft_load
import numpy as np

def main():
    image_path = "animal.jpeg"
    image, pixels, pixels_array = ft_load(image_path)
    print(pixels_array)

    height, width, channels = pixels.shape
    start_y = (height - 400) // 2
    start_x = (width - 400) // 2

    zoom = pixels[start_y:start_y + 400, start_x:start_x + 400]
    zoom_pixels = []

    for y in range(height):
        for x in range(width):
            zoom_pixels.append(
                image.getpixel((x, y))
            )
    zoom_pixels_array = np.array(zoom_pixels)

    print(f"New shape after slicing: {zoom.shape}")
    print(zoom_pixels_array)

if __name__ == "__main__":
    main()
