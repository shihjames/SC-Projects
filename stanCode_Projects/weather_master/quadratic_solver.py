"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


import math


def main():
	"""
	The program will ask user to input three values(a, b and c),
	these values represent three coefficient of ax^2 + bx + c = 0.
	Finally, the program will tell how many real roots exist
	and the value of the roots(if they exist).
	"""
	print('stanCode Quadratic Solver!')
	# Asking for input 'a'.
	a = float(input('a: '))
	# If input 'a' is zero, the program will stop.
	if a == 0:
		print('Sorry! input "a" cannot be zero')
	else:
		b = float(input('b: '))
		c = float(input('c: '))
		find_root(a, b, c)


def find_root(a, b, c):
	"""
	There are three kinds of situations. First, if the discriminant is
	bigger than zero, the function will print 'Two roots' and their
	values. Secondly, if the discriminant equals to zero, the function
	will print 'One root' and its value. Finally, if the discriminant
	is smaller than zero, the function will print 'No real roots'.
	"""
	if b**2-4*a*c > 0:
		y = math.sqrt(b ** 2 - 4 * a * c)
		discriminant = 'Two roots: ' + str((-1 * b + y) / (2 * a)) + ', ' + str((-1 * b - y) / (2 * a))
		print(discriminant)
	elif b**2-4*a*c == 0:
		y = math.sqrt(b ** 2 - 4 * a * c)
		discriminant = 'One root: ' + str((-1 * b + y) / (2 * a))
		print(discriminant)
	else:
		discriminant = 'No real roots'
		print(discriminant)


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
