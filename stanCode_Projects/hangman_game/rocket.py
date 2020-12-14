"""
File: rocket.py
Name: James Shih
----------------------------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

SIZE = 2


def main():
	"""
	This program will build a rocket, and the user can easily
	adjust its size by changing the constant (SIZE). The program
	will execute function build_head(), build_belt(), build_upper()
	build_lower(), build_belt() and build_head(), respectively.
	"""
	build_head()
	build_belt()
	build_upper()
	build_lower()
	build_belt()
	build_head()


def build_head():
	"""
	This function will build the head or the flame of the rocket.
	"""
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')
		for j in range(i+1):
			print('/', end='')
		for j in range(i+1):
			print('\\', end='')
		for j in range(SIZE-i):
			print(' ', end='')
		print('')


def build_belt():
	"""
	This function will build the junction of the rocket.
	"""
	print('+', end='')
	for j in range(SIZE*2):
		print('=', end='')
	print('+')


def build_upper():
	"""
	This function will build the upper part of the rocket.
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE-i-1):
			print('.', end='')
		for j in range(i+1):
			print('/', end='')
			print('\\', end='')
		for j in range(SIZE-i-1):
			print('.', end='')
		print('|')


def build_lower():
	"""
	This function will build the lower part of the rocket.
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE-i):
			print('\\', end='')
			print('/', end='')
		for j in range(i):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()