"""
File: largest_digit.py
Name: James Shih
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
count = 0


def main():
	"""
	Given a number, the program will find the largest digit of the number by a recursive algorithm.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function will execute a helper function to find the largest digit recursively.
	:param n: int, input number.
	:return largest: int, the largest digit of the number.
	"""
	num = abs(n)
	return helper(num, 0)


def helper(num, current):
	if num == 0:
		return current
	else:
		rem = num % 10
		if rem > current:
			current = rem
		return helper(num//10, current)


if __name__ == '__main__':
	main()
