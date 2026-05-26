"""Module for validating, shaping and slicing 2D array"""
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print shapes & slice a 2D list into a truncated version using NumPy.
    Args:
        family (list): A 2D list representing rows of data
        start (int): The starting index for the slice
        end (int): The ending index for the slice.
    Returns: Sliced nested list."""
    if not isinstance(family, list):
        raise TypeError("The 'family' parameter must be list.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers.")
    if len(family) > 0:
        if not isinstance(family[0], list):
            raise TypeError("The family list must contain nested lists.")
        row_length = len(family[0])
        for row in family:
            if not isinstance(row, list):
                raise TypeError("All elements of family must be lists.")
            if len(row) != row_length:
                raise ValueError("All rows in the 2D list must be same size.")
    np_arr = np.array(family)
    print(f"My shape is : {np_arr.shape}")
    sliced_arr = np_arr[start:end]
    print(f"My new shape is : {sliced_arr.shape}")
    return sliced_arr.tolist()


def main():
    """
    Empty main function to satisfy the project requirement
    without exectuting additional test logic
    """
    pass


if __name__ == "__main__":
    main()