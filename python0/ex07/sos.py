import sys


def encode_to_morse(text: str) -> str:
    """
    Translate an alphanumeric string into Morse code.
    Args:
        text (str): The input string to be encoded.
    Returns:
        str: The encoded Morse code string.
    """
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ",
        "8": "---.. ", "9": "----.. "
    }
    encoded_message = ""
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise ValueError("Invalid character")
        encoded_message += NESTED_MORSE[char]
    # strip the trailing space for clean output
    return encoded_message.strip()


def main():
    """
    Main function to handle command-line arguments and error management.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        input_string = sys.argv[1]
        if not isinstance(input_string, str):
            raise AssertionError("the argument are bad")
        result = encode_to_morse(input_string)
        print(result)
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
    except Exception:
        print("AssertionError: the argument are bad")


if __name__ == "__main__":
    main()
