"""Module to calculate BMI values and check them against a limit threshold."""


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
    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float) or not isinstance(w, (int, float))):
            raise TypeError("All elements must be integers or floats.")
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        if w <= 0:
            raise ValueError("Weight cannot be negative")
        bmi = w / (h**2)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int | float) -> list[bool]:
    """Check which BMI values from a list strictly exceed a given limit.
    Args: bmi: A list of calculated BMI values.
    Returns: List of bool with TRUE if the BMI is above the limit,
    False otherwise."""
    if not isinstance(bmi, list):
        raise TypeError("BMI must be provided as a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an integer or a float.")
    limit_results = []
    for val in bmi:
        if not isinstance(val, (int, float)):
            raise TypeError("All elements in BMI list must be numbers.")
        limit_results.append(val > limit)
    return limit_results


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
