import sys


def text_analyzer(text: str):
    """
    Analyzes a string & counts upper-case, lower-case,
    punctuation, spaces and digits.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    counts = {
        "upper": 0,
        "lower": 0,
        "punct": 0,
        "space": 0,
        "digit": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        elif char.isspace():
            counts["space"] += 1
        elif char in punctuation:
            counts["punct"] += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main():
    """
    Main entry point of the script. Handles argument logic and exceptions.
    """
    try:
        argv = sys.argv
        if len(argv) > 2:
            raise AssertionError('more than one argument is provided')
        if len(argv) < 2 or argv[1] is None or argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = argv[1]
        text_analyzer(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
