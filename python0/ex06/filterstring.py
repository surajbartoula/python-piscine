import sys


def filter_words(text, length):
    """
    Filter words from a string that are strictly longer than a given integer.

    Args:
        text (str): The string to parse.
        length (int): The minimum length threshold.
    Returns:
        list: A list of words with length > n.
    """

    return [word for word in text.split() if (lambda w: len(w) > length)(word)]


def main():
    """
    Main function to handle CLI arguments and execute word filtering.
    Validate input count and types before processing.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the argument are bad")
        arg_string = sys.argv[1]
        arg_integer = sys.argv[2]
        if not isinstance(arg_string, str) or not arg_integer.isdigit():
            raise AssertionError("the arguments are bad")
        result = filter_words(arg_string, int(arg_integer))
        print(result)
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
