"""Module to crop, convert to grayscale and display a specific image zone."""
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def zoom_image():
    """Load animal.jpeg, apply spatial slicing/grayscale and show the output."""
    try:
        original_img = ft_load("animal.jpeg")
        print(original_img)
        # Crop the image zone (400X400 area)
        # Slicing from row 100 to 500, column 450 to 850
        cropped_img = original_img[100:500, 450:850]
        # Convert to Grayscale
        # Using the standard luminosity formula: Y = 0.299R + 0.587G + 0.114B
        grayscale_img = np.dot(cropped_img[..., :3], [0.299, 0.587, 0.114])
        # Convert to int
        grayscale_img = grayscale_img.astype(np.uint8)
        # Reshape to explicitly match the required (400, 400, 1)
        zoomed_array = grayscale_img[:, :, np.newaxis]
        print(f"New shape after slicing: {zoomed_array.shape}")
        print(zoomed_array)
        # Display the img with visible axis
        plt.imshow(grayscale_img, cmap="gray")
        plt.title("Zoomed Grayscale Image")
        plt.show()
    except (TypeError, ValueError, FileNotFoundError, RuntimeError) as e:
        print(f"An expected error occured: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def main():
    """Main execution block"""
    zoom_image()


if __name__ == "__main__":
    main()
