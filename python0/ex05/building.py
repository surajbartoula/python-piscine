import sys


def main():
    """
    Main function to run the program.

    Checks how many argument provided by the user
    If the user provides more than 2 argument, assertionerror is given
    If the user provides no argument except the program itself then we
    ask for the input from the user
    If the user provides 1 argument with program then we call building to
    process it
    """
    try:
        if len(sys.argv) == 1:
            txt = input("What is the text to count?\n")
            txt += '\n'
            building(txt)
        elif len(sys.argv) == 2:
            building(sys.argv[1])
        else:
            raise AssertionError("more than one argument is provided")
    except Exception as e:
        print(f"AssertionError: {e}")
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


def building(txt):
    """
    Takes a single string and displays the sum of its upper-case
    characters, lower-case characters, punctuation characters, digits
    and spaces.

    Parameters:
    txt string

    Returns:
    Nothing only prints
    """
    total_chars = len(txt)
    upper_count = sum(1 for c in txt if c.isupper())
    lower_count = sum(1 for c in txt if c.islower())
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punct_count = sum(1 for c in txt if c in punctuations)
    space_count = sum(1 for c in txt if c.isspace())
    digit_count = sum(1 for c in txt if c.isdigit())

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
