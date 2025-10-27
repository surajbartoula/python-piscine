import sys

try:
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) == 2:
		try:
			arg = int(sys.argv[1])
		except ValueError:
			raise AssertionError("argument is not an integer")
			sys.exit(1)
		if (arg % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
except AssertionError as e:
	print(f"AssertionError: {e}")
