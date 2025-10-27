import sys

assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
arg = int(sys.argv[1])
if not isinstance(arg, int):
    raise TypeError("AssertionError: argument is not an integer")
if (arg % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
