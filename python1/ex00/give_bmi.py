"""Module to calculate BMI values and check them against a limit threshold."""
import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Calculate Body Mass Index (BMI) from lists of heights and weights.
    Formula used: BMI = weight / (height^2)
    Args: Height in meters and weight in kg.
    Returns: BMI values."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be provided as lists.")
    if len(height) != len(weight):
        raise ValueError("Height & weight list must be the same length.")
    try:
        np_height = np.array(height, dtype=float)
        np_weight = np.array(weight, dtype=float)
    except (ValueError, TypeError) as e:
        raise TypeError(
            "All elements in height & weight must be numbers."
        ) from e
    if np.any(np_height <= 0):
        raise ValueError("Height cannot be negative.")
    if np.any(np_weight <= 0):
        raise ValueError("Weight cannot be negative.")
    bmi_array = np_weight / (np_height ** 2)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int | float) -> list[bool]:
    """Check which BMI values from a list strictly exceed a given limit.
    Args: bmi: A list of calculated BMI values.
    Returns: List of bool with TRUE if the BMI is above the limit,
    False otherwise."""
    if not isinstance(bmi, list):
        raise TypeError("BMI must be provided as a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an integer or a float.")
    try:
        np_bmi = np.array(bmi, dtype=float)
    except (ValueError, TypeError) as e:
        raise TypeError("Elements in BMI List must be numbers.") from e
    # Vectorized comparision
    limit_results = np_bmi > limit
    return limit_results.tolist()


def main():
    """Execute evaluation tests and handle potential runtime execeptions."""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
