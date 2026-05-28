"""Module to manually transpose a cropped grayscale image section."""
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_zoom(img: np.ndarray, zh: int = 400, zw: int = 400) -> np.ndarray:
    """Crop the input image to a specific size centered within the original image.
    Args:
        img (np.ndarray): The source image array.
        zh (int): Target height of the zoom window.
        zw (int): Target width of the zoom window.
    Returns:
        np.ndarray: The centered cropped image zone."""
    h, w, _ = img.shape
    # Compute starting margins from the edges to find the absolute center
    start_row = (h - zh) // 2
    start_col = (w - zw) // 2
    return img[start_row : start_row + zh, start_col : start_col + zw]


def ft_grayscale(img: np.ndarray) -> np.ndarray:
    """Convert an RGB image array to a 2D grayscale array.
    Args:
        img (np.ndarray): The RBG image array.
    Returns:
        np.ndarray: The 2D grayscale image array (uint8)."""
    grayscale_img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    return grayscale_img.astype(np.uint8)


def ft_transpose(img: np.ndarray) -> np.ndarray:
    """Manually transpose a 2D matrix
    Args:
        img (np.ndarray): The 2D source matrix.
    Returns:
        np.ndarray: The manually transposed 2D matrix.
    """
    rows, cols = img.shape
    transposed_list = [
        [img[r][c] for r in range(rows)]
        for c in range(cols)
    ]
    return np.array(transposed_list, dtype=np.uint8)


def transpose_image():
    """Load an image, crop it and transpose"""
    try:
        original_img = ft_load("animal.jpeg")
        cropped_img = ft_zoom(original_img, zh=400, zw=400)
        grayscale_img = ft_grayscale(cropped_img)
        print(f"The shape of image is : {grayscale_img.shape}")
        print(grayscale_img)
        transposed_img = ft_transpose(grayscale_img)
        print(f"New shape after Transpose: {transposed_img.shape}")
        print(transposed_img)
        # Render the result in grid view
        plt.imshow(transposed_img, cmap="gray")
        plt.show()
    except (TypeError, ValueError, FileNotFoundError, RuntimeError) as e:
        print(f"An expected error occured: {e}")
    except Exception as e:
        print(f"An unexpected tracking error occurred: {e}")


def main():
    """Main execution block."""
    transpose_image()


if __name__ == "__main__":
    main()
