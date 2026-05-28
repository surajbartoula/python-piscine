"""Module to load images and convert into printable pixel arrays."""
import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image, display it's structural shape and return it's RGB pixels.
    Args:
        path (str): The file path to the target image.
    Returns:
        np.ndarray: A 3D array containing the RGB pixel values of the iamge."""
    if not isinstance(path, str):
        raise TypeError("The image path must be a string.")
    lower_path = path.lower()
    if not (lower_path.endswith(".jpg") or lower_path.endswith(".jpeg")):
        raise ValueError("Unsupported file format. Only JPG & JPEG allowed.")
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file assets at '{path}' were not found.")
    try:
        with Image.open(path) as img:
            rgb_img = img.convert("RGB")
            img_array = np.array(rgb_img)
            return img_array
    except Exception as e:
        raise RuntimeError(f"Failed to process the image: {e}")


def main():
    """
    Empty main function to satisfy the project requirement
    without exectuting additional test logic
    """
    pass


if __name__ == "__main__":
    main()
