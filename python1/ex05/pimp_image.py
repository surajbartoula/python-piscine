"""Module containing restrictive matrix-based color filters for RGB images."""
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received"""
    # Creating copy so we dont mutate the input array
    inverted = array.copy()
    inverted[:, :, :3] = 255 - inverted[:, :, :3]
    plt.imshow(inverted)
    plt.title("Inverted Filter")
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter by zeroing out green and blue channels."""
    red_img = array.copy()
    # Multiply Green(1) & Blue(2) channels by 0 to isolate Red
    red_img[:, :, 1] = red_img[:, :, 1] * 0
    red_img[:, :, 2] = red_img[:, :, 2] * 0
    plt.imshow(red_img)
    plt.title("Red Filter")
    plt.show()
    return red_img


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter by substracting Red & Blue channels from themselves."""
    green_img = array.copy()
    # Substracting a channel from iteself results in 0
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
    plt.imshow(green_img)
    plt.title("Green Filter")
    plt.show()
    return green_img


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter by zeroing out Red & Green channels using assignments."""
    blue_img = array.copy()
    # Direct assign 0 to Red(0) and Green(0) channels
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    plt.imshow(blue_img)
    plt.title("Blue Filter")
    plt.show()
    return blue_img


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the img to grayscale using channel broadcast distribution."""
    grey_img = array.copy()
    total_sum = np.sum(grey_img[:, :, :3], axis=2)
    gray_channel = (total_sum / 3).astype(np.uint8)
    # Assign single channel to all 3 slots to remove color variation
    grey_img[:, :, 0] = gray_channel
    grey_img[:, :, 1] = gray_channel
    grey_img[:, :, 2] = gray_channel
    plt.imshow(grey_img)
    plt.title("Grey Filter")
    plt.show()
    return grey_img
